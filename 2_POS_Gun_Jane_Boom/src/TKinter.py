from tkinter import *
from tkinter import messagebox
import random
import time
import json

with open('menu_new.json', 'r', encoding='utf-8') as file:
    menu_data = json.load(file)

root = Tk()
root.geometry("1350x750+0+0")
root.title("Engineering at Sriracha Coffee Shop")
root.configure(background='cyan')

Tops = Frame(root,width= 1350,height = 100, bd=14, relief="raise")
Tops.pack(side=TOP)


fMainL = Frame(root,width= 900,height = 650, bd=8, relief="raise")
fMainL.pack(side=LEFT)

fMainR = Frame(root,width= 440,height = 650, bd=8, relief="raise")
fMainR.pack(side=RIGHT)

fMLT = Frame(fMainL,width= 900,height = 320, bd=8, relief="raise")
fMLT.pack(side=TOP)

fMLB = Frame(fMainL,width= 900,height = 320, bd=6, relief="raise")
fMLB.pack(side=BOTTOM)

fReceipt = Frame(fMainR,width= 440,height = 450, bd=12, relief="raise")
fReceipt.pack(side=TOP)
fButton = Frame(fMainR,width= 440,height = 240, bd=12, relief="raise")
fButton.pack(side=BOTTOM)

fDrink = Frame(fMLT,width= 400,height =
                330, bd=16, relief="raise")
fDrink.pack(side=LEFT)
fCake = Frame(fMLT,width= 400,height = 320, bd=16, relief="raise")
fCake.pack(side=RIGHT)

fCost1 = Frame(fMLB,width= 440,height = 330, bd=14, relief="raise")
fCost1.pack(side=LEFT)
fCost2 = Frame(fMLB,width= 440,height = 320, bd=14, relief="raise")
fCost2.pack(side=RIGHT)

Tops.configure(background='pink')
fMainL.configure(background='blue')
fMainR.configure(background='blue')

lblInfo = Label(Tops,font=('TH Sarabun New',60,'bold'),text = "Engineering at Sriracha Coffee Shop",bg="yellow",bd=10)
lblInfo.grid(row=0,column=0)  

