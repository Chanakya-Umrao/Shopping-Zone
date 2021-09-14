from tkinter import *
import time
root=Tk()
root.title("Home Screen")
root.geometry("455x600")
root.configure(bg="white")
titleLabel0=Label(root,text="",font=("italic",50),bg="white")
titleLabel0.grid(row=0,column=7)
titleLabel1=Label(root,text="Shopping Zone",font=("italic",40),bg="white")
titleLabel1.grid(row=4,column=7)
titleLabel2=Label(root,text="The Online Shopping App",font=("italic",30),fg='purple',bg="white")
titleLabel2.grid(row=8,column=7)
titleLabel4=Label(root,text="",font=("italic",10),bg="white")
titleLabel4.grid(row=10,column=7)
logo=PhotoImage(file="logo.png")
ll=Button(root,bg="white")
ll.configure(image=logo)
ll.grid(row=12,column=7)
nameLabel3=Label(root,text="Submitted by: CHANAKYA UMRAO",font=("stencil",),bg='white',fg='black')
nameLabel3.grid(row=15,column=7)
nameLabel6=Label(root,text="loading...",font=("aerial",10),bg='white',fg='black')
nameLabel6.grid(row=20,column=7)

def waitfn():
    import os
    time.sleep(1)
    root.destroy()
    os.system('mc.py')


root.after(4000,waitfn)
root.mainloop()

