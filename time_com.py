from tkinter import *
from datetime import datetime



       

def time_set():  
    set_t=Tk()
    set_t.geometry("640x480")
    cu_tm=datetime.now().time()
    cu_tm = cu_tm.strftime("%I:%M:%S")
    hr_set=StringVar(set_t)
    mi_set=StringVar(set_t)
    lec_name=StringVar(set_t)
    Label(set_t,text=f"Current Time :{cu_tm}").pack()
    Label(set_t,text="Enter The Name Of Lecture ").pack()
    Entry(set_t,textvariable=lec_name).pack()
    Label(set_t,text="Enter Hours").pack()
    Entry(set_t,textvariable=hr_set).pack()

    Label(set_t,text="Enter Minuts").pack()
    Entry(set_t,textvariable=mi_set).pack()
    Button(set_t,text="Set Timer",command=lambda:start(hr_set.get(),mi_set.get(),"on",set_t,lec_name.get())).pack()
        

def start(hr_get,mi_get,st,des,lec):
    print(lec)
    if des!="off" :
        des.destroy()
    while True:
        cu_tm=datetime.now().time()
        cu_tm = cu_tm.strftime("%I:%M:%S") 
        if st=="on":
            tm1=f"{hr_get}:{mi_get}:00"
            if cu_tm>=tm1:
                print("equal",cu_tm)
                break
        
               

    

att=Tk()
att.geometry("640x480")

Button(
            att,
            text="Open Camera",
            command=lambda:start("no","no","off","off"),
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).pack(pady=20)

Button(
            att,
            text="Set Attandence Timer",
            command=time_set,
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).pack(pady=20)
att.mainloop()