#============================= Function =====================
def qExit():
    qExit= messagebox.askyesno("Quit System!!!", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
    
def Reset():
    FrameDrinkReset()
    FrameCakeReset()
    FrameCostReset()
    txtReceipt.delete("1.0",END)

def FrameDrinkReset():
    for x in VarDrinkList:    
        x.set("0")

    for x in EntryDrinkList:    
        x.set("0")

    txtDrink0.configure(state = DISABLED)
    txtDrink1.configure(state = DISABLED)
    txtDrink2.configure(state = DISABLED)
    txtDrink3.configure(state = DISABLED)
    txtDrink4.configure(state = DISABLED)
    txtDrink5.configure(state = DISABLED)
    txtDrink6.configure(state = DISABLED)
    txtDrink7.configure(state = DISABLED)

def FrameCakeReset():
    for x in VarCakeList:    
        x.set("0")

    for x in EntryCakeList:    
        x.set("0")

    txtCake0.configure(state = DISABLED)
    txtCake1.configure(state = DISABLED)
    txtCake2.configure(state = DISABLED)
    txtCake3.configure(state = DISABLED)
    txtCake4.configure(state = DISABLED)
    txtCake5.configure(state = DISABLED)
    txtCake6.configure(state = DISABLED)
    txtCake7.configure(state = DISABLED)
    
def FrameCostReset():
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
                 
def chkbutton_value(chkValue,txtLabel,Entry):
    if chkValue.get() == 1:
        txtLabel.configure(state=NORMAL)
    elif chkValue.get() == 0:
        txtLabel.configure(state=DISABLED)
        Entry.set("0")

CakePriceList = [50,50,50,50,50,50,50,50]
DrinkPriceList = [50,50,50,50,50,50,50,50]

def CostofItem():    

       TotalDrinkCost = 0
       TotalCakeCost = 0
       
       global CakePriceList
       global DrinkPriceList

       for i in range(8) :
             TotalDrinkCost += int(EntryDrinkList[i].get())* float(DrinkPriceList[i])
                                                             
       for i in range(8) :
             TotalCakeCost += int(EntryCakeList[i].get())* float(CakePriceList[i])

       DrinksPrice = "B", str('%.2f'%(TotalDrinkCost))
       CakesPrice = "B", str('%.2f'%(TotalCakeCost))
       CostofDrinks.set(DrinksPrice)
       CostofCakes.set(CakesPrice)
       SC = "B", str('%.2f'%(1.59))
       ServiceCharge.set(SC)

       CostPlus = TotalDrinkCost + TotalCakeCost + 1.59
        
       SubTotalofItems = "B", str('%.2f'%(CostPlus))
       SubTotal.set(SubTotalofItems)

       Tax = "B" , str('%.2f'%(CostPlus*0.07))
       PaidTax.set(Tax)
       TT = CostPlus * 0.07
       TC = "B" , str('%.2f'%(CostPlus + TT))
       TotalCost.set(TC)

def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    ReceiptRef.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + ReceiptRef.get() + '\t\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END, 'Items\t\t\t' + 'Price\t' + 'Qty\t' + 'Total\n\n')

    total_cost = 0

    for i in range(8):
        if VarDrinkList[i].get() == 1:
            price = 50  
            qty = int(EntryDrinkList[i].get())
            total = price * qty
            total_cost += total
            txtReceipt.insert(END, DrinkList[i] + '\t\t\t' + str(price) + '\t' + str(qty) + '\t' + str(total) + '\n')

    for i in range(8):
        if VarCakeList[i].get() == 1:
            price = 50  
            qty = int(EntryCakeList[i].get())
            total = price * qty
            total_cost += total
            txtReceipt.insert(END, CakeList[i] + '\t\t\t' + str(price) + '\t' + str(qty) + '\t' + str(total) + '\n')

    txtReceipt.insert(END, '\nTotal Cost: \t\t\t\t\t\t\t\t' + str(total_cost))

    txtReceipt.insert(END, '\nService Charge: \t\t\t\t1.59')

    tax = (total_cost + 1.59)* 0.07
    txtReceipt.insert(END, '\nPaid Tax (7%): \t\t\t\t' + str('%.2f' % tax))

    total_cost_with_charge_tax = total_cost + 1.59 + tax
    txtReceipt.insert(END, '\nTotal Cost (incl. service charge and tax): \t\t' + str('%.2f' % total_cost_with_charge_tax))

        
#====================== Variable Coffee =====================
ReceiptRef = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))

#====================== Variable Cake =====================
DrinkList = menu_data.get('drinks', [])

VarDrink0 = IntVar()
VarDrink1 = IntVar()
VarDrink2 = IntVar()
VarDrink3 = IntVar()
VarDrink4 = IntVar()
VarDrink5 = IntVar()
VarDrink6 = IntVar()
VarDrink7 = IntVar()

VarDrinkList = [VarDrink0,VarDrink1,VarDrink2,VarDrink3,VarDrink4,VarDrink5,VarDrink6,VarDrink7]

for x in VarDrinkList:    
    x.set("0")

EntryDrink0 = StringVar()
EntryDrink1 = StringVar()
EntryDrink2 = StringVar()
EntryDrink3 = StringVar()
EntryDrink4 = StringVar()
EntryDrink5 = StringVar()
EntryDrink6 = StringVar()
EntryDrink7 = StringVar()

EntryDrinkList = [EntryDrink0,EntryDrink1,EntryDrink2,EntryDrink3,EntryDrink4,EntryDrink5,EntryDrink6,EntryDrink7]

for x in EntryDrinkList:
    x.set("0")

#====================== Variable Cake =====================
CakeList = menu_data.get('cakes', [])

VarCake0 = IntVar()
VarCake1 = IntVar()
VarCake2 = IntVar()
VarCake3 = IntVar()
VarCake4 = IntVar()
VarCake5 = IntVar()
VarCake6 = IntVar()
VarCake7 = IntVar()


VarCakeList = [VarCake0,VarCake1,VarCake2,VarCake3,
               VarCake4,VarCake5,VarCake6,VarCake7]

for x in VarCakeList:    
    x.set("0")

EntryCake0 = StringVar()
EntryCake1 = StringVar()
EntryCake2 = StringVar()
EntryCake3 = StringVar()
EntryCake4 = StringVar()
EntryCake5 = StringVar()
EntryCake6 = StringVar()
EntryCake7 = StringVar()


