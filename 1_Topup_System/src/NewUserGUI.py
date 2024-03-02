import sys
import urllib.parse

sys.path.append("..\\..\\Public\\")

from tkinter import *

import JSON_Function as j
from SMTPClient import SMTPClient


def update_receiver_and_send_email(entry_receiver, uid, all_nisit_data, ftp_client):
    try:
        config_data = j.load_data("SMTP_Setting.json")

        sender_email = config_data.get("sender_email")
        password = config_data.get("password")

        # เติม ku.th ตามหลัง
        receiver_email = entry_receiver.get() + "@ku.th"
        new_uid_data = {
            "email": receiver_email,
            "isVerify": False,
            "money": 0,
            "points": 0,
        }
        all_nisit_data[uid] = new_uid_data
        # อัพเดทข้อมูลกลับลงไปใน json file
        j.update_data("nisit.json", all_nisit_data)
        ftp_client.upload_file("nisit.json")

        smtp_client = SMTPClient(
            smtp_server="smtp.gmail.com",
            port=587,
            username=sender_email,
            password=password,
        )
        smtp_client.connect()
        # เตรียมรายละเอียด
        sender = sender_email
        recipients = receiver_email
        subject = "Verify Identity"
        encoded_uid = urllib.parse.quote(uid)
        body = (
            "Please click the following link to verify your identity:\n"
            + f"http://127.0.0.1/?uid={encoded_uid}"
        )
        # ส่ง email
        smtp_client.send_email(sender, recipients, subject, body)
        print("Email sent successfully")
        smtp_client.disconnect()

    except Exception as e:
        print("An error occurred:", str(e))


def NewUser_GUI(uid, all_nisit_data, ftp_client):
    root = Tk()
    root.geometry("300x200")
    root.title("Email Verification")

    label_receiver = Label(root, text="Enter your email address:")
    label_receiver.pack()

    entry_receiver = Entry(root, width=30)
    entry_receiver.pack()

    btn_click = Button(
        root,
        text="Send Verification Email",
        command=lambda: update_receiver_and_send_email(
            entry_receiver, uid, all_nisit_data, ftp_client
        ),
    )
    btn_click.pack(pady=10)

    root.mainloop()
