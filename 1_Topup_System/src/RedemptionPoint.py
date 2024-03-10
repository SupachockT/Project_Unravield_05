import sys
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from OTPSender import OTPSenderApp  # Assuming you have OTPSenderApp class implemented

sys.path.append("..\\..\\Public\\")
from datetime import datetime
from NFC_Reader import NFC_Reader
import FTP_JSON as fj


class ShopUI:
    def __init__(self, master, uid, data):
        self.master = master
        self.uid = uid
        self.total_points = 0
        self.points = data[self.uid]["points"]
        self.items = []
        self.wrong_attempts = 0
        self.email = data[self.uid]["email"]

        self.master.geometry("1500x750+0+0")
        self.master.title("ร้านค้าแลกแต้ม")
        self.create_widgets()

    def create_widgets(self):

        self.top_frame = Frame(
            self.master, width=1500, height=50, bg="powder blue", relief=SUNKEN
        )
        self.top_frame.pack(side=TOP)
        Label(
            self.top_frame,
            font=("TH Sarabun New", 30, "bold"),
            text="ร้านค้าแลกแต้ม",
            fg="Blue",
            bd=10,
            anchor="w",
        ).pack()

        # Left Frame
        self.left_frame = Frame(
            self.master, width=900, height=700, bg="green", relief="raise", padx=350
        )
        self.left_frame.pack(side=LEFT)

        # Right Frame
        self.right_frame = Frame(
            self.master, width=600, height=700, bg="blue", relief="raise"
        )
        self.right_frame.pack(side=RIGHT)

        # Main Options Frame
        self.option_frame = Frame(
            self.right_frame, width=600, height=400, bg="blue", relief="raise"
        )
        self.option_frame.pack(side=TOP)

        # User Info Frame
        self.user_info_frame = Frame(
            self.right_frame, width=600, height=100, bg="blue", relief="raise"
        )
        self.user_info_frame.pack(side=BOTTOM)

        # Load and resize images
        self.images = {}
        for item, path in {
            "pen": "image/pen.jpg",
            "koplao": "image/koplao.jpg",
            "liquid": "image/liquid.jpg",
            "heartbeat": "image/heartbeat.jpg",
            "bag": "image/bag.png",
            "tshirt": "image/tshirt.png",
            "cup": "image/cup.jpg",
            "bear": "image/bear.jpg",
        }.items():
            image = Image.open(path).resize((110, 110), Image.LANCZOS)
            self.images[item] = ImageTk.PhotoImage(image)

        self.create_shop_items()

    def create_shop_items(self):
        for i, (item, points) in enumerate(
            [
                ("pen", 10),
                ("koplao", 50),
                ("liquid", 70),
                ("heartbeat", 90),
                ("bag", 120),
                ("tshirt", 200),
                ("cup", 300),
                ("bear", 400),
            ]
        ):
            item_frame = Frame(self.left_frame, bg="Green")
            item_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            Label(item_frame, image=self.images[item]).grid(row=0, column=0)
            Label(item_frame, font=("TH Sarabun New", 14, "bold"), text=item).grid(
                row=1, column=0
            )
            Label(
                item_frame, font=("TH Sarabun New", 14, "bold"), text=f"{points} แต้ม"
            ).grid(row=2, column=0)
            Button(
                item_frame,
                width=10,
                bd=3,
                fg="black",
                font=("TH Sarabun New", 10, "bold"),
                text="เลือก",
                bg="powder blue",
                command=lambda name=item, pts=points: self.add_points(name, pts),
            ).grid(row=3, column=0)

        self.userUID = StringVar()
        self.userUID.set(f"UID: {self.uid}")
        self.mypoint = StringVar()
        self.mypoint.set(f"My Points: {self.points}")
        self.itempoint = StringVar()
        self.itempoint.set(f"Total Points: {self.total_points}")

        Label(
            self.user_info_frame,
            width=20,
            padx=0,
            pady=0,
            bd=8,
            fg="black",
            font=("TH Sarabun New", 20, "bold"),
            textvariable=self.userUID,
            bg="powder blue",
        ).grid(row=0, column=0, columnspan=2)
        Label(
            self.user_info_frame,
            width=20,
            padx=0,
            pady=0,
            bd=8,
            fg="black",
            font=("TH Sarabun New", 20, "bold"),
            textvariable=self.mypoint,
            bg="powder blue",
        ).grid(row=1, column=0, columnspan=2)
        Label(
            self.user_info_frame,
            width=20,
            padx=0,
            pady=0,
            bd=8,
            fg="Red",
            font=("TH Sarabun New", 20, "bold"),
            textvariable=self.itempoint,
            bg="Yellow",
        ).grid(row=2, column=0, columnspan=2)
        Button(
            self.user_info_frame,
            width=10,
            bd=8,
            fg="black",
            font=("TH Sarabun New", 20, "bold"),
            text="Reset",
            bg="powder blue",
            command=self.btnReset,
        ).grid(row=3, column=0)
        Button(
            self.user_info_frame,
            width=10,
            bd=8,
            fg="black",
            font=("TH Sarabun New", 20, "bold"),
            text="ยืนยันการแลก",
            bg="red",
            command=self.submit_redemption,
        ).grid(row=3, column=1)

    def add_points(self, item_name, points):
        if self.total_points + points <= self.points:
            self.items.append(item_name)
            self.total_points += points
            self.itempoint.set(f"Total Points: {self.total_points}")
        else:
            return

    def submit_redemption(self):
        def handle_otp_verification(otp_verified):
            if otp_verified:
                # Deduct points and update logs
                data = fj.load_return_json()
                data[self.uid]["points"] -= self.total_points
                fj.send_json_back_ftp(data)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                items_str = ", ".join(self.items) if self.items else "No items selected"
                message = f"{self.uid} redeemed {self.total_points} points for items: {items_str}"
                fj.update_redemption_logs(self.uid, timestamp, message)

                # Update GUI
                self.updatePoint(self.total_points)
                self.total_points = 0
                self.items.clear()
                self.itempoint.set(f"Total Points: {0}")
                self.master.destroy()
            else:
                self.wrong_attempts += 1
                if self.wrong_attempts >= 3:
                    messagebox.showwarning(
                        "Warning", "Maximum attempts reached. Closing the application."
                    )
                    self.master.destroy()

        # Prompt for OTP verification
        otp_app_master = tk.Toplevel(self.master)  # Create a new Toplevel window
        otp_app = OTPSenderApp(
            otp_app_master, recipient_email=self.email, callback=handle_otp_verification
        )
        otp_app_master.lift()

    def btnReset(self):
        self.total_points = 0
        self.items.clear()
        self.itempoint.set(f"Total Points: {0}")

    def updatePoint(self, pointToDel):
        self.points -= pointToDel
        self.mypoint.set(f"My Points: {self.points}")
