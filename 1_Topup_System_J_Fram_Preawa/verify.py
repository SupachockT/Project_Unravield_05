from tkinter import *
import smtplib
from ftplib import FTP


def update_receiver_and_send_email():
    try:
        input_file = open("SentEmailToUser.txt", "r")
        lines = input_file.readlines()
        input_file.close()
        updated_receivers = entry_receiver.get() + "@ku.th"
        updated_line = lines[0].split(";")
        updated_line[-1] = updated_receivers + "\n"
        lines[0] = ";".join(updated_line)
        input_file = open("SentEmailToUser.txt", "w")
        input_file.writelines(lines)
        input_file.close()
        print("File write successful")
    except Exception as e:
        print("Error writing to file:", str(e))
        return

    try:
        account, password, receivers = lines[0].strip().split(";")
        print("Read successful")

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            print("Connect successful")
            try:
                server.login(account, password)
                msg = "Subject: Verify Identity\n\n" + "Please click the following link to verify your identity :\n" + "http://00.00.00.00/"
                server.sendmail(account, receivers, msg)
                print("Send Mail successful")
                #show_confirmation_label()
                #print(receivers)
            except:
                print("Incorrect")
            finally:
                server.quit()
        except:
            print("Not Found")
    except Exception as e:
        print("Data in file:", str(e))

def show_confirmation_label():
    confirmation_label = Label(root, text="Hi")
    confirmation_label.pack(pady=10)
    

root = Tk()
root.geometry("300x200")
root.title("Email Verification")

label_receiver = Label(root, text="enter your username :")
label_receiver.pack()

entry_receiver = Entry(root, width=30)
entry_receiver.pack()

btn_click = Button(root, text="Click", command=update_receiver_and_send_email)
btn_click.pack(pady=10)

ftp = FTP('00.00.00.00') # IP server
ftp.login(user='Fam', passwd='Fam')
#ftp.retrlines('LIST')

root.mainloop()



