from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import filedialog
import os

import random
root=Tk()
root.title("Shop")
root.configure(bg="white")
root.attributes("-fullscreen",True)


logo=PhotoImage(file="back.png")
root.attributes("-fullscreen",True)
ll=Label(root)
ll.configure(image=logo)
ll.place(x=0,y=0)

def show():
        root3=Tk()
        root3.geometry('600x480')
        file=open('order.txt','r+')
        z=''
        data=file.readlines()
        for f in data:
                        i=1;
                        l=f.rstrip().split(',')
                        x=('Order id:'+str(random.randint(10000,20000))+'\nItem name:'+str(l[0])+'\nItem Price:'+str(l[1])+'\n\n')
                        z=z+x
                        i=i+1
        orderlabel=Label(root3,text=z,font=('aerial')).place(x=10,y=20)
                        
        file.close()



def addr():
        def placed():
            root1.destroy()
            root2=Tk()
            
            root2.geometry("455x600")
            file=open('order.txt','a+')
            oc=ps.get()
            if oc==1:
                n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name1var.get())+"\n amouting to   "+str(price1var.get()),font=("aerial")).place(x=100,y=250)
                file.write(name1var.get()+","+str(price1var.get())+'\n')
                file.close()
            if oc==2:
                 n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name2var.get())+"\n amouting to   "+str(price2var.get()),font=("aerial")).place(x=100,y=250)
                 file.write(name2var.get()+","+str(price2var.get())+'\n')
                 file.close()
            if oc==3:
                 n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name3var.get())+"\n amouting to   "+str(price3var.get()),font=("aerial")).place(x=100,y=250)
                 file.write(name3var.get()+","+str(price3var.get())+'\n')
                 file.close()
            if oc==4:
                 n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name4var.get())+"\n amoutaing to   "+str(price4var.get()),font=("aerial")).place(x=100,y=250)
                 file.write(name4var.get()+","+str(price4var.get())+'\n')
                 file.close()            
            if oc==5:
                 n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name5var.get())+"\n amouting to   "+str(price5var.get()),font=("aerial")).place(x=100,y=250)
                 file.write(name5var.get()+","+str(price5var.get())+'\n')
                 file.close()
            if oc==6:
                 n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name6var.get())+"\n amouting to   "+str(price6var.get()),font=("aerial")).place(x=100,y=250)
                 file.write(name6var.get()+","+str(price6var.get())+'\n')
                 file.close()
            if oc==7:
                 n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name7var.get())+"\n amouting to   "+str(price7var.get()),font=("aerial")).place(x=100,y=250)
                 file.write(name7var.get()+","+str(price7var.get())+'\n')
                 file.close()
            if oc==8:
                n1=Label(root2,text="Thanks"+str(namevar.get())+"for ordering  "+str(name8var.get())+"\n amouting to   "+str(price8var.get()),font=("aerial")).place(x=100,y=250)
                file.write(name8var.get()+","+str(price8var.get())+'\n')
                file.close()
            
            
            def waitfn():
                root2.destroy()
                
            root2.after(2000,waitfn)
            
    

            
            
        os.system('home.py')

        def backad():
         root1.destroy()

        root1=Tk()
        root1.title("Address Details")
        root1.configure()
        root1.attributes("-fullscreen",True)
        btncreate=Button(root1,text="Place Order",width=20,command=placed).place(x=800,y=950);
        btncreat=Button(root1,text="Back",width=20,command=backad).place(x=1000,y=950);
        
    

        name=Label(root1,text="Name",font=("aerial",20)).place(x=420,y=150);
        area=Label(root1,text="Area",font=("aerial",20)).place(x=420,y=250);
        local=Label(root1,text="Locality",font=("aerial",20)).place(x=420,y=350);
        land=Label(root1,text="Landmark",font=("aerial",20)).place(x=420,y=450);
        city=Label(root1,text="City",font=("aerial",20)).place(x=420,y=550);
        state=Label(root1,text="State",font=("aerial",20)).place(x=420,y=650);
        pin=Label(root1,text="Pincode",font=("aerial",20)).place(x=420,y=750);
        mn=Label(root1,text="Mobile Number",font=("aerial",20)).place(x=420,y=850);

        namevar=StringVar()
        namee=Entry(root1,font=("Arial",20),textvariable=namevar).place(x=700,y=150);
        areae=Entry(root1,font=("Arial",20)).place(x=700,y=250);
        locale=Entry(root1,font=("Arial",20)).place(x=700,y=350);
        lande=Entry(root1,font=("Arial",20)).place(x=700,y=450);
        citye=Entry(root1,font=("Arial",20)).place(x=700,y=550);
        statee=Entry(root1,font=("Arial",20)).place(x=700,y=650);
        pine=Entry(root1,font=("Arial",20)).place(x=700,y=750);
        mne=Entry(root1,font=("Arial",20)).place(x=700,y=850);


    
            
            
        
        
def bac():
    root1.destroy()


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
Orders.add_command(label="My orders",command=show)

