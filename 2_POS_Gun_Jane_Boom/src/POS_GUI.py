import sys
import os
import datetime

sys.path.append("..\\..\\Public\\")
import JSON_Function as j
from FTPClient import FTPClient
from Jane import POSSystem

from tkinter import *
from tkinter import messagebox
import random
import time

# เชื่อมต่อ FTP Server และ load nisit.json
fileName = "nisit.json"
ftp_client = FTPClient("127.0.0.1", user="admin", passwd="")


def load_json():
    ftp_client.download_file(fileName)
    all_nisit_data = j.load_data(fileName)
    return all_nisit_data

def update_json_and_send_to_ftp(uid, jsonData, money, point):
    if uid in jsonData:
        jsonData[uid]["money"] = money
        jsonData[uid]["points"] = point
        j.update_data("nisit.json", jsonData)
        ftp_client.upload_file(fileName)
        os.remove(fileName)
    
def update_time():
    current_time = time.asctime(time.localtime(time.time()))
    time_label.config(text=current_time)
    root.after(1000, update_time)

def validate_money_input(input_str):
    if input_str.isdigit():
        return True
    elif input_str == "" or input_str == "-":  # Allow empty string or minus sign for negative numbers
        return True
    else:
        return False
    
    
#user global variable
uid = None
data = None
money = 0
points = 0
is_verify = False
nisit_code = ""
fname = ""
lname = ""


# Tkinter GUI
root = Tk()
validate_money = root.register(validate_money_input)
root.geometry("1500x750+10+10")
root.title("ซุ้ม KU คณะวิศวกรรมศาสตร์ ศรีราชา")

Tops = Frame(root, width=1500, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

receipt_frame = Frame(f2, padx=20, pady=20)
receipt_frame.pack(fill=BOTH)

#Header time and verdor name
current_time = time.asctime(time.localtime(time.time()))
header_label = Label(Tops, font=("TH Sarabun New", 50, "bold"), text="ซุ้ม KU คณะวิศวกรรมศาสตร์ ศรีราชา", fg="Blue", bd=10, anchor="w")
header_label.grid(row=0, column=0)

time_label = Label(Tops, font=("TH Sarabun New", 20, "bold"), text=current_time, fg="Blue", bd=10, anchor="w")
time_label.grid(row=1, column=0)
update_time()

# Card UID Display
card_uid_var = StringVar()
card_uid_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text="Card UID:", fg="black", bd=10, anchor="w")
card_uid_label.grid(row=0, column=0)
card_uid_display = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=card_uid_var, bd=10, insertwidth=4, bg="powder blue", justify="right", state='readonly')
card_uid_display.grid(row=0, column=1)

# Money Input
money_var = StringVar()
money_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text="Enter Money:", fg="black", bd=10, anchor="w")
money_label.grid(row=1, column=0)
money_entry = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=money_var, bd=10, insertwidth=4, bg="powder blue",justify="right", validate="key", validatecommand=(validate_money, "%P"))
money_entry.grid(row=1, column=1)

# Customer Display
customer_display_var = StringVar()
customer_display_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text="Customer Display:", fg="black", bd=10, anchor="w")
customer_display_label.grid(row=2, column=0)
customer_display = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=customer_display_var, bd=10, insertwidth=4, bg="powder blue", justify="right", state='readonly')
customer_display.grid(row=2, column=1)

# Customer Points Display
customer_points_text = "Customer Points:"
customer_points_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text=customer_points_text, fg="black", bd=10, anchor="w")
customer_points_label.grid(row=3, column=0)

customer_points_var = StringVar()
customer_points_entry = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=customer_points_var, bd=10, insertwidth=4, bg="powder blue", justify="right", state='readonly')
customer_points_entry.grid(row=3, column=1)

#receipt display
receipt_text = Text(receipt_frame, font=("TH Sarabun New", 20, "bold"), bd=10, insertwidth=4, bg="powder blue", state="disabled")
receipt_text.pack(fill=BOTH, expand=True)

#pos system instance
pos_system = POSSystem()

# Read UID button
def readCard():
    global money, points, uid, data, nisit_code, fname, lname
    data = load_json()
    
    uid = pos_system.read_uid()
    print('uid is: ' + str(uid))

    if uid in data:
        card_data = data[uid]
        money = card_data["money"]
        points = card_data["points"]
        is_verify = card_data["isVerify"]
        nisit_code = card_data["nisit_code"]
        fname = card_data["fname"]
        lname = card_data["lname"]
        if is_verify: 
            card_uid_var.set(uid)
            customer_display_var.set("Money: " + str(money))
            customer_points_var.set("Points: " + str(points))
        else:
            card_uid_var.set('this email is not verify')
    else:
        customer_display_var.set('')
        card_uid_var.set('uid not found')

read_card_button = Button(f1, padx=50, pady=8, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"), text="Read Card", bg="powder blue", command=readCard)
read_card_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='w')

fileName3 = "pos_logs.json"
def update_pos_logs(uid, timestamp, message):
    ftp_client.download_file(fileName3)
    logs = j.load_data(fileName3)
    if uid in logs:
        logs[uid].append({"timestamp": timestamp, "message": message})
    else:
        logs[uid] = [{"timestamp": timestamp, "message": message}]
    j.update_data(fileName3, logs)
    ftp_client.upload_file(fileName3)
    os.remove(fileName3)


# process payment
def processPayment():
    global money, points, uid, data, nisit_code, fname, lname
    
    receipt_text.config(state='normal')
    receipt_text.delete('1.0', END)  # Clear previous content
    money_to_pay = int(money_var.get())
    
    if money_to_pay > 0 and money >= money_to_pay:
        money -= money_to_pay
        customer_display_var.set("Money: " + str(money))  # Convert money to string for display
        points += pos_system.calculate_points(money_to_pay)
        customer_points_var.set("Points: " + str(points))
        
        update_json_and_send_to_ftp(uid, data, money, points)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        receipt = pos_system.generate_receipt(uid, money_to_pay, nisit_code, fname, lname, timestamp)
        update_pos_logs(uid, timestamp, "uid " + str(uid) + " nisit_code " + str(nisit_code) + " name " + fname + " " + lname + " have paid " + str(money_to_pay))
        receipt_text.insert(END, receipt)
    else:
        customer_display_var.set("Not enough money") 
    receipt_text.config(state='disabled') 


payment_button_config = {
    'padx': 50,
    'pady': 8,
    'bd': 8,
    'fg': 'black',
    'font': ('TH Sarabun New', 20, 'bold'),
    'text': 'Process Payment',
    'bg': 'powder blue',
    'command': processPayment
}
payment_button = Button(f1, **payment_button_config)
payment_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='w')


root.mainloop()
