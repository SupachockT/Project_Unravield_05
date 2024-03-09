import sys
import os

sys.path.append("..\\..\\Public\\")

import JSON_Function as j
from FTPClient import FTPClient
from tkinter import *
from tkinter import messagebox
import random
import time
import json
from NFC_Reader import NFC_Reader
fileName = "nisit.json"
ftp_client = FTPClient("127.0.0.1", user="admin", passwd="")
ftp_client.download_file(fileName)
all_nisit_data = j.load_data(fileName)

root = Tk()
root.geometry("1500x750+10+10")
root.title("ซุ้ม KU คณะวิศวกรรมศาสตร์ ศรีราชา")

Tops = Frame(root, width=1500, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

text_Input = StringVar()
operator = ""


# Money Input
money_var = StringVar()
money_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text="Enter Money:", fg="black", bd=10, anchor="w")
money_label.grid(row=0, column=0)
money_entry = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=money_var, bd=10, insertwidth=4, bg="powder blue",
                    justify="right")
money_entry.grid(row=0, column=1)

# Customer Display
customer_display_var = StringVar()
customer_display_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text="Customer Display:", fg="black", bd=10,
                               anchor="w")
customer_display_label.grid(row=1, column=0)
customer_display = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=customer_display_var, bd=10,
                         insertwidth=4, bg="powder blue", justify="right", state='readonly')
customer_display.grid(row=1, column=1)

# Card UID Display
card_uid_var = StringVar()
card_uid_label = Label(f1, font=("TH Sarabun New", 20, "bold"), text="Card UID:", fg="black", bd=10,
                               anchor="w")
card_uid_label.grid(row=2, column=0)
card_uid_display = Entry(f1, font=("TH Sarabun New", 20, "bold"), textvariable=card_uid_var, bd=10,
                         insertwidth=4, bg="powder blue", justify="right", state='readonly')
card_uid_display.grid(row=2, column=1)

def btnClick(num):
    global operator
    operator += str(num)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set(operator)

def btnEqual():
    global operator
    text_Input.set(str(eval(operator)))
    operator = ""

localtime = time.asctime(time.localtime(time.time()))
_ = Label(Tops, font=("TH Sarabun New", 50, "bold"),
          text="ซุ้ม KU คณะวิศวกรรมศาสตร์ ศรีราชา", fg="Blue", bd=10, anchor="w")
_.grid(row=0, column=0)

_ = Label(Tops, font=("TH Sarabun New", 20, "bold"), text=localtime, fg="Blue", bd=10, anchor="w").grid(row=1, column=0)

# Calculator
_ = Entry(f2, font=("TH Sarabun New", 20, "bold"),
          textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify="right")
_.grid(columnspan=4)

# Row 1
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="+", bg="powder blue", command=lambda: btnClick('+')).grid(row=2, column=3)

# Row 2
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="-", bg="powder blue", command=lambda: btnClick('-')).grid(row=3, column=3)

# Row 3
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="*", bg="powder blue", command=lambda: btnClick('*')).grid(row=4, column=3)

# Row 4
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="C", bg="powder blue", command=lambda: btnClear()).grid(row=5, column=1)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="=", bg="powder blue", command=lambda: btnEqual()).grid(row=5, column=2)
_ = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
           text="/", bg="powder blue", command=lambda: btnClick('/')).grid(row=5, column=3)


uid = " "
# Read Card Button
reader=None

try:
    reader=NFC_Reader()
except:
    uid="no nfc reader connect"
        

def readCard():
    try:
        uid = reader.read_uid()
    except:
        uid = "no nfc reader connect"

    # Simulate card reading
    test="11 22 33 44"
    if test in all_nisit_data:
        info = all_nisit_data[test]
        money_amount = info.get('money', 0)  # Get the money amount from the customer data
        customer_display_var.set(f"Money: {money_amount} THB")
        print("Money:", money_amount)
        print("Points:", info.get('points', 0))
    else:
        customer_display_var.set("Card not found")

read_card_button = Button(f1, padx=50, pady=8, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
                          text="Read Card", bg="powder blue", command=readCard)
read_card_button.grid(row=5, column=2, columnspan=2)

# Payment Button
def processPayment():
    # Add your payment processing logic here
    pass

payment_button = Button(f1, padx=50, pady=8, bd=8, fg="black", font=("TH Sarabun New", 20, "bold"),
                        text="Process Payment", bg="powder blue", command=processPayment)
payment_button.grid(row=5, column=4, columnspan=2)

root.mainloop()
