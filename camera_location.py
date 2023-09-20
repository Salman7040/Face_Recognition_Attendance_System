import cv2


cap=cv2.VideoCapture(0)

while True:
    _,fr=cap.read()
    fr=cv2.resize(fr,(640,480))
    cv2.namedWindow("MyWindow", cv2.WINDOW_NORMAL)
    cv2.moveWindow("MyWindow",x=0,y=0)
    cv2.imshow("MyWindow",fr)
    cv2.waitKey(1)
