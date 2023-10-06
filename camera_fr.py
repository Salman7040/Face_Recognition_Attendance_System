import cv2

cap=cv2.VideoCapture(0)

# fr=cv2.imread("frame4.jpg",-1)
# fr=cv2.resize(fr,(800,800))

line_inc=0
co=480
th=1
while True:
    _,frame=cap.read()
    # frame[30:30+480,30:30+640]=frame
    
    
    cv2.line(frame,(0,line_inc),(640,line_inc),(0,255,0),2)
    
    if line_inc==0:
        co=480
    if co>=line_inc:
        line_inc+=10
    elif line_inc>co:
        line_inc-=10
        co=0    
    cv2.imshow("webcam",frame)
    # cv2.imshow("frame",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

