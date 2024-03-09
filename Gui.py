import tkinter as tk
from tkinter import messagebox

def open_uid_window():
    new_window = tk.Toplevel(window)
    new_window.title("UID HOME")
    new_window.geometry("500x400+750+250")

    # สร้างกล่องข้อความในหน้าต่างใหม่
    entry2 = tk.Entry(new_window)
    entry2.place(x=200, y=110)  # ตำแหน่ง x, y ของ entry2
    label = tk.Label(new_window, text="จำนวนเงินของคุณ : ", font=30, bg="gray").place(x=50, y=50)
    label2 = tk.Label(new_window, text="จำนวนเงินที่จะเติม : ", font=30, bg="skyblue").place(x=50, y=110)

    # สร้างปุ่ม Submit
    submit_button = tk.Button(new_window, text="เติมเงิน", command=submit_data)
    submit_button.place(x=200, y=150)
    restart_button = tk.Button(new_window, text="restart", command=restart_data)
    restart_button.place(x=250, y=150)

def submit_data():
    messagebox.showinfo("success","เติมเงินสำเร็จ")

def restart_data():
    messagebox.showinfo("restart","รีสตาร์ทใหม่")

def open_register_window():
    new_window = tk.Toplevel(window)
    new_window.title("REGISTER")
    new_window.geometry("500x400+750+250")

def show_input():
    input_text = entry.get()
    messagebox.showinfo("Input", f"The input value is: {input_text}")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("Main Window")
window.geometry("500x400+200+250")

# สร้างกล่อง input
entry = tk.Entry(window)
entry.pack()

# สร้างปุ่มเพื่อเปิดหน้าต่างใหม่และแสดงข้อความในกล่องข้อความ
button1 = tk.Button(window, text="READ UID", command=open_uid_window)
button1.pack()

# สร้างปุ่มเพื่อแสดงข้อความที่ป้อนในกล่องอินพุต
button2 = tk.Button(window, text="REGISTER", command=open_register_window)
button2.pack()

# กำหนดตำแหน่งของ entry และปุ่ม
entry.place(x=185, y=50)
button1.place(x=215, y=75)
button2.place(x=215, y=115)

# แสดงหน้าต่างหลัก
window.mainloop()
