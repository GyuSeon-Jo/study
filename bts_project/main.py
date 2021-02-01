import cv2
import numpy as np

video_path = 'video/bts_video.mp4'
cap = cv2.VideoCapture(video_path)

def setOutput(width, height):
    output_size = (width, height)
    return output_size

def writeVideo(output_size):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter('%s_output.mp4' % (video_path.split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), output_size)
    return out

#set size (w, h)
#output_size = (375, 667)
#output_size = (185, 333)

#write video initialize
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('result/%s_output.mp4'%(video_path.split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), output_size)

if not cap.isOpened():
    exit()

tracker = cv2.TrackerCSRT_create()

ret, img = cap.read()

cv2.namedWindow('Selected Window')
cv2.imshow('Selected Window', img)

#ROI
rect = cv2.selectROI('Selected Window', img, fromCenter=False, showCrosshair=True)
cv2.destroyWindow('Selected Window')

#initialize ROI
tracker.init(img, rect)

while True:
    ret, img = cap.read()

    #if not ret:
    #    exit()

    success, box = tracker.update(img)
    l, r, w, h = [int(v) for v in box]

    center_x = l + w / 2
    center_y = r + h / 2


    #calculate result box's size
    res_t = int(center_y - output_size[1] / 2)
    res_b = int(center_y + output_size[1] / 2)
    res_l = int(center_x - output_size[0] / 2)
    res_r = int(center_x + output_size[0] / 2)

    res_img = img[res_t:res_b, res_l:res_r]#.copy()
    #out.write(res_img)

    cv2.rectangle(img, pt1=(l, r), pt2=(l+w, r+h), color=(255, 255, 255), thickness=3)


    cv2.imshow('res_img', res_img)
    cv2.imshow('img', img)
    if cv2.waitKey(60) == ord('q'):
        break