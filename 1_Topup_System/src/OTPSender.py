import tkinter as tk
from tkinter import messagebox, simpledialog
from email.mime.text import MIMEText
import smtplib
import random


class OTPSenderApp:
    def __init__(self, master, recipient_email=None, callback=None):
        self.master = master
        master.title("OTP สำหรับแลก Point")
        self.recipient_email = recipient_email  # Store recipient email
        self.callback = callback  # Callback function to handle OTP verification

        self.label = tk.Label(master, text="Recipient's email:")
        self.label.pack()

        self.email_label = tk.Label(master, text=recipient_email)
        self.email_label.pack()

        self.send_button = tk.Button(master, text="Send OTP", command=self.send_otp)
        self.send_button.pack()

        self.center_window()

    def center_window(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f"+{x}+{y}")

    def send_otp(self):
        sender_email = "shopkuexchange@gmail.com"
        recipient_email = self.recipient_email
        app_password = (
            "vxfi aaob bccv fpqu"  # Use the app password generated for your script
        )

        if not recipient_email:
            messagebox.showwarning("Warning", "Please enter your email address.")
            return

        otp = str(random.randint(100000, 999999))
        subject = "OTP สำหรับแลก Point"
        body = f"Your OTP for point exchange is: {otp}"
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient_email

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            server.quit()
            messagebox.showinfo("Success", "Email sent successfully!")

            user_input = simpledialog.askstring(
                "OTP Confirmation", "Enter the OTP received:"
            )
            if user_input == otp:
                if self.callback:
                    self.callback(
                        True
                    )  # Call the callback function with OTP verification status
            else:
                if self.callback:
                    self.callback(
                        False
                    )  # Call the callback function with OTP verification status

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
