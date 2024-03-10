import sys
import tkinter as tk
from tkinter import messagebox
import datetime
from tkinter import Toplevel

sys.path.append("..\\..\\Public\\")

from NFC_Reader import NFC_Reader
import FTP_JSON as fj
from NewUserGUI import NewUser_GUI, center_window
from RedemptionPoint import ShopUI

uid = None
data = None


def open_top_up():
    new_window = tk.Toplevel(window)
    new_window.title("UID HOME")
    center_window(new_window, 500, 400)

    def create_label(parent, text, bg_color):
        label = tk.Label(parent, text=text, font=("Arial", 12), bg=bg_color)
        label.pack(pady=(10, 5))
        return label

    def create_entry(parent, var=None):
        def validate_input(new_value):
            if new_value == "":
                return True
            try:
                float(new_value)
                return True
            except ValueError:
                return False

        vcmd = parent.register(validate_input)
        entry = tk.Entry(
            parent, textvariable=var, validate="key", validatecommand=(vcmd, "%P")
        )
        entry.pack(pady=(5, 10))
        return entry

    data = fj.load_return_json()
    specific_uid_data = data.get(uid)

    if specific_uid_data:
        label1 = create_label(
            new_window, f"จำนวนเงินของคุณ : {specific_uid_data['money']}", "skyblue"
        )

        label2 = create_label(new_window, "จำนวนเงินที่จะเติม", "skyblue")
        entry2_var = tk.StringVar()
        entry2 = create_entry(new_window, entry2_var)

        submit_button = tk.Button(
            new_window,
            text="เติมเงิน",
            command=lambda: submit_data(entry2_var.get(), new_window),
        )
        submit_button.pack(pady=10)

        restart_button = tk.Button(
            new_window, text="go back", command=new_window.destroy
        )
        restart_button.pack()


def submit_data(money_input, window_to_close):
    messagebox.showinfo("Success", f"เติมเงินสำเร็จ: {money_input}")
    data = fj.load_return_json()

    if uid in data:
        data[uid]["money"] += int(money_input)
        fj.send_json_back_ftp(data)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = uid + " top-up " + money_input + " bath"
        fj.update_topup_logs(uid, timestamp, msg)

    window_to_close.destroy()


def read_uid():
    global uid, data
    reader = NFC_Reader()
    uid = reader.read_uid()
    data = fj.load_return_json()

    is_uid_exist = fj.is_uid_exists(data, uid)
    is_uid_verify = fj.is_uid_verify(data, uid)

    if is_uid_exist:
        entry_var.set(uid)
        if is_uid_verify:
            button2.config(state="normal")
            button3.config(state="disabled")
            button4.config(state="normal")
        else:
            entry_var.set(uid + " is not verify")
    else:
        entry_var.set("uid is not found")
        button2.config(state="disabled")
        button3.config(state="normal")


def open_redemption():
    new_window = Toplevel(window)
    new_window.title("Redemption Point")
    new_window.lift()  # Lift the new Toplevel window to the top
    data = fj.load_return_json()
    shop_ui = ShopUI(new_window, uid, data)


# Create the main window
window = tk.Tk()
window.title("Main Window")
center_window(window, 500, 400)

entry_var = tk.StringVar(value="None")
entry = tk.Entry(window, textvariable=entry_var, state="readonly", width=30)
entry.pack(pady=(50, 10))

button1 = tk.Button(window, text="READ UID", command=read_uid)
button1.pack(pady=(10, 5))

button2 = tk.Button(
    window, text="TopUp", command=open_top_up, state="disabled"
)  # Initially disabled
button2.pack(pady=5)

button3 = tk.Button(
    window,
    text="REGISTER",
    command=lambda: NewUser_GUI(uid, data, fj.ftp_client),
    state="disabled",  # Initially disabled
)
button3.pack(pady=5)

button4 = tk.Button(
    window, text="redemption point", command=open_redemption, state="disabled"
)
button4.pack(pady=5)

window.mainloop()
