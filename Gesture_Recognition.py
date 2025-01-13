# import cv2
# import numpy as np
# import mediapipe as mp

# # Initialize the MediaPipe Hands solution
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
# mp_drawing = mp.solutions.drawing_utils

# # Load the Haar cascade for face detection
# face_features = cv2.CascadeClassifier("C:/Users/user/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# # Turn on the camera
# video_cap = cv2.VideoCapture(0)

# while True:
#     ret, video_data = video_cap.read()
#     if not ret:
#         break

#     # Convert frame to grayscale for face detection
#     video_col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
#     faces = face_features.detectMultiScale(
#         video_col,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )

#     # Perform face detection
#     for (x, y, w, h) in faces:
#         cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     # Convert the frame to RGB for hand detection
#     video_rgb = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)

#     # Perform hand detection
#     results = hands.process(video_rgb)

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Draw hand landmarks on the frame
#             mp_drawing.draw_landmarks(video_data, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#     # Display the frame
#     if ret:
#         cv2.imshow('video_live', video_data)

#     # Save the frame
#     cv2.imwrite('frame.jpg', video_data)

#     # Turning off the camera
#     if cv2.waitKey(10) == ord('a'):
#         break

# # Release the camera and close all windows
# video_cap.release()
# cv2.destroyAllWindows()
# ------------------------------------------------------------------------------------------------------------------------
# functionality to detect a plus symbol with fingers and invoke the finger-counting function if the plus symbol is detected. We'll define a separate function for counting the raised fingers and integrate it into the main loop.\
import cv2
import numpy as np
import mediapipe as mp

# Initialize the MediaPipe Hands solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load the Haar cascade for face detection
face_features = cv2.CascadeClassifier("C:/Users/user/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Finger names corresponding to the indices in the hand landmarks
finger_names = ["Thumb", "Index Finger", "Middle Finger", "Ring Finger", "Pinky Finger"]

# Function to count raised fingers
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    count = 0
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

def get_raised_fingers(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    raised_fingers = []
    for i, tip in enumerate(finger_tips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y: 
            raised_fingers.append(finger_names[i])
            return raised_fingers

# Function to check for plus symbol
def is_plus_symbol(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    return thumb_tip.x < index_tip.x and abs(thumb_tip.y - index_tip.y) < 0.05

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

    left_hand_fingers = 0
    right_hand_fingers = 0
    index_fingers_up = False

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = handedness.classification[0].label
            raised_fingers = get_raised_fingers(hand_landmarks)
            # Check if the index finger is up
            if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:
                index_fingers_up = True

            # Count the number of raised fingers
            num_fingers = count_fingers(hand_landmarks)

            if hand_label == 'Left':
                left_hand_fingers = num_fingers
            else:
                right_hand_fingers = num_fingers

            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(video_data, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            if hand_label == "Right":
                for i, finger_name in enumerate(raised_fingers):
                    cv2.putText(video_data, finger_name, (10, 50 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                  
    # If the index fingers are up, calculate the total number of raised fingers
    if index_fingers_up:
        total_fingers = left_hand_fingers + right_hand_fingers
        cv2.putText(video_data, f'Total fingers: {total_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the frame
    if ret:
        cv2.imshow('video_live', video_data)

    # Save the frame
    cv2.imwrite('frame.jpg', video_data)

    # Turning off the camera
    if cv2.waitKey(10) == ord('a'):
        break

# Release the camera and close all windows
video_cap.release()
cv2.destroyAllWindows()
