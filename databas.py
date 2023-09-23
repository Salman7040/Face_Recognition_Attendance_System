from tkinter import* 
import mysql.connector



host="localhost"
user="root"
password="root1234"
database="mydb1"

try:
    connection=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    # if connection.is_connected():
    #     print("mysql connected")
except Exception as e:
    print(e)


cursor=connection.cursor()
insert_query = "INSERT INTO sec_pass(user_pass) VALUES (%s)"
data_to_insert = ("yash111",)
try:
    cursor.execute(insert_query,data_to_insert)
    connection.commit()
    print("data was submited")
except mysql.connector.Error as err:
    print(err)


cursor.close()
connection.close()

