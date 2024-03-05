from tkinter import *
from tkinter import messagebox
import random
import time
import json

root = Tk()
root.geometry("1500x750+10+10")
root.title("ซุ้ม KU คณะวิศวกรรมศาสตร์ ศรีราชา")

Tops = Frame(root,width=1500,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

text_Input = StringVar()
operator = ""

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
    
def ExitButton():
    ExitButton = messagebox.askyesno("Quit System!!!", "Do you want to quit?")
    if ExitButton > 0:
        root.destroy()
        return
    
localtime = time.asctime(time.localtime(time.time()))
_ = Label(Tops,font=("TH Sarabun New",50,"bold"),text="ซุ้ม KU คณะวิศวกรรมศาสตร์ ศรีราชา",fg="Blue",bd=10,anchor="w")
_.grid(row=0,column=0)

_ = Label(Tops,font=("TH Sarabun New",20,"bold"),text=localtime,fg="Blue",bd=10,anchor="w").grid(row=1,column=0)

#Calculator
_ = Entry(f2,font=("TH Sarabun New",20,"bold"),
          textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify="right")
_.grid(columnspan=4)

#Row 1
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="+",bg="powder blue",command=lambda:btnClick('+')).grid(row=2,column=3)

#Row 2
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="-",bg="powder blue",command=lambda:btnClick('-')).grid(row=3,column=3)

#Row 3
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=0)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=2)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="*",bg="powder blue",command=lambda:btnClick('*')).grid(row=4,column=3)

#Row 4
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="C",bg="powder blue",command=lambda:btnClear()).grid(row=5,column=1)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="=",bg="powder blue",command=lambda:btnEqual()).grid(row=5,column=2)
_ = Button(f2,padx=16,pady=16,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="/",bg="powder blue",command=lambda:btnClick('/')).grid(row=5,column=3)

_ = Button(f1,padx=50,pady=8,bd=8,fg="black",font=("TH Sarabun New",20,"bold"),
           text="Exit",bg="powder blue",command=lambda:ExitButton()).grid(row=5,column=1)
    

root.mainloop()