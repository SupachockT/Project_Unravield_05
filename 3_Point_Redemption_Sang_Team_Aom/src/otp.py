import smtplib
from email.mime.text import MIMEText
import random

# Replace with your email credentials and recipient's email address
sender_email = "shopkuexchange@gmail.com"
recipient_email = "sangkungbibi@gmail.com"
app_password = "vxfi aaob bccv fpqu"  # Use the app password generated for your script

# Generate a random 6-digit OTP
otp = str(random.randint(100000, 999999))

# Compose the email message
subject = "OTP สำหรับแลก Point"
body = f"Your OTP for point exchange is: {otp}"
message = MIMEText(body)
message["Subject"] = subject
message["From"] = sender_email
message["To"] = recipient_email

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()
    print("Email sent successfully!")

    # เพิ่มส่วนตรวจสอบ OTP ที่ถูกต้อง
    user_input = input("Enter the OTP received: ")
    if user_input == otp:
        print("OTP is correct. Points exchanged!")
        # ทำการแลกแต้มต่อไปได้ที่นี่
    else:
        print("Incorrect OTP. Points not exchanged.")

except Exception as e:
    print(f"Error: {e}")
