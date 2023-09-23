from tkinter import *


def main():
    root=Tk()
    root.geometry("640x480")



    ip_con=StringVar(root)
    global change
    change=0


    def confi():
        global change
        if(ip_con.get()==""):
            change=1
        else:
            change=2
    

    if change==1:
        Label(root,text="Entry is empty").pack()
    elif change==2:
        Label(root,text="Entry is not empty").pack()



    Entry(root,textvariable=ip_con).pack()
    Button(root,text="Setting",command=main).pack()

    root.mainloop()

main()