from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Login")
root.attributes("-fullscreen",True)

varusername=StringVar()
varpassword=StringVar()
logo=PhotoImage(file="back.png")
root.attributes("-fullscreen",True)
ll=Button(root,bg="white")
ll.configure(image=logo)
ll.place(x=0,y=0)


def createdb_clicked():
        sqlite_file= 'apshop.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        uname=str(varusername.get())
        pwd=str(varpassword.get())
        c.execute("select * from logininfo where username=(?) and password=(?)",(uname,pwd))
        data=c.fetchall()
        if(len(data)==0):
            messagebox.showerror("Error","Wrong details entered...")
        else:
            root.destroy()

        conn.commit()
        conn.close()


    

    

def clear_clicked():
    varusername.set("")
    varpassword.set("")

def back_clicked():
    import os
    root.destroy()
    
    


titleLabel=Label(root,text="Login to the AbhiShop",font=("aerial",40),fg='black').place(x=550,y=100);

lblusername=Label(root,text="Username",font=("aerial",30),fg='black').place(x=420,y=250);
lblpassword=Label(root,text="Password",font=("aerial",30),fg='black').place(x=420,y=350);

txtusername=Entry(root,font=("Arial",30),fg='black',textvariable=varusername)
txtusername.place(x=750,y=250);
txtpassword=Entry(root,font=("Arial",30),fg='black',show="*",textvariable=varpassword)
txtpassword.place(x=750,y=350);


btncreate=Button(root,text="Login",font=("aerial",20),fg='black',command=createdb_clicked).place(x=650,y=500);
btnclear=Button(root,text="Clear",font=("aerial",20),fg='black',command=clear_clicked).place(x=850,y=500);
btnback=Button(root,text="Exit",font=("aerial",20),fg='black',command=back_clicked).place(x=1050,y=500);

txtusername.focus()

root.mainloop()
