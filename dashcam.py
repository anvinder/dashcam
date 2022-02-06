import shutil
import cv2
import time
import os
cv2.namedWindow("dashcam")
video = cv2.VideoCapture(1)
last_save_time = -10
now = time.time()
path1 = "C:\\Users\\qwerty\\PycharmProjects\\generic\\dashcam"
os.chdir(path1)
usage = shutil.disk_usage(path1)
free_space = usage[1]

bytes = float(free_space)
kb = bytes / 1024
Mb = kb/(1024*1024)
print("size in Mb = ", Mb)

for filename in os.listdir(path1):
    if os.path.getmtime(os.path.join(path1, filename)) < now - 7*86400:
        if os.path.isfile(os.path.join(path1, filename)):
            print(filename)
            os.remove(os.path.join(path1, filename))

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



