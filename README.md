# 📸 Motion Detection and Alert System 🚨

Welcome to the **Motion Detection and Alert System** project! This Python application uses OpenCV to detect motion via a webcam and sends an email alert with a snapshot when motion is detected. Perfect for basic home security or surveillance systems. 🏠👀

---

## 🎯 Features

- 🕵️‍♂️ **Real-time Motion Detection**: Detects motion using contours and highlights the detected object with a green rectangle.
- 📧 **Email Notifications**: Automatically sends an email with a snapshot when motion is detected.
- 🗑️ **Automatic Cleanup**: Cleans up the images folder to avoid clutter.
- 🧵 **Threading for Efficiency**: Uses threading to handle email sending and cleanup operations in the background.

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anindyaPrivate/Webcam_Monitoring_Email_Alert_System_using_OpenCV.git
   cd Webcam_Monitoring_Email_Alert_System_using_OpenCV
   ```
   
# Install the required dependencies
```bash
pip install -r requirements.txt
```
# Set up your environment variables
```bash
echo "webpassword=yourpassword" > .env
```
# Run the application
```bash
python motion_detection.py
```

# 🖥️ Usage
Start the program:
Once the program is running, it will open your webcam feed in a window called "My video". The application will begin detecting motion after initialization.

## Monitoring:

The program detects motion using frame differencing and highlights the motion with a green rectangle. 📐
When significant motion is detected, a snapshot is taken and stored in the images folder. 📸

## Email Alerts:

If motion is detected and then stops, an email with the snapshot is sent to the configured receiver. 📧
You will receive an email with the subject "New customer showed up!".
## Stopping the program:

To stop the motion detection, press the s key.
