# CrowdSafe: Real-Time Crowd Monitoring Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An AI-powered dashboard for real-time crowd detection, counting, and alerting using YOLOv8 and Streamlit.

---

## 📋 Features

* **Live Video Analysis**: Processes a video stream to detect and count people in real-time.
* **IoT Sensor Simulation**: Simulates data from entry/exit sensors for a comprehensive view.
* **Real-Time Statistics**: Displays the current crowd count, density status (Low, Moderate, High), and total people detected.
* **Incident Management**: Automatically detects high-density events and creates an incident.
* **SMS Alert System**: Instantly dispatches alerts to authorities via Twilio when a high-density incident is detected.
* **Firebase Integration**: Pushes real-time crowd data to a Firebase Realtime Database.
* **Configurable Controls**: Easily adjust detection confidence, cluster size, and alert thresholds from the sidebar.

---

## 🛠️ Technology Stack

* **Dashboard**: Streamlit
* **AI/Detection**: YOLOv8, PyTorch, OpenCV
* **Backend & Database**: Firebase Realtime Database
* **Alerting**: Twilio SMS API
* **Data Handling**: Pandas, NumPy

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

* Python 3.9 or higher
* Git

### 1. Clone the Repository

```bash
git clone [https://github.com/samulya896/CROWDSAFE.git](https://github.com/samulya896/CROWDSAFE.git)
cd CROWDSAFE
```

### 2. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

This project uses a `.env` file to securely manage API keys and other secrets.

**Create a file named `.env`** in the root of the project directory and paste the following content into it. You must replace the placeholder values with your actual credentials.

```env
# Path to your local video file
VIDEO_PATH="local_train.mp4"

# Path to your Firebase credentials file
FIREBASE_KEY_PATH="firebase-credentials.json"

# Your Firebase Realtime Database URL
FIREBASE_DB_URL="[https://your-project-id.firebaseio.com](https://your-project-id.firebaseio.com)"

# Twilio Credentials
TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN="your_twilio_auth_token"
TWILIO_PHONE_NUMBER="+15017122661"

# General Configuration
LOCATION_NAME="Your Location Name"

# List of authority phone numbers to alert, separated by commas
AUTHORITY_NUMBERS="+11234567890,+10987654321"
```
**Important:** The `.gitignore` file in this repository is configured to ignore the `.env` file, so your secrets will not be committed.

### 5. Add Local Files

1.  **Firebase Credentials**: Place your Firebase service account key file in the root folder and ensure its name matches the `FIREBASE_KEY_PATH` in your `.env` file (e.g., `firebase-credentials.json`).
2.  **Video File**: Place your video file in the root folder and ensure its name matches the `VIDEO_PATH` in your `.env` file (e.g., `local_train.mp4`).

---

## ▶️ Usage

Once all the dependencies are installed and your `.env` file is configured, run the Streamlit application from your terminal:

```bash
streamlit run app.py
```

The application will open in a new tab in your web browser.

---

## 📊 Data Flow

The system processes data from two main sources and channels it to the dashboard and alert systems via Firebase.

```
CCTV Video → YOLOv8 → People Count → Firebase
                                        ↓
IoT Sensors → Entry/Exit Events → Firebase
                                        ↓
Firebase → Real-time Updates → Dashboard
                                        ↓
High Crowd → Alert System → Twilio SMS
```