import face_recognition
import os, glob
from os import listdir
import cv2
import numpy as np
from tkinter import *
import mysql.connector
from datetime import datetime


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
insert_query = "INSERT INTO att (std_name,att_time,att_date) VALUES (%s, %s, %s)"


ctr_img_len = 0
real_myimg = []
img_name = []
folder_dir = "C:/Users/DELL/Desktop/face_recognition_Attandence/my_image"
for images in os.listdir(folder_dir):
    img_name.append(images.split("."))
    print(folder_dir + "/" + images)
    real_myimg.append(face_recognition.load_image_file(folder_dir + "/" + images))
    ctr_img_len += 1


print(ctr_img_len)

# TODO:Encoding face here
face_enco=[]
for img in range(0,ctr_img_len):
    encodings=face_recognition.face_encodings(real_myimg[img])
    if encodings:
        face_enco.append(encodings[0])
    else:
        print("No face encodings found in an image.")





# TODO:compareing face here
def comp(fc_en, fr_en):
    for i in fr_en:
        res = face_recognition.compare_faces(fc_en, fr_en)
        return res


att = Tk()
width = att.winfo_screenwidth()
height = att.winfo_screenheight()
att.geometry(f"{width}x{height}")

face_cap = cv2.CascadeClassifier(
    "C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml"
)


def start():
    wait = 10
    che = 1
    inc = 0
    img_len = ctr_img_len
    cap = cv2.VideoCapture(0)
    time = datetime.now()
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if che >= wait:
            face_loc = face_recognition.face_locations(frame)
            f1_en = face_recognition.face_encodings(frame, face_loc)
            res = comp(face_enco[inc], f1_en)
            time = datetime.now()
            if res != None:
                face = face_cap.detectMultiScale(
                    col,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE,
                )
                if res[0] == True:
                    ondate = time.strftime("%d-%m-%Y")
                    ontime = time.strftime("%H:%M:%S")
                    data_to_insert = (f"{img_name[inc][0]}", f"{ontime}", f"{ondate}")
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
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
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
                    print("not equal", " name ", img_name[inc][0])

                inc += 1
                if inc >= img_len:
                    inc = 0
                cv2.imshow("video", frame)
                if cv2.waitKey(1) & 0xFF == ord("e"):
                    cv2.destroyAllWindows()
                    cap.release()
                    break
        che += 1


# start()

Label(
    att,
    text="Give The Attandence Here....",
    font=("Helvetica", 50, "bold"),
    borderwidth=10,
    relief=RAISED,
    bg="red",
).pack(pady=20)

call = Button(
    att,
    text="Open Camera",
    command=start,
    font=("Abril Fatface", 20, "bold"),
    borderwidth=5,
    relief=RAISED,
    bg="gray",
    fg="white",
).pack(pady=20)
att.mainloop()


cursor.close()
connection.close()
