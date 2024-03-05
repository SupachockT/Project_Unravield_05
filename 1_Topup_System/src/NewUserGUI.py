import sys
import urllib.parse
from tkinter import Tk, Label, Entry, Button, StringVar

sys.path.append("..\\..\\Public\\")

import JSON_Function as j
from SMTPClient import SMTPClient

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

def update_receiver_and_send_email(entry_receiver, uid, all_nisit_data, ftp_client, email_status_var):
    try:
        config_data = j.load_data("SMTP_Setting.json")
        sender_email = config_data.get("sender_email")
        password = config_data.get("password")

        # Append "@ku.th" to the entered email address
        receiver_email = entry_receiver.get()
        new_uid_data = {
            "email": receiver_email,
            "isVerify": False,
            "money": 0,
            "points": 0,
        }

        smtp_client = SMTPClient(
            smtp_server="smtp.gmail.com",
            port=587,
            username=sender_email,
            password=password,
        )
        smtp_client.connect()

        # Prepare email details
        sender = sender_email
        receiver = receiver_email
        subject = "Verify Identity"
        encoded_uid = urllib.parse.quote(uid)
        body = (
            "Please click the following link to verify your identity:\n"
            + f"http://127.0.0.1/?uid={encoded_uid}"
        )
        
        try:
            smtp_client.send_email(sender, receiver, subject, body)
            print("Email sent successfully")
            email_status_var.set("Email sent successfully")
            # Update UID data
            all_nisit_data[uid] = new_uid_data
            # Update data in JSON file
            j.update_data("nisit.json", all_nisit_data)
            ftp_client.upload_file("nisit.json")
        except Exception as e:
            email_status_var.set("Failed to send email, incorrect email")
            print(f"Failed to send email")

        smtp_client.disconnect()

    except Exception as e:
        email_status_var.set("An error occurred: " + str(e))
        print("An error occurred:", str(e))

def NewUser_GUI(uid, all_nisit_data, ftp_client):
    root = Tk()
    root.title("Email Register")
    center_window(root, 300, 150)  # Adjusted window height

    label_receiver = Label(root, text="Enter your email address:")
    label_receiver.pack()

    entry_receiver = Entry(root, width=30)
    entry_receiver.insert(0, "@ku.th") 
    entry_receiver.pack()

    # Status label to show email status
    email_status_var = StringVar()
    status_label = Label(root, textvariable=email_status_var, fg="red")
    status_label.pack()

    btn_click = Button(
        root,
        text="Send Verification Email",
        command=lambda: update_receiver_and_send_email(
            entry_receiver, uid, all_nisit_data, ftp_client, email_status_var
        ),
    )
    btn_click.pack(pady=10)

    root.mainloop()