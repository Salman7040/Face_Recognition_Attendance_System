import face_recognition
import cv2


cap=cv2.VideoCapture(0)
# add = "http://192.168.0.100:8080/video"
# cap.open(add)
def loc(fr):
    
    return face_loc

while(True):
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    face_loc=face_recognition.face_locations(frame)
    
    for x,y,w,h in face_loc:
        cv2.rectangle(frame,(x,y),(h,w),(0,0,255),2)   
        cv2.imshow("vido",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break