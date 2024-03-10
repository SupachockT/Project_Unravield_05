from tkinter import *
from tkinter import messagebox
import random
import time
import json
from PIL import Image, ImageTk
import urllib.request
import io

root = Tk()
root.geometry("1500x750+0+0")
root.title("ร้านค้าแลกแต้ม")

Tops = Frame(root, width=1500, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

fitem = Frame(root, width=900, height=700, bg="green", relief="raise", padx=350)
fitem.pack(side=LEFT)

fmainR = Frame(root, width=600, height=700, bg="blue", relief="raise")
fmainR.pack(side=RIGHT)

foption = Frame(fmainR, width=600, height=300, bg="blue", relief="raise")
foption.pack(side=TOP)


foption2 = Frame(fmainR, width=600, height=300, bg="blue", relief="raise")
foption2.pack(side=BOTTOM)

foption3 = Frame(fmainR, width=600, height=100, bg="blue", relief="raise")
foption3.pack(side=BOTTOM)

userUID = StringVar()
UID = ""
userUID.set(f"UID: {UID}")
point = 0
mypoint = StringVar()
mypoint.set(f"My Points: {point}")
total_points = 0
itempoint = StringVar()
itempoint.set(f"Total Points: {total_points}")

itemPointDict = {
    "pen": 10,
    "pencil": 20,
    "koplao": 50,
    "koplao": 50,
    "liquid": 70,
    "heartbeat": 90,
    "bag": 120,
    "tshirt": 200,
    "cup": 300,
    "bear": 400,
}


def btnReset():
    global total_points
    total_points = 0
    itempoint.set(f"Total Points: {0}")


def add_points(item_name, points):
    global total_points
    total_points += points
    itempoint.set(f"Total Points: {total_points}")


_ = Label(
    Tops,
    font=("TH Sarabun New", 30, "bold"),
    text="ร้านค้าแลกแต้ม",
    fg="Blue",
    bd=10,
    anchor="w",
)
_.grid(row=0, column=0)

# Option 1
_ = Button(
    foption,
    width=10,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    text="Read UID",
    bg="powder blue",
).grid(row=0, column=0)
_ = Button(
    foption,
    width=10,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    text="Email",
    bg="powder blue",
).grid(row=1, column=0)
_ = Button(
    foption,
    width=10,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    text="Send OTP",
    bg="powder blue",
).grid(row=2, column=0)
_ = Button(
    foption,
    width=10,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    text="ปุ่มดึงแต้ม",
    bg="powder blue",
).grid(row=3, column=0)


# Option 2
_ = Label(
    foption2,
    width=20,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    textvariable=userUID,
    bg="powder blue",
).grid(row=0, column=0, columnspan=2)
_ = Label(
    foption2,
    width=20,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    textvariable=mypoint,
    bg="powder blue",
).grid(row=1, column=0, columnspan=2)
_ = Label(
    foption2,
    width=20,
    padx=0,
    pady=0,
    bd=8,
    fg="Red",
    font=("TH Sarabun New", 20, "bold"),
    textvariable=itempoint,
    bg="Yellow",
).grid(row=2, column=0, columnspan=2)
_ = Button(
    foption2,
    width=10,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    text="Reset",
    bg="powder blue",
    command=btnReset,
).grid(row=3, column=0)
_ = Button(
    foption2,
    width=10,
    padx=0,
    pady=0,
    bd=8,
    fg="black",
    font=("TH Sarabun New", 20, "bold"),
    text="ยืนยันการแลก",
    bg="red",
).grid(row=3, column=1)

# โหลดรูปภาพ
image_path = "image/pen.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
penimg = ImageTk.PhotoImage(image)

image_path = "image/pencil.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
pencilimg = ImageTk.PhotoImage(image)

image_path = "image/koplao.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
koplaoimg = ImageTk.PhotoImage(image)

image_path = "image/liquid.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
liquidimg = ImageTk.PhotoImage(image)

image_path = "image/bag.png"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
bagimg = ImageTk.PhotoImage(image)

image_path = "image/tshirt.png"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
tshirtimg = ImageTk.PhotoImage(image)

image_path = "image/heartbeat.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
heartbeatimg = ImageTk.PhotoImage(image)

image_path = "image/cup.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
cupimg = ImageTk.PhotoImage(image)

image_path = "image/bear.jpg"
image = Image.open(image_path)
image = image.resize((110, 110), Image.LANCZOS)
bearimg = ImageTk.PhotoImage(image)


# สร้าง Label แสดงรูปภาพ

_ = Label(fitem, image=pencilimg)
_.grid(row=0, column=0, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="ดินสอ", bg="Green")
_.grid(row=1, column=0)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="10 แต้ม", bg="Green")
_.grid(row=2, column=0)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="pencill", pts=10: add_points(name, pts),
).grid(row=3, column=0)

_ = Label(fitem, image=penimg)
_.grid(row=0, column=1, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="ปากกา", bg="Green")
_.grid(row=1, column=1)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="20 แต้ม", bg="Green")
_.grid(row=2, column=1)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="pen", pts=20: add_points(name, pts),
).grid(row=3, column=1)

_ = Label(fitem, image=koplaoimg)
_.grid(row=0, column=2, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="กบเหลา", bg="Green")
_.grid(row=1, column=2)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="50 แต้ม", bg="Green")
_.grid(row=2, column=2)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="koplao", pts=50: add_points(name, pts),
).grid(row=3, column=2)

_ = Label(fitem, image=liquidimg)
_.grid(row=4, column=0, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="ลิขวิด", bg="Green")
_.grid(row=5, column=0)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="70 แต้ม", bg="Green")
_.grid(row=6, column=0)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="liquid", pts=70: add_points(name, pts),
).grid(row=7, column=0)

_ = Label(fitem, image=heartbeatimg)
_.grid(row=4, column=1, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="ลูกอม", bg="Green")
_.grid(row=5, column=1)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="90 แต้ม", bg="Green")
_.grid(row=6, column=1)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="heartbeat", pts=90: add_points(name, pts),
).grid(row=7, column=1)

_ = Label(fitem, image=bagimg)
_.grid(row=4, column=2, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="กระเป๋าผ้า", bg="Green")
_.grid(row=5, column=2)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="120 แต้ม", bg="Green")
_.grid(row=6, column=2)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="bag", pts=120: add_points(name, pts),
).grid(row=7, column=2)

_ = Label(fitem, image=tshirtimg)
_.grid(row=8, column=0, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="เสื้อ", bg="Green")
_.grid(row=9, column=0)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="200 แต้ม", bg="Green")
_.grid(row=10, column=0)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="tshirt", pts=200: add_points(name, pts),
).grid(row=11, column=0)

_ = Label(fitem, image=cupimg)
_.grid(row=8, column=1, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="แก้วน้ำ", bg="Green")
_.grid(row=9, column=1)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="300 แต้ม", bg="Green")
_.grid(row=10, column=1)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="cup", pts=300: add_points(name, pts),
).grid(row=11, column=1)

_ = Label(fitem, image=bearimg)
_.grid(row=8, column=2, padx=10, pady=10)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="ตุ๊กตาหมี", bg="Green")
_.grid(row=9, column=2)
_ = Label(fitem, font=("TH Sarabun New", 14, "bold"), text="400 แต้ม", bg="Green")
_.grid(row=10, column=2)
_ = Button(
    fitem,
    width=10,
    bd=3,
    fg="black",
    font=("TH Sarabun New", 10, "bold"),
    text="เลือก",
    bg="powder blue",
    command=lambda name="bear", pts=400: add_points(name, pts),
).grid(row=11, column=2)

root.mainloop()
