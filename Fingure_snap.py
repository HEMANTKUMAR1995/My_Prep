import cv2
import numpy as np
import mediapipe as mp
import time

# Initialize the MediaPipe Hands solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load the Haar cascade for face detection
face_features = cv2.CascadeClassifier("C:/Users/user/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Function to detect snapping gesture
def is_snapping(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    middle_tip = hand_landmarks.landmark[12]
    return abs(thumb_tip.x - middle_tip.x) < 0.05 and abs(thumb_tip.y - middle_tip.y) < 0.05

# Function to get the names of raised fingers
def get_raised_fingers(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    finger_names = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Pinky Finger"]
    raised_fingers = []
    for i, tip in enumerate(finger_tips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            raised_fingers.append(finger_names[i])
    return raised_fingers

# Turn on the camera
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    if not ret:
        break

    # Convert frame to grayscale for face detection
    video_col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_features.detectMultiScale(
        video_col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Perform face detection
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Convert the frame to RGB for hand detection
    video_rgb = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)

    # Perform hand detection
    results = hands.process(video_rgb)

    snapping_detected = False

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            raised_fingers = get_raised_fingers(hand_landmarks)

            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(video_data, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Check for snapping gesture
            if is_snapping(hand_landmarks):
                snapping_detected = True

            # Display the names of raised fingers
            for i, finger_name in enumerate(raised_fingers):
                cv2.putText(video_data, finger_name, (10, 50 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Take a screenshot if snapping is detected
    if snapping_detected:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        cv2.imwrite(f'screenshot_{timestamp}.jpg', video_data)
        cv2.putText(video_data, "Screenshot taken", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    if ret:
        cv2.imshow('video_live', video_data)

    # Turning off the camera
    if cv2.waitKey(10) == ord('a'):
        break

# Release the camera and close all windows
video_cap.release()
cv2.destroyAllWindows()
