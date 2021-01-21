import smtplib
import threading




server  =   smtplib.SMTP('smtp.gmail.com',  587)
server.starttls()
server.login('*********', '*********')
def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
def sendMail():
    server.sendmail('***********',
                    '*************',
                    '*******'
                    )
    print('MailSent')
setInterval(sendMail,5)
#you need to give your credentials to run this and allow the LESS SECURE APP feature on your gmail
#on the sendmail function FIRST ADD YOUR GMAIL,THEN THE GMAIL OF THE RECIEVER AND THEN THE MESSAGE
# YOU WANT TO SEND
#remember to stop the program after you have irritated your friend  JUST CLICK ON THE RED BUTTON
#THE PROGRAM