Contact.add_command(label="Call us: 7206603613", )
Contact.add_command(label="Email us: apshop@gmail.com", )
Contact.add_command(label="Instagram: aprechargebox", )
Contact.add_command(label="Twitter: aprechargebox")

Exit.add_command(label="Quit App",command=root.destroy)



price1var=IntVar()
price1var.set("44999")
price2var=IntVar()
price2var.set("50999")
price3var=IntVar()
price3var.set("12999")
price4var=IntVar()
price4var.set("9999")
price5var=IntVar()
price5var.set("13999")
price6var=IntVar()
price6var.set("6999")
price7var=IntVar()
price7var.set("15999")
price8var=IntVar()
price8var.set("39999")

name1var=StringVar()
name1var.set("iPhone 7")
name2var=StringVar()
name2var.set("iPhone 8")
name3var=StringVar()
name3var.set("Samsung M30")
name4var=StringVar()
name4var.set("Redmi Note")
name5var=StringVar()
name5var.set("Nokia 6")
name6var=StringVar()
name6var.set("Redmi 7")
name7var=StringVar()
name7var.set("Oppo V1")
name8var=StringVar()
name8var.set("Oneplus 6t")

price1=Label(root,textvariable=price1var,font=("aerial")).place(x=290,y=220)
name1=Label(root,textvariable=name1var,font=("aerial")).place(x=260,y=250)
price2=Label(root,textvariable=price2var,font=("aerial")).place(x=550,y=220)
name2=Label(root,textvariable=name2var,font=("aerial")).place(x=520,y=250)
price3=Label(root,textvariable=price3var,font=("aerial")).place(x=810,y=220)
name3=Label(root,textvariable=name3var,font=("aerial")).place(x=780,y=250)
price4=Label(root,textvariable=price4var,font=("aerial")).place(x=1070,y=220)
name4=Label(root,textvariable=name4var,font=("aerial")).place(x=1020,y=250)
price5=Label(root,textvariable=price5var,font=("aerial")).place(x=290,y=510)
name5=Label(root,textvariable=name5var,font=("aerial")).place(x=260,y=540)
price6=Label(root,textvariable=price6var,font=("aerial")).place(x=550,y=510)
name6=Label(root,textvariable=name6var,font=("aerial")).place(x=520,y=540)
price7=Label(root,textvariable=price7var,font=("aerial")).place(x=810,y=510)
name7=Label(root,textvariable=name7var,font=("aerial")).place(x=780,y=540)
price8=Label(root,textvariable=price8var,font=("aerial")).place(x=1070,y=510)
name8=Label(root,textvariable=name8var,font=("aerial")).place(x=1040,y=540)
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
        
     
    
        
      
c1=Radiobutton(root,text=("Men Clothing"),width=30,value=1,variable=q,command=click).grid(row=3,column=1)
c2=Radiobutton(root,text=("Women Clothing"),width=30,value=2,variable=q,command=click).grid(row=4,column=1)
c3=Radiobutton(root,text="Mobile",width=30,value=3,variable=q,command=click).grid(row=5,column=1)
c4=Radiobutton(root,text="Mobile Accessories",width=30,value=4,variable=q,command=click).grid(row=6,column=1)
c5=Radiobutton(root,text="Pantry",width=30,value=5,variable=q,command=click).grid(row=7,column=1)
c6=Radiobutton(root,text="Jewellerey",width=30,value=6,variable=q,command=click).grid(row=9,column=1)



ps=IntVar()
mc1=Radiobutton(root,command=addr,value=1,variable=ps)
mc1i=PhotoImage(file="ph1.png")
mc1.configure(image=mc1i)
mc2=Radiobutton(root,command=addr,value=2,variable=ps)
mc2i=PhotoImage(file="ph2.png")
mc2.configure(image=mc2i)
mc3=Radiobutton(root,command=addr,value=3,variable=ps)
mc3i=PhotoImage(file="ph3.png")
mc3.configure(image=mc3i)
mc4=Radiobutton(root,command=addr,value=4,variable=ps)
mc4i=PhotoImage(file="ph4.png")
mc4.configure(image=mc4i)
mc5=Radiobutton(root,command=addr,value=5,variable=ps)
mc5i=PhotoImage(file="ph5.png")
mc5.configure(image=mc5i)
mc6=Radiobutton(root,command=addr,value=6,variable=ps)
mc6i=PhotoImage(file="ph6.png")
mc6.configure(image=mc6i)
mc7=Radiobutton(root,command=addr,value=7,variable=ps)
mc7i=PhotoImage(file="ph7.png")
mc7.configure(image=mc7i)
mc8=Radiobutton(root,command=addr,value=8,variable=ps)
mc8i=PhotoImage(file="ph8.png")
mc8.configure(image=mc8i)


mc1.place(x=220,y=10)
mc2.place(x=480,y=10)
mc3.place(x=740,y=10)
mc4.place(x=1000,y=10)
mc5.place(x=220,y=300)
mc6.place(x=480,y=300)
mc7.place(x=740,y=300)
mc8.place(x=1000,y=300)

root.mainloop()
