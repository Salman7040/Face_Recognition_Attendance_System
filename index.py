import face_recognition
import os, glob
from os import listdir
import cv2
import numpy as np
from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox

# TODO:Databases Connection
host = "localhost"
user = "root"
password = "root1234"
database = "mydb1"

try:
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    # if connection.is_connected():
    #     print("mysql connected")
except Exception as e:
    print(e)

cursor = connection.cursor()


def comp(fc_en, fr_en):
    for i in fr_en:
        res = face_recognition.compare_faces(fc_en, fr_en)
        return res


# Tkinter Design
def main():
    # TODO:Adding Folder Image to real_myimg within counting a number of image have
    ctr_img_len = 0
    real_myimg = []
    img_name = []
    folder_dir = "my_image"
    for images in os.listdir(folder_dir):
        img_name.append(images.split("."))
        real_myimg.append(face_recognition.load_image_file(folder_dir + "/" + images))
        ctr_img_len += 1

    # TODO:Encoding face to Real_myimg or store in face_enco list
    face_enco = []
    for img in range(0, ctr_img_len):
        real_img_fac_loc = face_recognition.face_locations(real_myimg[img])
        encodings = face_recognition.face_encodings(real_myimg[img], real_img_fac_loc)
        if encodings:
            face_enco.append(encodings[0])
        else:
            print("image not Found")

    # TODO:comparing face  wich is get by sending while loop encoding img send to captuer video

    def show_att_data():
        show_d = Tk()
        show_d.geometry("640x480")
        Label(show_d, text="Student Name").grid(row=0, column=1)
        Label(show_d, text="Att time").grid(row=0, column=2)
        Label(show_d, text="Att Date").grid(row=0, column=3)
        sql_query = "SELECT * FROM att"
        try:
            cursor.execute(sql_query)
            results = cursor.fetchall()
        except Exception as e:
            print(e)
        nextmv = 1
        for row in results:
            Label(show_d, text=row[0]).grid(row=nextmv, column=1)
            Label(show_d, text=row[1]).grid(row=nextmv, column=2)
            Label(show_d, text=row[2]).grid(row=nextmv, column=3)
            nextmv += 1

    def save1(name, frame):
        cv2.imwrite(f"my_image\{name}.jpg", frame)

    def register_page():
        reg = Tk()
        width = reg.winfo_screenwidth()
        height = reg.winfo_screenheight()
        reg.geometry(f"{width}x{height}")
        reg.configure(bg="#f7da8f")
        reg.title("Register Your Face Here...")
        img_name = StringVar(reg)

        def op_camera():
            if img_name.get() == "":
                messagebox.showerror(
                    "Text Box Empty", "First Fill The Name Of Student "
                )
                register_page()
            else:
                cap = cv2.VideoCapture(0)
                while True:
                    # cap.open(address)
                    _, frame = cap.read()
                    cv2.imshow("Press 'Q' To Capture Image", frame)
                    frame = cv2.resize(frame, (640, 480))
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        name = img_name.get()
                        save1(name, frame)
                        cv2.destroyAllWindows()
                        cap.release()
                        break

        Label(
            reg,
            text="Register Your Face Here",
            font=("Helvetica", 50, "bold"),
            borderwidth=5,
            relief=RIDGE,
            bg="#dfcbf2",
        ).pack(fill=X)

        Label(
            reg,
            text="First Enter The Name Of Student :",
            font=("Varela Round", 20),
            bg="#f7da8f",
        ).place(x=60, y=150)

        txt = Entry(
            reg,
            textvariable=img_name,
            font=("Varela Round", 20),
            bg="#f7da8f",
            relief=SUNKEN,
            borderwidth=5,
        ).place(x=500, y=150)

        call = Button(
            reg,
            text="Open Camera",
            command=op_camera,
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).place(x=60, y=250)

        Button(
            reg,
            text="Go To Home Page",
            command=main,
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).place(x=500, y=250)

    def attandence_page():
        att = Tk()
        width = att.winfo_screenwidth()
        height = att.winfo_screenheight()
        att.geometry(f"{width}x{height}")
        att.configure(bg="#f7da8f")
        # TODO:face feature get from cv2 official
        face_cap = cv2.CascadeClassifier(
            "C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
        )
        insert_query = (
            "INSERT INTO att (std_name,att_time,att_date) VALUES (%s, %s, %s)"
        )
        global img_len
        img_len = ctr_img_len
        def start():
            global img_len
            inc=0   
            wait = 20
            che = 1                     
            time = datetime.now()
            cap = cv2.VideoCapture(0)
            add = "http://192.168.0.100:8080/video"
            cap.open(add)
            while True:
                _,frame = cap.read()
                frame = cv2.resize(frame, (640, 480))
                col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = face_cap.detectMultiScale(
                    col,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE,
                )

                if che >= wait:
                    print(che)
                    if img_len == 0:
                        cv2.destroyAllWindows()
                        cap.release()
                        Label(
                            att,
                            text="Success Fully Mark The Attandence Of All The Student",
                            borderwidth=5,
                            relief=RAISED,
                            bg="#8b5a94",
                            font=("Calistoga", 30),
                        ).pack()
                        break
                    face_loc = face_recognition.face_locations(frame)
                    if face_loc != []:
                        f1_en = face_recognition.face_encodings(frame, face_loc)
                        try:                       
                            print("repeated val inc =",inc," img_len=",img_len) 
                            res = comp(face_enco[inc], f1_en)

                        except Exception as e:
                            print(e)
                            print("length=", len(face_enco), " inc=", inc)
                            cv2.destroyAllWindows()
                            cap.release()
                            messagebox.showerror(
                                "Image Not Found Exception", "Check Your Image Folder "
                            )
                            break
                    time = datetime.now()
                    if res[0] == True:
                        ondate = time.strftime("%d-%m-%Y")
                        ontime = time.strftime("%H:%M:%S")
                        data_to_insert = (
                            f"{img_name[inc][0]}",
                            f"{ontime}",
                            f"{ondate}",
                        )
                        try:
                            cursor.execute(insert_query, data_to_insert)
                            connection.commit()
                            cv2.putText(
                                frame,
                                "Attandence Marked..",
                                (50, 50),
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (0, 255, 0),
                                3,
                            )
                            for x, y, w, h in face:
                                cv2.rectangle(
                                    frame, (x, y), (x + w, y + h), (0, 255, 0), 2
                                )
                            cv2.putText(
                                frame,
                                img_name[inc][0],
                                (x, y),
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (0, 255, 0),
                                3,
                            )
                        except mysql.connector.Error as err:
                            print(err)
                        img_name.pop(inc)
                        face_enco.pop(inc)
                        inc=0
                        img_len -= 1
                    
                    else:
                        for x, y, w, h in face:
                            cv2.putText(
                                frame,
                                "Face Not Match..?",
                                (50, 50),
                                cv2.FONT_HERSHEY_PLAIN,
                                3,
                                (0, 0, 255),
                                3,
                            )
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    inc += 1 
                    if inc == img_len:
                        inc = 0          

                    cv2.imshow("Attandence Press 'E'  To Exit Frame", frame)
                    if cv2.waitKey(1) & 0xFF == ord("e"):
                        cv2.destroyAllWindows()
                        cap.release()
                        break
                che += 1

        Label(
            att,
            text="Give The Attandence Here....",
            font=("Helvetica", 50, "bold"),
            borderwidth=5,
            relief=RIDGE,
            bg="#dfcbf2",
        ).pack(fill=X)

        call = Button(
            att,
            text="Open Camera",
            command=start,
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).pack(pady=20)

        Button(
            att,
            text="View Attandence Data",
            command=show_att_data,
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).pack(pady=20)

        Button(
            att,
            text="Go To Home Page",
            command=main,
            font=("Abril Fatface", 20, "bold"),
            borderwidth=5,
            relief=RAISED,
            bg="gray",
            fg="white",
            width=20,
        ).pack(pady=20)

    # TODO:mian page code and design
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")
    root.configure(bg="#f7da8f")
    root.title("This Is Your Home Page")

    Label(
        root,
        text="This Is Your Home Page ",
        font=("Helvetica", 50, "bold"),
        borderwidth=5,
        relief=RIDGE,
        bg="#dfcbf2",
    ).pack(fill=X)

    next = Button(
        root,
        text="Rigister Page",
        command=register_page,
        font=("Abril  Fatface", 20, "bold"),
        borderwidth=5,
        relief=RAISED,
        bg="gray",
        fg="white",
        width=20,
    ).pack(pady=20)

    next = Button(
        root,
        text="Attandence Page",
        command=attandence_page,
        font=("Abril Fatface", 20, "bold"),
        borderwidth=5,
        relief=RAISED,
        bg="gray",
        fg="white",
        width=20,
    ).pack(pady=20)

    root.mainloop()


main()
cursor.close()
connection.close()
