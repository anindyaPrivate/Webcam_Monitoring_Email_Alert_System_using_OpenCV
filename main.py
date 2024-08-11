import cv2
import time

# Open a connection to the default camera (usually the first camera connected to the computer)
video = cv2.VideoCapture(0)

# Pause for a moment to allow the camera to initialize
time.sleep(1)

# Create a named window and specify the desired size (e.g., full HD resolution 1920x1080)
cv2.namedWindow("My video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("My video", 1280, 720)  # Adjust the size as needed, for example 1280x720

# Start an infinite loop to continuously capture frames from the camera
while True:
    # Capture a frame from the video feed
    check, frame = video.read()

    # Display the captured frame in the resized window named "My video"
    cv2.imshow("My video", frame)

    # Wait for 1 millisecond to see if a key is pressed
    key = cv2.waitKey(1)

    # If the 's' key is pressed, break out of the loop to stop the video feed
    if key == ord("s"):
        break

# Release the video capture object and close the camera connection
video.release()


