import cv2
import time
cv2.namedWindow("dashcam")
video = cv2.VideoCapture(1)
last_save_time = -10
while video.isOpened():
    rval, frame = video.read()
    if not rval:
        break
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    current_time = time.time()
    if current_time - last_save_time > 10:
        last_save_time = current_time
        timestr = time.strftime("%Y_%m_%d__%H_%M_%S")
        out = cv2.VideoWriter(timestr+'.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (frame_width, frame_height))
    cv2.imshow('dashcam', frame)
    out.write(frame)
    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break
video.release()
cv2.destroyAllWindows()
