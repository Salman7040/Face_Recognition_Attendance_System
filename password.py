from tkinter import *
import mysql.connector
from tkinter import messagebox

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








root=Tk()
root.geometry("300x300")



def get_pass(set_pass):
    del_query="DELETE FROM sec_pass "
    cursor.execute(del_query)
    connection.commit()

    insert_query = "INSERT INTO sec_pass(user_pass) VALUES (%s)"
    data_to_insert = (set_pass,)
    try:
        cursor.execute(insert_query,data_to_insert)
        connection.commit()
        print("data was submited")
    except mysql.connector.Error as err:
        print(err)


def forgot():
    forg=Tk()
    forgot=StringVar(forg)
    forg.geometry("300x300")
    forg.title("Re Bulid Your Password")
    Label(forg,text="Enter Password New:").grid(row=1,column=1)
    Entry(forg,textvariable=forgot).grid(row=1,column=2)
    Button(forg,text="submit",command=lambda:get_pass(forgot.get())).grid(row=2,column=2)


def rem_data():
    rem_data=Tk()
    rem_data.geometry("400x400")
    Label(rem_data,text="delete your ms data")


def cheking_pass(pass_cheking):
    select="select * from sec_pass"
    cursor.execute(select)
    res= cursor.fetchall()
    for ch in res:
        if pass_cheking==ch[0]:
            rem_data()
        else:
            messagebox.showerror("Paasword Not Match Exception", "Your PassWord Is Incorrect Try Again..?")
            cheking_pass()
                                
                            


    
    
def password():
    
    pa=Tk()
    chek_pass=StringVar(pa)
    pa.geometry("640x480")
    Label(pa,text="Enter Password:").grid(row=1,column=1)
    Entry(pa,textvariable=chek_pass).grid(row=1,column=2)
    Button(pa,text="Frogot",command=forgot).grid(row=2,column=1)
    Button(pa,text="Enter",command=lambda:cheking_pass(chek_pass.get())).grid(row=2,column=2)



Button(root,text="Delete Data",command=password).pack()
root.mainloop()

cursor.close()
connection.close()