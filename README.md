# 🚀 CrowdSafe Nexus

An AI-powered real-time crowd monitoring and safety platform that detects crowd density, predicts risks, and triggers automated alerts to prevent accidents.

---

## 🎯 Features

🎥 Live Crowd Detection – Detects and counts people in real-time using YOLOv8  
📊 Crowd Density Analysis – Identifies dense clusters using proximity-based logic  
🚦 Multi-Level Alert System – SAFE 🟢 | MODERATE 🟠 | HIGH 🔴 | CRITICAL 🚨  
🗺️ Zone-Based Monitoring – Tracks crowd distribution (Left, Center, Right zones)  
🌡️ Heatmap Visualization – Real-time density heatmap overlay  
⚡ Surge Detection – Predicts sudden increase in crowd flow  
🧾 Incident Logging – Automatically logs high-risk events with timestamps  
📩 Alert System – Sends alerts via Email (SMTP) and optional Twilio SMS  
☁️ Firebase Integration – Real-time data sync and dashboard updates  
⚙️ Configurable Controls – Adjustable confidence, thresholds, and risk parameters  

---

## 🛠️ Tech Stack

**AI/ML:** YOLOv8, OpenCV (Python)  
**Dashboard:** Streamlit  
**Database:** Firebase Realtime Database  
**Alerts:** SMTP (Email), Twilio (optional)  
**Libraries:** NumPy, Pandas  

---

## 📋 Project Structure

```
crowdsafe/
├── app.py                 # Main Streamlit dashboard
├── requirements.txt       # Dependencies
├── assets/                # Images / screenshots
├── firebase/              # Firebase config files
├── utils/                 # Helper functions
├── models/                # AI model files
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+  
- Git  

### Installation

```
git clone https://github.com/your-username/CrowdSafe.git
cd CrowdSafe
python -m venv venv
```

### Activate Environment

**Windows:**
```
venv\Scripts\activate
```

**macOS/Linux:**
```
source venv/bin/activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

👉 Open in browser:  
http://localhost:8501  

---

## 📡 System Workflow

Video Input (CCTV/Webcam)  
↓  
YOLOv8 Detection (People Count)  
↓  
OpenCV Processing (Bounding Boxes + Distance)  
↓  
Crowd Density Calculation  
↓  
Risk Classification (Safe → Critical)  
↓  
Firebase (Real-time Sync)  
↓  
Dashboard Visualization  
↓  
Alert System (Email / SMS)  

---

## 📊 Core Logic

- Detect people using YOLOv8  
- Calculate distance between individuals  
- Identify dense clusters  
- Compare with threshold values  
- Trigger alerts when risk increases  

---

## 📈 Use Cases

- Railway stations  
- Stadiums & events  
- Religious gatherings  
- Concerts  
- Smart city monitoring  

---

## 🔮 Future Enhancements

- Multi-camera integration  
- AI-based crowd prediction  
- Smart evacuation guidance  
- Map-based live tracking  
- Edge AI deployment  

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub  

---

## 📬 Contact

For issues or collaboration, open a GitHub issue  

---

Made with ❤️ for public safety 🚨
