from tkinter import *
import mysql.connector
from tkinter import messagebox
import smtplib
from os import listdir
from  mailSend import  mailSendToStudent

root = Tk()
root.geometry("700x250")

def get_data():
    if(entry.get()==""):
         messagebox.showerror("Text Box Empty Exception","Keep Fill The Student Email Id In Text Box..")
    else:
        messagebox.showinfo("Email Sended",f"OTP SuccessFully Sended To Your Email Id: {mailSendToStudent(entry.get())}")



Label(
        root,
        text=" Enter The Student Email : ",
        borderwidth=5,
        relief="ridge",
        font=("Varela Round", 20),
        bg="#82817e",
        foreground="white",
        width=23
    ).grid(row=1, column=1,padx=5, pady=10)

entry = Entry(root, width= 25,font=("Ubuntu",20))
entry.grid(row=2, column=1,padx=5, pady=10)



Button(root, text= "Verify Email", command= get_data,font=("Arial",14)).grid(row=2, column=2,padx=5, pady=10)

root.mainloop()
