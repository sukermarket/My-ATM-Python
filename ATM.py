from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
from tkinter import messagebox


window=ThemedTk(theme='equilux')
window.configure(themebg="equilux")
window.title('My ATM')
window.geometry('250x400')
balance=random.randint(0,100000)


def transferbutton():
    global balance,amount,transferamount,ShowBalance,trnsfrname,transfername
    transferamount = amount.get()
    transfername=trnsfrname.get()
    if int(transferamount) > int(balance):
        messagebox.showerror('Error', 'insufficent funds')
        amount.delete(0, END)
    elif int(transferamount) < int(balance):
        balance = balance - int(transferamount)
        ShowBalance.configure(text='Your balance is:' + str(balance))
        amount.delete(0, END)
        trnsfrname.delete(0, END)
        messagebox.showinfo('Transfer Succesful','Transfer succesful, you have sent '+str(transferamount)+' to '+str(transfername))
    file = open('Transactions.txt','a')
    file.write('transfer:'+transferamount+'\n')
    file.close()


def transfer1():
    global amount,ShowBalance,trnsfrname
    for widget in window.winfo_children():
        widget.destroy()
    titletransfer=ttk.Label(window,text='Transfer',font=('tahoma',18))
    titletransfer.place(x=77,y=80)
    namelabel=ttk.Label(window,text='Recipient',font=('tahoma',12))
    namelabel.place(x=90,y=130)
    trnsfrname=ttk.Entry(window,width=25)
    trnsfrname.place(x=45,y=150)
    amountlabel=ttk.Label(window,text="Amount",font=('tahoma',12))
    amountlabel.place(x=95,y=180)
    amount=ttk.Entry(window,width=25)
    amount.place(x=45,y=200)
    confirm=ttk.Button(window,text='Confirm',command=transferbutton)
    confirm.place(x=80,y=230)
    backbutton=ttk.Button(window,text="Back",command=first_window)
    backbutton.place(x=80,y=260)
    ShowBalance = ttk.Label(window, text='Your balance is:' + str(balance), font=('tahoma', 12))
    ShowBalance.place(x=47, y=110)
    username = ttk.Label(text="© @Sukermarket", font=("Helvetica", 12, "bold"))
    username.place(x=10, y=377)

def withdrawbutton():
    global balance, withdrawamount, withdraw,ShowBalance,wthdrw
    withdrawamount = wthdrw.get()
    if int(withdrawamount) > int(balance):
        messagebox.showerror('Error', 'insufficent funds')
        wthdrw.delete("-1", "end")
    elif int(withdrawamount) < int(balance):
        balance = balance - int(withdrawamount)
        ShowBalance.configure(text='Your balance is:' + str(balance))
        wthdrw.delete("-1","end")
    file = open('Transactions.txt','a')
    file.write('withdraw:'+withdrawamount+'\n')
    file.close()


def withdraw1():
    global withdrawbutton,donewithdraw,balance,wthdrw,ShowBalance
    for widget in window.winfo_children():
        widget.destroy()
    titlewithdraw=ttk.Label(window,text='Withdraw',font=('tahoma',18))
    titlewithdraw.place(x=75,y=100)
    wthdrw=ttk.Entry(window,width=25)
    wthdrw.place(x=45,y=160)
    withdrawbutton=ttk.Button(window,text='Withdraw',command=withdrawbutton)
    withdrawbutton.place(x=80,y=190)
    donewithdraw = ttk.Button(window, text='Done', command=first_window)
    donewithdraw.place(x=80,y=220)
    ShowBalance = ttk.Label(window, text='Your balance is:' + str(balance), font=('tahoma', 12))
    ShowBalance.place(x=47,y=130)
    username = ttk.Label(text="© @Sukermarket", font=("Helvetica", 12, "bold"))
    username.place(x=10, y=377)



def depositbutton():
    global balance,depositamount,deposit,dpst,ShowBalance
    depositamount=dpst.get()
    balance=balance+int(depositamount)
    ShowBalance.configure(text='Your balance is:' + str(balance))
    file = open('Transactions.txt', 'a')
    file.write('deposit:' + depositamount + '\n')
    file.close()
def deposit1():
    global deposit1,depositbutton,donedeposit,ShowBalance,dpst
    for widget in window.winfo_children():
        widget.destroy()
    titledeposit=ttk.Label(window,text="Deposit",font=("tahoma", 18),)
    titledeposit.place(x=80,y=100)
    dpst=ttk.Entry(window,width=25)
    dpst.place(x=45,y=160)
    depositbutton=ttk.Button(window,text='Deposit',command=depositbutton)
    depositbutton.place(x=80,y=190)
    donedeposit=ttk.Button(window,text='Done',command=first_window)
    donedeposit.place(x=80,y=220)
    ShowBalance = ttk.Label(window, text='Your balance is:' + str(balance), font=('tahoma', 12))
    ShowBalance.place(x=47,y=130)
    username = ttk.Label(text="© @Sukermarket", font=("Helvetica", 12, "bold"))
    username.place(x=10, y=377)

def password2():
    global pwd
    checkpassword=pwd.get()
    if checkpassword == "123":
        first_window()
    else:
        messagebox.showerror('Wrong password','Wrong password, Try again.')
        pwd.delete(0, END)

def password():
    global pwd
    for widget in window.winfo_children():
        widget.destroy()
    lbl2 =ttk.Label(window, text="Password:", font=("tahoma", 18), )
    lbl2.place(x=70,y=130)

    pwd =ttk.Entry(window, width=25, show="*")
    pwd.place(x=50,y=170)

    done=ttk.Button(window,text='done',command=password2)
    done.place(x=85,y=200)

    username = ttk.Label(text="© @Sukermarket", font=("Helvetica", 12, "bold"))
    username.place(x=10, y=377)

def first_window():
    for widget in window.winfo_children():
        widget.destroy()

    ATM=ttk.Label(window,text='A.T.M',font=("tahoma",18))
    ATM.place(x=95,y=100)

    ShowBalance=ttk.Label(window,text='Your balance is:'+str(balance),font=('tahoma',12))
    ShowBalance.place(x=45,y=130)

    deposit=ttk.Button(window,text='Deposit',command=deposit1)
    deposit.place(x=85,y=160)

    withdraw=ttk.Button(window,text='Withdraw',command=withdraw1)
    withdraw.place(x=85,y=190)

    transfer=ttk.Button(window,text='Transfer',command=transfer1)
    transfer.place(x=85,y=220)

    username = ttk.Label(text="© @Sukermarket", font=("Helvetica", 12, "bold"))
    username.place(x=10,y=377)


insert= ttk.Button(window,text='Insert card',command=password)
insert.place(x=85,y=170)

username = ttk.Label(text="© @Sukermarket", font=("Helvetica", 12, "bold"))
username.place(x=10,y=377)

window.mainloop()