from tkinter import *
from tkinter import messagebox
import os
import sqlite3
root=Tk()
root.title("Home Screen")
root.configure(bg="white")
logo=PhotoImage(file="back.png")
root.attributes("-fullscreen",True)
ll=Button(root,bg="white")
ll.configure(image=logo)
ll.place(x=0,y=0)
label1=Label(root,text="To place an order you must Login or Signup",font=("Aerial",50),bg="white",fg="black").place(x=250,y=150)


def logindb_clicked():
    os.system("log.py")
    root.destroy()

def create_clicked():
    os.system("sup.py")
    root.destroy()

    
def cancel_clicked():
    root.destroy()


btnlogin=Button(root,text="Login",font=("Calibri",20),bg="black",fg="white",command=logindb_clicked).place(x=550,y=500);
btncreate=Button(root,text="Signup",font=("Calibri ",20),bg="black",fg="white",command=create_clicked).place(x=750,y=500);
btncancel=Button(root,text="Back",font=("Calibri ",20),bg="black",fg="white",command=cancel_clicked).place(x=950,y=500);
root.mainloop()
