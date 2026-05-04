# Firebase Setup Guide for Crowd Detection System

## 1. Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Create a project"
3. Enter project name: `crowd-detection-system`
4. Enable Google Analytics (optional)
5. Click "Create project"

## 2. Setup Realtime Database

1. In Firebase Console, go to "Realtime Database"
2. Click "Create Database"
3. Choose "Start in test mode" (for development)
4. Select database location (closest to your region)
5. Click "Done"

## 3. Configure Database Rules

Replace the default rules with:

```json
{
  "rules": {
    "crowd_data": {
      ".read": true,
      ".write": true
    },
    "current_status": {
      ".read": true,
      ".write": true
    },
    "alerts": {
      ".read": true,
      ".write": true
    }
  }
}
```

## 4. Get Configuration Keys

### For Web/React Dashboard:
1. Go to Project Settings (gear icon)
2. Scroll to "Your apps" section
3. Click "Web" icon to add web app
4. Register app with name "Crowd Dashboard"
5. Copy the config object:

```javascript
const firebaseConfig = {
  apiKey: "your-api-key",
  authDomain: "your-project.firebaseapp.com",
  databaseURL: "https://your-project-default-rtdb.firebaseio.com/",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "your-app-id"
};
```

### For Python Scripts (Colab/IoT):
1. Go to Project Settings → Service Accounts
2. Click "Generate new private key"
3. Download the JSON file
4. Upload this file to Google Colab or your Python environment

## 5. Setup Cloud Messaging (Optional)

1. In Firebase Console, go to "Cloud Messaging"
2. Add your app for notifications
3. Get the Server Key for sending notifications

## 6. Test Database Connection

Use Firebase Console's Database tab to manually add test data:

```json
{
  "current_status": {
    "count": 45,
    "status": "Medium",
    "last_update": "2024-01-01T12:00:00Z"
  }
}
```

## 7. Database Structure

Your database will have this structure:

```
crowd-detection-system/
├── crowd_data/
│   ├── -NxxxxxXXXXX/
│   │   ├── count: 45
│   │   ├── timestamp: "2024-01-01T12:00:00Z"
│   │   ├── source: "AI_Detection"
│   │   └── location: "Main Plaza"
│   └── ...
├── current_status/
│   ├── count: 45
│   ├── status: "Medium"
│   └── last_update: "2024-01-01T12:00:00Z"
└── alerts/
    └── -NyyyyyYYYYY/
        ├── message: "High crowd detected"
        ├── level: "HIGH"
        └── timestamp: "2024-01-01T12:00:00Z"
```

## 8. Security Notes

- For production, implement proper authentication
- Restrict database rules to authenticated users
- Use environment variables for sensitive keys
- Enable Firebase Security Rules

## 9. Integration Steps

1. **Streamlit Dashboard**: Update `app.py` with your Firebase config
2. **YOLOv8 Script**: Add your service account JSON to Colab
3. **IoT Simulator**: Update Python script with Firebase config  
4. **React Native App**: Update `firebaseConfig` in the app
5. **Notifications**: Configure FCM server key for alerts

## 10. Testing Checklist

- [ ] Database reads/writes work
- [ ] Real-time updates sync across apps
- [ ] Alerts trigger correctly
- [ ] Mobile app receives notifications
- [ ] Dashboard displays live data

## Troubleshooting

- **Connection issues**: Check database URL format
- **Permission denied**: Verify database rules
- **No real-time updates**: Ensure using Realtime Database (not Firestore)
- **Mobile app crashes**: Check Firebase config keys