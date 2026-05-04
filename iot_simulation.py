"""
IoT Sensor Simulation Script
Simulates entry/exit sensors and sends data to Firebase
"""

import firebase_admin
from firebase_admin import credentials, db
import random
import time
from datetime import datetime, timedelta
import threading
from twilio.rest import Client

# Twilio Configuration
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"  # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = "+1234567890"  # Replace with your Twilio phone number
CITIZEN_PHONE_NUMBERS = ["+1987654321"]  # Replace with citizen phone numbers to notify

class IoTSensorSimulator:
    def __init__(self):
        self.current_count = 45  # Starting crowd count
        self.running = False
        self.last_notification_time = 0  # Track when the last notification was sent
        
    def init_firebase(self):
        """
        Initialize Firebase with the project configuration
        """
        try:
            cred = credentials.Certificate("firebase-key.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'YOUR DATABASE URL'
            })
            print("Firebase initialized successfully")
        except Exception as e:
            print(f"Firebase initialization error: {e}")
    
    def simulate_entry_exit(self):
        """
        Simulate realistic entry/exit patterns
        """
        current_hour = datetime.now().hour
        
        # Adjust probabilities based on time of day
        if 9 <= current_hour <= 17:  # Business hours
            entry_prob = 0.7
            exit_prob = 0.3
        elif 18 <= current_hour <= 22:  # Evening
            entry_prob = 0.4
            exit_prob = 0.6
        else:  # Night/early morning
            entry_prob = 0.2
            exit_prob = 0.8
        
        # Simulate sensor events
        if random.random() < 0.3:  # 30% chance of activity per cycle
            if random.random() < entry_prob:
                # Entry detected
                self.current_count += random.randint(1, 3)
                event_type = "ENTRY"
                change = "+1-3"
            else:
                # Exit detected
                self.current_count -= random.randint(1, 2)
                event_type = "EXIT"
                change = "-1-2"
            
            # Ensure count doesn't go below 0
            self.current_count = max(0, self.current_count)
            
            return event_type, change
        
        return None, None
    
    def send_to_firebase(self, event_type=None, change=None):
        """
        Send sensor data to Firebase
        """
        try:
            # Get current status before sending data
            current_status = self.get_crowd_status()
            
            ref = db.reference('crowd_data')
            data = {
                'count': self.current_count,
                'timestamp': datetime.now().isoformat(),
                'source': 'IoT_Sensor',
                'location': 'Main Plaza',
                'event_type': event_type,
                'change': change,
                'status': current_status
            }
            ref.push(data)
            
            # Also update current status
            status_ref = db.reference('current_status')
            status_ref.set({
                'count': self.current_count,
                'last_update': datetime.now().isoformat(),
                'status': current_status
            })
            
            # If status is High, also create an alert in Firebase
            if current_status == "High":
                # Check if we should send an alert (limit to once every 5 minutes)
                current_time = time.time()
                if current_time - self.last_notification_time > 300:  # 300 seconds = 5 minutes
                    alert_ref = db.reference('alerts')
                    alert_data = {
                        'message': 'High crowd density detected!',
                        'level': 'HIGH',
                        'count': self.current_count,
                        'timestamp': datetime.now().isoformat(),
                        'location': 'Main Plaza'
                    }
                    alert_ref.push(alert_data)
                    self.last_notification_time = current_time
                    print(f"🚨 High crowd alert sent to Firebase: {self.current_count} people")
            
            print(f"📡 Sent to Firebase: {self.current_count} people | Status: {current_status} | Event: {event_type}")
            
        except Exception as e:
            print(f"Firebase error: {e}")
    
    def get_crowd_status(self):
        """
        Determine crowd status level
        """
        if self.current_count < 30:
            return "Low"
        elif self.current_count < 70:
            return "Medium"
        else:
            # Check if we should send a notification (limit to once every 5 minutes)
            current_time = time.time()
            if current_time - self.last_notification_time > 300:  # 300 seconds = 5 minutes
                location = "Main Plaza"  # This could be dynamic based on sensor location
                message = f"High crowd density detected"
                send_sms_notification(message, location, self.current_count)
                self.last_notification_time = current_time
            return "High"
    
    def run_simulation(self, duration_minutes=60):
        """
        Run the IoT simulation for specified duration
        """
        self.running = True
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        
        print(f"🚀 Starting IoT simulation for {duration_minutes} minutes...")
        print(f"Initial crowd count: {self.current_count}")
        
        while self.running and time.time() < end_time:
            # Simulate sensor activity
            event_type, change = self.simulate_entry_exit()
            
            # Send data to Firebase
            self.send_to_firebase(event_type, change)
            
            # Display current status
            status = self.get_crowd_status()
            print(f"🏢 Current: {self.current_count} people | Status: {status} | Time: {datetime.now().strftime('%H:%M:%S')}")
            
            # Wait before next update (simulate real sensor frequency)
            time.sleep(random.uniform(2, 8))  # 2-8 seconds between updates
        
        print("🛑 IoT simulation stopped")
    
    def stop_simulation(self):
        """
        Stop the simulation
        """
        self.running = False

def send_sms_notification(message, location, count):
    """
    Send SMS notification to citizens using Twilio
    """
    try:
        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Format the message with location information
        formatted_message = f"🚨 CROWDSAFE ALERT: {message} at {location}. Current count: {count}. Please avoid this area if possible."
        
        # Send SMS to all citizen phone numbers
        for phone_number in CITIZEN_PHONE_NUMBERS:
            message = client.messages.create(
                body=formatted_message,
                from_=TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            print(f"📱 SMS notification sent to {phone_number}")
        return True
    except Exception as e:
        print(f"Failed to send SMS notification: {e}")
        return False

def send_test_alert():
    """
    Send a test high crowd alert
    """
    try:
        ref = db.reference('alerts')
        alert_data = {
            'message': 'High crowd density detected!',
            'level': 'HIGH',
            'count': 95,
            'timestamp': datetime.now().isoformat(),
            'location': 'Main Plaza'
        }
        ref.push(alert_data)
        print("🚨 Test alert sent to Firebase")
        
        # Also send SMS notification
        send_sms_notification("High crowd density detected!", "Main Plaza", 95)
    except Exception as e:
        print(f"Alert error: {e}")

if __name__ == "__main__":
    # Create simulator instance
    simulator = IoTSensorSimulator()
    
    # Initialize Firebase
    simulator.init_firebase()
    
    print("\n🔧 IoT Sensor Simulator")
    print("1. Run continuous simulation")
    print("2. Send test data")
    print("3. Send test alert")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            duration = int(input("Enter simulation duration in minutes (default 60): ") or 60)
            try:
                simulator.run_simulation(duration)
            except KeyboardInterrupt:
                simulator.stop_simulation()
                print("\n🛑 Simulation stopped by user")
        
        elif choice == "2":
            simulator.send_to_firebase("TEST", "0")
            print("✅ Test data sent")
        
        elif choice == "3":
            send_test_alert()
        
        elif choice == "4":
            simulator.stop_simulation()
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    print("👋 Goodbye!")