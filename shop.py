from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import filedialog
import os

root=Tk()
root.title("Shop")
root.configure(bg="white")
root.attributes("-fullscreen",True)

logo=PhotoImage(file="back.png")
root.attributes("-fullscreen",True)
ll=Label(root)
ll.configure(image=logo)
ll.place(x=0,y=0)

def fresh():
    root.destroy()
    os.system("shop.py")
menu = Menu(root)
root.config(menu=menu)
Profile = Menu(menu)
Orders= Menu(menu)
Contact= Menu(menu)
Exit= Menu(menu)

menu.add_cascade(label="Profile", menu=Profile)
menu.add_cascade(label="Orders", menu=Orders)
menu.add_cascade(label="Contact Us", menu=Contact)
menu.add_cascade(label="Exit", menu=Exit)

Profile.add_command(label="My Profile")

Orders.add_command(label="New Item",command=fresh)

Contact.add_command(label="Call us: 7206603613", )
Contact.add_command(label="Email us: apshop@gmail.com", )
Contact.add_command(label="Instagram: aprechargebox", )
Contact.add_command(label="Twitter: aprechargebox")

Exit.add_command(label="Quit App",command=root.destroy)

q=IntVar()
def click():
    root.geometry("1204x720")
    a=q.get()
    if(a==1):
        root.destroy()
        os.system("mc.py")
    if(a==2):
        root.destroy()
        os.system("wc.py")
    if(a==3):
        root.destroy()
        os.system("mo.py")
    if(a==4):
        root.destroy()
        os.system("ma.py")
    if(a==5):
        root.destroy()
        os.system("pa.py")
    if(a==6):
        root.destroy()
        os.system("jw.py")
        
     
    
def shop():
        root.destroy()
        import shop
        
      
c1=Radiobutton(root,text=("Men Clothing"),width=30,value=1,variable=q,command=click).grid(row=3,column=1)
c2=Radiobutton(root,text=("Women Clothing"),width=30,value=2,variable=q,command=click).grid(row=4,column=1)
c3=Radiobutton(root,text="Mobile",width=30,value=3,variable=q,command=click).grid(row=5,column=1)
c4=Radiobutton(root,text="Mobile Accessories",width=30,value=4,variable=q,command=click).grid(row=6,column=1)
c5=Radiobutton(root,text="Pantry",width=30,value=5,variable=q,command=click).grid(row=7,column=1)
c6=Radiobutton(root,text="Jewellerey",width=30,value=6,variable=q,command=click).grid(row=9,column=1)
c7=Button(root,text="Retry",command=shop).grid(row=10,column=1)








root.mainloop()

