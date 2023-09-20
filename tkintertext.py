from tkinter import *
from tkinter import messagebox
import cv2


reg=Tk()
var=StringVar()
reg.geometry("640x480")
def show():
    if var.get()=="":
         messagebox.showerror("Text Box Empty", "First Fill The Name Of Student ")
    else:
        cap = cv2.VideoCapture(0)
        while True:
        # cap.open(address)
         _, frame = cap.read()
         cv2.imshow("video", frame)
         frame = cv2.resize(frame, (640, 480))
         if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
                            
                        


Entry(reg,textvariable=var).pack()
Button(reg,text="cllick",command=show).pack()

reg.mainloop()

