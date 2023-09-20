import mysql.connector
from tkinter import *


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
sql_query = "select * from att"
cursor.execute(sql_query)
results = cursor.fetchall()
show_d = Tk()


def show_att_data():
    show_d.geometry("640x480")
    Label(show_d, text="Student Name").grid(row=0, column=1)
    Label(show_d, text="Att time").grid(row=0, column=2)
    Label(show_d, text="Att Date").grid(row=0, column=3)
    nextmv = 1
    for row in results:
        Label(show_d, text=row[0]).grid(row=nextmv, column=1)
        Label(show_d, text=row[1]).grid(row=nextmv, column=2)
        Label(show_d, text=row[2]).grid(row=nextmv, column=3)    
        nextmv += 1


Button(
    show_d,
    text="View Attandence Data",
    command=show_att_data,
    font=("Abril Fatface", 20, "bold"),
    borderwidth=5,
    relief=RAISED,
    bg="gray",
    fg="white",
).grid(row=1,column=1)

show_d.mainloop()


cursor.close()
connection.close()
