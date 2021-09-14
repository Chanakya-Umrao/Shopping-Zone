from tkinter import *
from tkinter import messagebox
import sqlite3



root1=Tk()
root1.title("Signup")
root1.attributes("-fullscreen",True)
varusername=StringVar()
varpassword=StringVar()
logo=PhotoImage(file="back.png")
root1.attributes("-fullscreen",True)
ll=Button(root1,bg="white")
ll.configure(image=logo)
ll.place(x=0,y=0)


def createdb_clicked():
    sqlite_file = 'apshop.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("create table if not exists logininfo(username Text,password Text)")
    uname=str(varusername.get())
    pwd=str(varpassword.get())
    c.execute("select * from logininfo where username=(?) and password=(?)",(uname,pwd))
    data=c.fetchall()
    if(len(data)==0):
        c.execute("insert into logininfo (username,password) values (?,?)",(uname,pwd))
        messagebox.showinfo("Great","User created...")
    else:
        messagebox.showerror("Error","Username already exists...")
    conn.commit()
    conn.close()


def clear_clicked():
    varusername.set("")
    varpassword.set("")

def back_clicked():
        import os
        os.system("log.py")
        root1.destroy()
        
    

titleLabel=Label(root1,text="Signup",font=("calibiri",40),bg='white',fg="black").place(x=550,y=100);
lblusername1=Label(root1,text="USERNAME",font=("calibiri",30),bg='white',fg="black").place(x=420,y=250);
lblpassword1=Label(root1,text="PASSWORD",font=("calibiri",30),bg='white',fg="black",).place(x=420,y=350);

txtusername1=Entry(root1,font=("Arial",30),bg='white',fg="black",textvariable=varusername)
txtusername1.place(x=750,y=250);
txtusername1.focus()
txtpassword=Entry(root1,font=("Arial",30),bg='white',fg="black",show="*",textvariable=varpassword)
txtpassword.place(x=750,y=350);


btncreate1=Button(root1,text="Create",font=("calibiri",20),bg='white',fg="black",command=createdb_clicked).place(x=650,y=500)

btnclear1=Button(root1,text="Clear",font=("calibiri",20),bg='white',fg="black",command=clear_clicked).place(x=850,y=500);
btnback1=Button(root1,text="Back to Login",bg='white',fg="black",font=("black",20),command=back_clicked).place(x=1050,y=500);

root1.mainloop()
