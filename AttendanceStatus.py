from tkinter import *
import mysql.connector
from tkinter import messagebox
import os, glob
from os import listdir

def showingAttendanceStatus():
    host = "localhost"
    user = "root"
    password = "root1234"
    database = "mydb1"

    try:
        connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
    except Exception as e:
        print(e)

    cursor = connection.cursor()

    img_name = []
    folder_dir = "./my_image"
    for images in os.listdir(folder_dir):
        img_name.append(images.split(".")[:1])


    sql_query = "SELECT * FROM att "
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
# TODO:cheking from database student present or not
    def presentOrNot(show):
        sql_query = f"SELECT * FROM att where std_name='{show}'"
        try:
            cursor.execute(sql_query)
            haveOrNot= cursor.fetchall()
        except Exception as e:
            print(e)
        if haveOrNot==[]:
            return False
        else:
            return True

    show_d = Tk()
    show_d.geometry("817x490")
    show_d.configure(bg="#f7da8f")
    show_d.title("View The Attendance Data")

    # TODO:For printing status witch is student present or not
    def statusPrint(rowMove,status,color):
         Label(
                frame,
                text=status,
                borderwidth=2,
                relief="solid",
                font=("Varela Round", 20),
                bg="#b8fab6",
                width=6,
                foreground=color
            ).grid(row=rowMove, column=2, pady=2,padx=5)

    canvas = Canvas(show_d,width=754,height=480,background="#f7da8f")
    canvas.grid(row=0, column=0,padx=20, sticky="NSEW")

    frame = Frame(canvas,background="#f7da8f")
    canvas.create_window((0, 0), window=frame, anchor="s")

    Label(
        frame,
        text="Name Of The Student's",
        borderwidth=5,
        relief="ridge",
        font=("Varela Round", 20),
        bg="yellow",
        width=30
    ).grid(row=0, column=1,padx=5, pady=10)
    Label(
        frame,
        text="Status",
        borderwidth=5,
        relief="ridge",
        font=("Varela Round", 20),
        bg="yellow",
        width=6
    ).grid(row=0, column=2,padx=5, pady=10)



    myString=""
    nextmv = 1
    for res in img_name:
        Label(
                frame,
                text=myString.join(res).strip(),
                borderwidth=2,
                relief="solid",
                font=("Varela Round", 20),
                bg="#b8fab6",
                width=30,
                anchor="w"
            ).grid(row=nextmv, column=1, pady=2,padx=5)

        if presentOrNot(myString.join(res))==False :
            statusPrint(nextmv,"A","red")
        else:
            statusPrint(nextmv,"P","#078703")
        nextmv += 1



    scrollbar = Scrollbar(show_d, orient="vertical", command=canvas.yview,width=20)
    scrollbar.grid(row=0, column=5, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


    show_d.mainloop()



# showingAttendanceStatus()






