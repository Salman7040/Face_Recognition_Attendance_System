import math
import smtplib
import random

my_mail = "jaj22884@gmail.com"
passcode = "uunq gwyo oeep pheu"
x=random.random()


def mailSendToStudent(toSend):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls() # transfer layer security
    connection.login(user=my_mail, password=passcode)
    mail_content = f"Subject: Email Verificattion  \n\n Code : {math.trunc(x*1000000)} "
    try:
        connection.sendmail(from_addr=my_mail, to_addrs=toSend, msg=mail_content)
    except Exception as e:
        print(e)
    connection.close()
    return math.trunc(x*1000000)


