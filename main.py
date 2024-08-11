import cv2
import time

# Open a connection to the default camera (usually the first camera connected to the computer)
video = cv2.VideoCapture(0)

# Pause for a moment to allow the camera to initialize
time.sleep(1)

# Create a named window and specify the desired size (e.g., full HD resolution 1920x1080)
cv2.namedWindow("My video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("My video", 1280, 720)  # Adjust the size as needed, for example 1280x720

first_frame = None
# Start an infinite loop to continuously capture frames from the camera
while True:
    # Capture a frame from the video feed
    check, frame = video.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to the grayscale frame to reduce noise and detail
    gray_frame_gauss = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Set the first frame if it's not already set
    if first_frame is None:
        first_frame = gray_frame_gauss

    # Compute the absolute difference between the first frame and the current blurred frame
    delta_frame = cv2.absdiff(first_frame,gray_frame_gauss)

    # Apply a threshold to get a binary image
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]

    # Dilate the threshold image to fill in holes
    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)

    # Find contours in the threshold image
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small contours to reduce noise
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        # Draw a rectangle around the contour on the original frame
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("My video", frame)

    # Wait for 1 millisecond to see if a key is pressed
    key = cv2.waitKey(1)

    # If the 's' key is pressed, break out of the loop to stop the video feed
    if key == ord("s"):
        break

# Release the video capture object and close the camera connection
video.release()


