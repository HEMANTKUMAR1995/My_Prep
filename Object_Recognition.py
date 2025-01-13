import cv2
import numpy as np

# Load the pre-trained MobileNet-SSD model
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Class labels the model can detect
class_names = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant",
               "sheep", "sofa", "train", "tvmonitor"]

# Load the Haar cascade for face detection
face_features = cv2.CascadeClassifier("C:/Users/user/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")

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

    # Perform object detection
    blob = cv2.dnn.blobFromImage(cv2.resize(video_data, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Draw bounding boxes for faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Loop over the detections for objects
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.2:  # Set a confidence threshold
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([video_data.shape[1], video_data.shape[0], video_data.shape[1], video_data.shape[0]])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw the bounding box and label for detected objects
            label = "{}: {:.2f}%".format(class_names[idx], confidence * 100)
            cv2.rectangle(video_data, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(video_data, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame
    if ret:
        cv2.imshow('video_live', video_data)

    # Save the frame
    cv2.imwrite('frame.jpg', video_data)

    # Turning off the camera
    if cv2.waitKey(10) == ord('x'):
        break

# Release the camera and close all windows
video_cap.release()
cv2.destroyAllWindows()
