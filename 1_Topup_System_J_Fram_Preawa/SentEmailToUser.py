'''
import smtplib
import sys

try:
    input = open("SentEmailToUser.txt")
    print("File open successful")
except:
    print("Error")
    sys.exit()
try:
    account,password,receivers = input.read().split(";")
    print("Read successful")
    input.close()
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        print("Connect successful")
        try:
            server.login(account,password)
            msg = "Verify your identity " + receivers
            server.sendmail(account,receivers,msg)
            print("Send Mail successful")
        except:
            print("Incorrect")
        finally:
            server.quit()
    except:
        print("Not Found")
except:
    print("Data in file")
    sys.exit()

    
    
from tkinter import *
from tkinter import messagebox
import smtplib
import sys

def send_email():
    try:
        input_file = open("SentEmailToUser.txt")
        print("File open successful")
    except:
        print("Error")
        messagebox.showerror("Error", "Could not open file")
        return

    try:
        account, password, receivers = input_file.read().split(";")
        print("Read successful")
        input_file.close()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            print("Connect successful")
            try:
                server.login(account, password)
                msg = "Verify your identity " + receivers
                server.sendmail(account, receivers, msg)
                print("Send Mail successful")
                messagebox.showinfo("Success", "Email sent successfully")
            except:
                print("Incorrect")
                messagebox.showerror("Error", "Incorrect login credentials")
            finally:
                server.quit()
        except:
            print("Not Found")
            messagebox.showerror("Error", "SMTP server not found")
    except:
        print("Data in file")
        messagebox.showerror("Error", "Invalid data in file")
        return

def on_yes_click():
    send_email()

root = Tk()
root.geometry("300x100")
root.title("Email Verification")

btn_yes = Button(root, text="sent Email", command=on_yes_click)
btn_yes.pack(pady=20)

root.mainloop()
'''

from tkinter import *
from ftplib import FTP

def update_file(filename):
    with open(filename, 'a') as file:
        file.write("Hi\n")

ftp = FTP('10.64.150.32')
ftp.login(user='Fam', passwd='Fam')

ftp.retrlines('LIST')

update_file('Users.txt')

def send_email():
    try:
        input_file = open("SentEmailToUser.txt")
        print("File open successful")
    except:
        print("Error")
        return

    try:
        account, password, receivers = input_file.read().split(";")
        print("Read successful")
        input_file.close()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            print("Connect successful")
            try:
                server.login(account, password)
                msg = "Verify your identity " + receivers
                server.sendmail(account, receivers, msg)
                print("Send Mail successful")
                show_confirmation_label()
            except:
                print("Incorrect")
            finally:
                server.quit()
        except:
            print("Not Found")
    except:
        print("Data in file")

def show_confirmation_label():
    confirmation_label = Label(root, text="Hi")
    confirmation_label.pack(pady=10)

root = Tk()
root.geometry("300x150")
root.title("Email Verification")

btn_sent_email = Button(root, text="Sent Email", command=send_email)
btn_sent_email.pack(pady=20)

root.mainloop()