EntryCakeList = [EntryCake0,EntryCake1,EntryCake2,EntryCake3,
                 EntryCake4,EntryCake5,EntryCake6,EntryCake7]

for x in EntryCakeList:    
    x.set("0")
    
#===============================Variable Calculation =====================
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofDrinks = StringVar()
CostofCakes = StringVar()
ServiceCharge = StringVar()

#==================================== Drink =================================
_ = Checkbutton(fDrink, text=DrinkList[0]+"*"+str(DrinkPriceList[0]),variable = VarDrinkList[0],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[0],txtDrink0,EntryDrinkList[0])).grid(row= 0, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[1]+"*"+str(DrinkPriceList[1]),variable = VarDrinkList[1],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[1],txtDrink1,EntryDrinkList[1])).grid(row= 1, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[2]+"*"+str(DrinkPriceList[2]),variable = VarDrinkList[2],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[2],txtDrink2,EntryDrinkList[2])).grid(row= 2, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[3]+"*"+str(DrinkPriceList[3]),variable = VarDrinkList[3],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[3],txtDrink3,EntryDrinkList[3])).grid(row= 3, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[4]+"*"+str(DrinkPriceList[4]),variable = VarDrinkList[4],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[4],txtDrink4,EntryDrinkList[4])).grid(row= 4, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[5]+"*"+str(DrinkPriceList[5]),variable = VarDrinkList[5],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[5],txtDrink5,EntryDrinkList[5])).grid(row= 5, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[6]+"*"+str(DrinkPriceList[6]),variable = VarDrinkList[6],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[6],txtDrink6,EntryDrinkList[6])).grid(row= 6, sticky=W)
_ = Checkbutton(fDrink, text=DrinkList[7]+"*"+str(DrinkPriceList[7]),variable = VarDrinkList[7],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarDrinkList[7],txtDrink7,EntryDrinkList[7])).grid(row= 7, sticky=W)


#=======================Enter Widgets for Drink=======================
txtDrink0 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[0],state = DISABLED)
txtDrink0.grid(row=0,column =1)
txtDrink1 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[1],state = DISABLED)
txtDrink1.grid(row=1,column =1)
txtDrink2 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[2],state = DISABLED)
txtDrink2.grid(row=2,column =1)
txtDrink3 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[3],state = DISABLED)
txtDrink3.grid(row=3,column =1)
txtDrink4 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[4],state = DISABLED)
txtDrink4.grid(row=4,column =1)
txtDrink5 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[5],state = DISABLED)
txtDrink5.grid(row=5,column =1)
txtDrink6 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[6],state = DISABLED)
txtDrink6.grid(row=6,column =1)
txtDrink7 = Entry(fDrink,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryDrinkList[7],state = DISABLED)
txtDrink7.grid(row=7,column =1)


#====================================== Cake====================================
"""CoffeeCake = Checkbutton(fCake, text="Coffee Cake \t",variable = var9,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold')).grid(row= 0, column=0)"""    
_ = Checkbutton(fCake, text=CakeList[0]+"*"+str(CakePriceList[0]),variable = VarCakeList[0] ,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[0],txtCake0,EntryCakeList[0])).grid(row= 0, sticky=W)

_ = Checkbutton(fCake, text=CakeList[1]+"*"+str(CakePriceList[1]),variable = VarCakeList[1],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[1],txtCake1,EntryCakeList[1])).grid(row= 1, sticky=W)

_ = Checkbutton(fCake, text=CakeList[2]+"*"+str(CakePriceList[2]),variable = VarCakeList[2],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[2],txtCake2,EntryCakeList[2])).grid(row= 2, sticky=W)

_ = Checkbutton(fCake, text=CakeList[3]+"*"+str(CakePriceList[3]),variable = VarCakeList[3],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[3],txtCake3,EntryCakeList[3])).grid(row= 3, sticky=W)

_ = Checkbutton(fCake, text=CakeList[4]+"*"+str(CakePriceList[4]),variable = VarCakeList[4],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[4],txtCake4,EntryCakeList[4])).grid(row= 4, sticky=W)

_ = Checkbutton(fCake, text=CakeList[5]+"*"+str(CakePriceList[5]),variable = VarCakeList[5],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[5],txtCake5,EntryCakeList[5])).grid(row= 5, sticky=W)

