import sys
import tkinter as tk

sys.path.append("..\\..\\Public\\")


def get_data_by_uid(data, uid):
    if uid in data:
        return data[uid]
    else:
        return None


def Open_TopUp(nisitData, uid):
    root = tk.Tk()
    root.geometry("300x300")
    root.title("TopUp")

    label = tk.Label(root, text="WelCome to TopUp System!")
    label.pack()

    found_data = get_data_by_uid(nisitData, uid)
    label1 = tk.Label(root, text=f"Your email are {found_data["email"]}")
    label1.pack()
    
    label2 = tk.Label(root, text=f"Your money is {found_data["money"]}")
    label2.pack()
    
    root.mainloop()
