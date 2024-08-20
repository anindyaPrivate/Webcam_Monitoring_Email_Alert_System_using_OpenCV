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
   
## Install the required dependencies
```bash
pip install -r requirements.txt
```
## Set up your environment variables

Create a '.env' file in the project directory and add your email credentials:
```bash
webpassword=yourpassword
```
## Run the application
```bash
python motion_detection.py
```

## 🖥️ Usage
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

## 📂 Project Structure
```bash
motion-detection-alert-system/
│
├── .env                  # Environment variables for email credentials
├── motion_detection.py    # Main script for motion detection
├── send_email.py          # Script for sending email alerts
├── images/                # Directory to store captured images
└── README.md              # This awesome README file 😎
```
## 🚀 Technologies Used
OpenCV for image processing and motion detection 🖼️

smtplib for sending email notifications 💌

Threading for efficient multi-tasking 🧵

## 📧 Email Functionality
The send_email.py script uses Gmail's SMTP server to send email alerts. Make sure to set up your .env file with your credentials. If you're using Gmail, ensure that "Less Secure Apps" is enabled in your Gmail settings (or use an app-specific password).

##🔧 Customization
Motion Sensitivity: You can adjust the motion sensitivity by modifying the contour area in motion_detection.py:
```bash
if cv2.contourArea(contour) < 5000:
    continue
```
Frame Size: You can adjust the frame size by modifying the resize dimensions:
```bash
cv2.resizeWindow("My video", 1280, 720)
```

## 🤝 Contributing
Feel free to submit issues, fork the repository, and make pull requests. Contributions are welcome! 🚀

## 🧑‍💻 Author
Made with ❤️ by Anindya Das