_ = Checkbutton(fCake, text=CakeList[6]+"*"+str(CakePriceList[6]),variable = VarCakeList[6],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[6],txtCake6,EntryCakeList[6])).grid(row= 6, sticky=W)

_ = Checkbutton(fCake, text=CakeList[7]+"*"+str(CakePriceList[7]),variable = VarCakeList[7],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarCakeList[7],txtCake7,EntryCakeList[7])).grid(row= 7, sticky=W)

#=======================Enter Widgets for Cake =======================
txtCake0 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[0],state = DISABLED)
txtCake0.grid(row=0,column =1)
txtCake1 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[1],state = DISABLED)
txtCake1.grid(row=1,column =1)
txtCake2 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[2],state = DISABLED)
txtCake2.grid(row=2,column =1)
txtCake3 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[3],state = DISABLED)
txtCake3.grid(row=3,column =1)
txtCake4 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[4],state = DISABLED)
txtCake4.grid(row=4,column =1)
txtCake5 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[5],state = DISABLED)
txtCake5.grid(row=5,column =1)
txtCake6 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[6],state = DISABLED)
txtCake6.grid(row=6,column =1)
txtCake7 = Entry(fCake,font=('TH Sarabun New',18,'bold'),bd=8,width=6,justify='left',textvariable=EntryCakeList[7],state = DISABLED)
txtCake7.grid(row=7,column =1)

#================================== Receipt Information ===================
_ = Label(fReceipt,font=('TH Sarabun New',12,'bold'), text="Receipt", bd=2,anchor='w')
_.grid(row=0,column=0, sticky=W)
txtReceipt = Text(fReceipt,font=('TH Sarabun New',11,'bold'), bd=8,width=59,height=22,bg="white")
txtReceipt.grid(row=1,column=0)

#=================================== Cost Items Information============
_ = Label(fCost1,font=('TH Sarabun New',18,'bold'),text="Cost of Drinks",bd=8)
_.grid(row=0,column=0,sticky=W)
_=Entry(fCost1,font=('TH Sarabun New',18,'bold'),bd=8,justify='left',
                      textvariable=CostofDrinks)
_.grid(row=0,column=1,sticky=W)

_ = Label(fCost1,font=('TH Sarabun New',18,'bold'),text="Cost of Cakes",bd=8)
_.grid(row=1,column=0,sticky=W)
_=Entry(fCost1,font=('TH Sarabun New',18,'bold'),bd=8,justify='left',
                     textvariable=CostofCakes)
_.grid(row=1,column=1,sticky=W)

_ = Label(fCost1,font=('TH Sarabun New',18,'bold'),text="Service Charge",bd=8)
_.grid(row=2,column=0,sticky=W)
_=Entry(fCost1,font=('TH Sarabun New',18,'bold'),bd=8,justify='left',
                       textvariable=ServiceCharge)
_.grid(row=2,column=1,sticky=W)

#=========================== Payment Information========================
_ = Label(fCost2,font=('TH Sarabun New',18,'bold'),text="Paid Tax",bd=8)
_.grid(row=0,column=0,sticky=W)
_=Entry(fCost2,font=('TH Sarabun New',18,'bold'),bd=8,justify='left',
                 textvariable=PaidTax)
_.grid(row=0,column=1,sticky=W)

_ = Label(fCost2,font=('TH Sarabun New',18,'bold'),text="Sub Total",bd=8)
_.grid(row=1,column=0,sticky=W)
_=Entry(fCost2,font=('TH Sarabun New',18,'bold'),bd=8,justify='left',
                  textvariable=SubTotal)
_.grid(row=1,column=1,sticky=W)

_ = Label(fCost2,font=('TH Sarabun New',18,'bold'),text="Total",bd=8)
_.grid(row=2,column=0,sticky=W)
_=Entry(fCost2,font=('TH Sarabun New',18,'bold'),bd=8,justify='left',
                   textvariable=TotalCost)
_.grid(row=2,column=1,sticky=W)

#================================== Button =========================
_=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Total",command=CostofItem).grid(row=0, column=0)
_=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Receipt",command=Receipt).grid(row=0, column=1)
_=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Reset",command=Reset).grid(row=0, column=2)
_=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Exit",command=qExit).grid(row=0, column=3)


root.mainloop()
