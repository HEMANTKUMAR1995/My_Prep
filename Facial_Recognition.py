import cv2

# capturing facial features
face_features = cv2.CascadeClassifier("C:/Users/user/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")
#  Turn on the camera 
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    video_col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    face = face_features.detectMultiScale(
        video_col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in face :
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    if ret: cv2.imshow('video_live', video_data)
# # Display the frame
# # Save the frame
    cv2.imwrite('frame.jpg', video_data) 
# # Turning off the camera
    if cv2.waitKey(1) == ord('a'): 
        break 
# Release the camera and close all windows video_cap.release()
    # cv2.destroyAllWindows()