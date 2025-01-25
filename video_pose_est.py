import cv2
import mediapipe as mp

#initialize mediapipe pose
mp_pose=mp.solutions.pose
mp_drawing=mp.solutions.drawing_utils

#reading video
video_source=0
# cap=cv2.VideoCapture('.\\videos\\pose_est.mp4')
cap=cv2.VideoCapture(video_source)

#set video resolution for web cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)

with mp_pose.Pose(static_image_mode=False,model_complexity=0,enable_segmentation=False, min_detection_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame=cap.read()
        if not ret:
            print('Video capture ended')
            break
        frame=cv2.flip(frame,1)
        frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #perform pose estimation
        results=pose.process(frame_rgb) 

        #draw landmarks only (no lines)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame,results.pose_landmarks,
                                    mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(0,255,0),thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(0,0,255),thickness=2, circle_radius=2))
        #resize frame to fit the screen
        display_frame=cv2.resize(frame,(480,640))
        cv2.imshow('Pose Estimation',display_frame)

        #Break the loop is q is pressed
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
                

cap.release()
cv2.destroyAllWindows()


