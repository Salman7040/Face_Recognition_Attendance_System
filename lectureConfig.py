from tkinter import *
import mysql.connector

# TODO:Databases Connection
host = "localhost"
user = "root"
password = "root1234"
database = "mydb1"

try:
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    if connection.is_connected():
        print("mysql connected")
except Exception as e:
    print(e)

cursor = connection.cursor()
insert_query ="INSERT INTO TeacherManagement (teacherName) VALUES (%s)"



data_to_insert = ("salan")
try:
    cursor.execute(insert_query, data_to_insert)
    connection.commit()

except mysql.connector.Error as err:
                                print(err)
# sql_query = ("INSERT INTO TeacherManagement (teacherName) VALUES (%s)")
#
#
# data_to_insert = ("salman")
# cursor.execute(sql_query, data_to_insert)
# try:
#     cursor.execute(sql_query, data_to_insert)
#     db_connection.commit()
#     print("Data inserted successfully")
#
# except mysql.connector.Error as error:
#     # Rolling back in case of any error
#     db_connection.rollback()
#     print("Error inserting data:", error)
#
#
# cursor.close()
# connection.close()




#
#
# root = Tk()
# root.geometry("640x480")
#
#
# text_array = []
# entry_boxes = []
#
# def recName(name):
#     print(name)
# def add_entry_box():
#     entry = Entry(root)
#     entry.pack(pady=5)
#     entry_boxes.append(entry)
#
#
# button_dict = {}
# def print_text():
#
#     for entry in entry_boxes:
#         text_array.append(entry.get())
#     for name in text_array:
#         TeacherNameAdding(name)
#
#     text_array.clear()
#
# def mkEntry():
#     for i in range(0,int(entry.get())):
#         add_entry_box()
#     Button(root, text="Save", command=print_text).pack(pady=5)
#
#
#
#
#
# entry =Entry(root)
# entry.pack(pady=10)
# button = Button(root, text="Send", command=mkEntry)
# button.pack(pady=5)
#
#
#
# root.mainloop()
#
#
#
