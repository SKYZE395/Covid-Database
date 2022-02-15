from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import os
import mysql.connector as sql
import tkinter.ttk as ttk
dbcon=sql.connect(host="localhost",database="donation",user="root",passwd="candy123")
dbcursor=dbcon.cursor()

def june_graph():
    global root

    dbcon=sql.connect(host="localhost",database="CORONA",user="root",passwd="candy123")
    dbcursor=dbcon.cursor()
    dbcursor.execute("select DOC_june from june_gujarat")

    x=dbcursor.fetchall()

    dbcursor.execute("select deaths from june_gujarat")

    y=dbcursor.fetchall()

    dbcursor.execute("select Active_cases from june_gujarat")

    z=dbcursor.fetchall()

    dbcursor.execute("select Total_cases from june_gujarat")

    a=dbcursor.fetchall()

    plt.figure(figsize=(10,5))
    plt.plot(x,y,label="DEATHS",marker="*")
    plt.plot(x,z,label="TOTAL CASES",marker="D")
    
    plt.legend()
    plt.xlim(1,30)
    plt.xticks(range(1,31))
    plt.title("ACTIVE CASES,DEATHS AND TOTAL CASES",fontstyle="italic")
    plt.xlabel("TIME(DAYS):-(june)")
    plt.ylabel("CASES")
    plt.show()

def july_graph():
    global root
    dbcon=sql.connect(host="localhost",database="CORONA",user="root",passwd="candy123")
    dbcursor=dbcon.cursor()
    dbcursor.execute("select DOC_july from july_gujarat")

    x=dbcursor.fetchall()

    dbcursor.execute("select deaths from july_gujarat")

    y=dbcursor.fetchall()

    dbcursor.execute("select Active_cases from july_gujarat")

    z=dbcursor.fetchall()

    dbcursor.execute("select Total_cases from july_gujarat")

    a=dbcursor.fetchall()

    plt.figure(figsize=(10,5))
    plt.plot(x,y,label="DEATHS",marker="*")
    plt.plot(x,z,label="TOTAL CASES",marker="D")
    
    plt.legend()
    plt.xlim(1,31)
    plt.xticks(range(1,32))
    plt.title("ACTIVE CASES,DEATHS AND TOTAL CASES",fontstyle="italic")
    plt.xlabel("TIME(DAYS);-(July)")
    plt.ylabel("CASES")
    plt.show()

def august_graph():
    global root

    dbcon=sql.connect(host="localhost",database="CORONA",user="root",passwd="candy123")
    dbcursor=dbcon.cursor()
    dbcursor.execute("select DOC_august from august_gujarat")

    x=dbcursor.fetchall()

    dbcursor.execute("select deaths from august_gujarat")

    y=dbcursor.fetchall()

    dbcursor.execute("select Active_cases from august_gujarat")

    z=dbcursor.fetchall()

    dbcursor.execute("select Total_cases from august_gujarat")

    a=dbcursor.fetchall()
    
    plt.figure(figsize=(10,5))
    plt.plot(x,y,label="DEATHS",marker="*")
    plt.plot(x,z,label="TOTAL CASES",marker="D")
    
    plt.legend()
    plt.xlim(1,31)
    plt.xticks(range(1,32))
    plt.title("ACTIVE CASES,DEATHS AND TOTAL CASES",fontstyle="italic")
    plt.xlabel("TIME(DAYS):-(August)")
    plt.ylabel("CASES")
    plt.show()

def graph1_june():
    global root

    dbcon=sql.connect(host="localhost",database="CORONA",user="root",passwd="candy123")
    dbcursor=dbcon.cursor()
    dbcursor.execute("select DOC_june from june_india")

    x=dbcursor.fetchall()

    dbcursor.execute("select deaths from june_india")

    y=dbcursor.fetchall()

    dbcursor.execute("select Active_cases from june_india")

    z=dbcursor.fetchall()

    dbcursor.execute("select Total_cases from june_india")

    a=dbcursor.fetchall()
    
    plt.figure(figsize=(10,5))
    plt.plot(x,y,label="DEATHS",marker="*")
    plt.plot(x,z,label="TOTAL CASES",marker="D")
    
    plt.legend()
    plt.xlim(1,30)
    plt.xticks(range(1,31))
    plt.title(label="ACTIVE CASES,DEATHS AND TOTAL CASES",fontstyle="italic")
    plt.xlabel("TIME(DAYS):-(June)")
    plt.ylabel("CASES")
    plt.show()

def graph1_july():
    global root
    dbcon=sql.connect(host="localhost",database="CORONA",user="root",passwd="candy123")
    dbcursor=dbcon.cursor()
    dbcursor.execute("select DOC_july from july_india")

    x=dbcursor.fetchall()

    dbcursor.execute("select deaths from july_india")

    y=dbcursor.fetchall()

    dbcursor.execute("select Active_cases from july_india")

    z=dbcursor.fetchall()

    dbcursor.execute("select Total_cases from july_india")

    a=dbcursor.fetchall()
    
    plt.figure(figsize=(10,5))
    plt.plot(x,y,label="DEATHS",marker="*")
    plt.plot(x,z,label="TOTAL CASES",marker="D")
    
    plt.legend()
    plt.xlim(1,31)
    plt.xticks(range(1,32))
    plt.title(label="ACTIVE CASES,DEATHS AND TOTAL CASES",fontstyle="italic")
    plt.xlabel("TIME(DAYS):-(July)")
    plt.ylabel("CASES")
    plt.show()

def graph1_august():
    global root
    dbcon=sql.connect(host="localhost",database="CORONA",user="root",passwd="candy123")
    dbcursor=dbcon.cursor()
    dbcursor.execute("select DOC_august from august_india")

    x=dbcursor.fetchall()

    dbcursor.execute("select deaths from august_india")

    y=dbcursor.fetchall()

    dbcursor.execute("select Active_cases from august_india")

    z=dbcursor.fetchall()

    dbcursor.execute("select Total_cases from august_india")

    a=dbcursor.fetchall()
     
    plt.figure(figsize=(10,5))
    plt.plot(x,y,label="DEATHS",marker="*")
    plt.plot(x,z,label="TOTAL CASES",marker="D")
    
    plt.legend()
    plt.xlim(1,31)
    plt.xticks(range(1,32))
    plt.title(label="ACTIVE CASES,DEATHS AND TOTAL CASES",fontstyle="italic")
    plt.xlabel("TIME(DAYS):-(August)")
    plt.ylabel("CASES")
    plt.show()
    
def GUJwin():
    global root
    root.destroy()
    root = Tk()
    root.geometry("1366x768+0+0")
    root.title("GUJARAT UPDATES")
    Pic=ImageTk.PhotoImage(Image.open("VADCVDMAP.jpg").resize((1400,710)))
    L2=Label(root,image=Pic)
    L2.place(x=0,y=0)

    
    B2=Button(root,text="RETURN TO HOME PAGE",command=mainscreen)
    B2.place(x=90,y=90,width=250,height=30)

    B3=Button(root,text="SHOW GRAPH OF JUNE",command=june_graph)
    B3.place(x=90,y=200,width=250,height=30)

    B4=Button(root,text="SHOW GRAPH OF JULY",command=july_graph)
    B4.place(x=90,y=300,width=250,height=30)

    B5=Button(root,text="SHOW GRAPH OF AUGUST",command=august_graph)
    B5.place(x=90,y=400,width=250,height=30)
    root.mainloop()

def INDwin():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1366x768+0+0")
    root.title("VADODARA UPDATES")
    picture=ImageTk.PhotoImage(Image.open("INDIAMAP.jpg").resize((1400,710)))
    L3=Label(root,image=picture)
    L3.place(x=0,y=0)
    
    B2=Button(root,text="RETURN TO HOME PAGE",command=mainscreen)
    B2.place(x=90,y=90,width=250,height=30)
    
    B3=Button(root,text="GRAPH OF JUNE",command=graph1_june)
    B3.place(x=800,y=500,width=250,height=30)

    B4=Button(root,text="GRAPH OF JULY",command=graph1_july)
    B4.place(x=800,y=550,width=250,height=30)

    B5=Button(root,text="GRAPH OF AUGUST", command=graph1_august)
    B5.place(x=800,y=600,width=250,height=30)
    root.mainloop()
def PUBLIC():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1366x768+0+0")
    root.title("PRECAUTIONS FOR PUBLIC PLACES")

    img1=ImageTk.PhotoImage(Image.open("BACKGROUND.jpeg").resize((2000,2000)))
    L1=Label(root,image=img1)
    L1.place(x=0,y=0)

    B2=Button(root,text="RETURN TO HOME PAGE",command=mainscreen)
    B2.place(x=20,y=0,width=250,height=30)

    B3=Button(root,text="BACK",command=PRCwin)
    B3.place(x=20,y=650,width=250,height=30)

    L14=Label(root,text="IN PUBLIC PLACES",bg="white")
    L14.config(font=("Arial Nova",30))
    L14.place(x=20,y=50)

    L5=Label(root,text="1) Avoid touching your eyes, nose, and mouth with unwashed hands.",bg="white")
    L5.config(font=("Arial Nova",15))
    L5.place(x=0,y=130)

    L6=Label(root,text="2) Keeping distance from others is especially important for people who are at higher risk of getting very sick.",bg="white")
    L6.config(font=("Arial Nova",15))
    L6.place(x=0,y=190)

    L10=Label(root,text="3) If soap and water are not readily available, use a hand sanitizer that contains at least 60% alcohol.",bg="white")
    L10.config(font=("Arial Nova",15))
    L10.place(x=0,y=250)

    L11=Label(root,text="4) Everyone should wear a mask in public settings and when around people who don’t live in your household.",bg="white")
    L11.config(font=("Arial Nova",15))
    L11.place(x=0,y=310)
    
    L12=Label(root,text="5) Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze.",bg="white")
    L12.config(font=("Arial Nova",15))
    L12.place(x=0,y=370)

    img2=ImageTk.PhotoImage(Image.open("ANIMATION_1.jpg").resize((400,400)))
    L2=Label(root,image=img2)
    L2.place(x=950,y=290)

    root.mainloop()
def OFFICE():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1366x768+0+0")
    root.title("PRECAUTIONS FOR OFFICE WORK")
    img1=ImageTk.PhotoImage(Image.open("BACKGROUND.jpeg").resize((1555,4007)))
    L2=Label(root,image=img1)
    L2.place(x=0,y=0)

    B2=Button(root,text="RETURN TO HOME PAGE",command=mainscreen)
    B2.place(x=20,y=0,width=250,height=30)

    B3=Button(root,text="BACK",command=PRCwin)
    B3.place(x=20,y=650,width=250,height=30)

    img2=ImageTk.PhotoImage(Image.open("OFFICE.jpg").resize((700,700)))
    L3=Label(root,image=img2)
    L3.place(x=650,y=0)

    img3=ImageTk.PhotoImage(Image.open("BLUEBKG.jpg").resize((500,100)))
    L4=Label(root,image=img3)
    L4.place(x=650,y=590)

    L14=Label(root,text="IN PUBLIC PLACES",bg="white")
    L14.config(font=("Arial Nova",30))
    L14.place(x=20,y=50)

    L6=Label(root,text="1)maintain 1.5 meters distance between each other.",bg="white")
    L6.config(font=("Arial Nova",15))
    L6.place(x=0,y=130)

    L7=Label(root,text="2)Wash your hands with soap and running water for at least 20 seconds",bg="white")
    L7.config(font=("Arial Nova",15))
    L7.place(x=0,y=190)
    
    L8=Label(root,text="3)Avoid touching each other or touching your faces with unwashed hands",bg="white")
    L8.config(font=("Arial Nova",15))
    L8.place(x=0,y=250)

    L9=Label(root,text="4)Clean and disinfect common objects prior and after their usage",bg="white")
    L9.config(font=("Arial Nova",15))
    L9.place(x=0,y=310)
    
    L10=Label(root,text="5)If sick, stay home and seek medical help",bg="white")
    L10.config(font=("Arial nova",15))
    L10.place(x=0,y=370)
    root.mainloop()
              
def PRCwin():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1366x768+0+0")
    root.title("PRECAUTIONS")
    img=ImageTk.PhotoImage(Image.open("CORONA_HOUSEHOLD.jpg").resize((650,400)))
    img1=ImageTk.PhotoImage(Image.open("BACKGROUND.jpeg").resize((1555,4007)))
    L2=Label(root,image=img1)
    L2.place(x=0,y=0)
    L1=Label(root,image=img)
    L1.place(x=710,y=300)

    B2=Button(root,text="RETURN TO HOME PAGE",command=mainscreen)
    B2.place(x=20,y=0,width=250,height=30)

    B3=Button(root,text="PRECAUTIONS FOR PUBLIC PLACES",command=PUBLIC)
    B3.place(x=20,y=600,width=250,height=30)

    B4=Button(root,text="PRECAUTIONS FOR OFFICE WORK",command=OFFICE)
    B4.place(x=300,y=600,width=250,height=30)
    
    L2=Label(root,text="PRECAUTIONS TO BE TAKEN ARE",bg="white")
    L2.config(font=("Arial Nova",30))
    L2.place(x=400,y=0)

    L14=Label(root,text="IN HOUSEHOLD",bg="white")
    L14.config(font=("Arial Nova",30))
    L14.place(x=20,y=50)

    L3=Label(root,text="1) Wash your hands with soap and water for at least 20 seconds specially after you've been in a public place or after blowing your nose or sneezing",bg="white")
    L3.config(font=("Arial Nova",15))
    L3.place(x=0,y=130)
    
    L7=Label(root,text="5) Cover your mouth and nose with a mask when around others.",bg="white")
    L7.config(font=("Arial Nova",15))
    L7.place(x=0,y=370)
   

    L8=Label(root,text="2) Clean and disinfect frequently touched surfaces daily this includes tables, doorknobs, switches,countertops, handles, phones, keyboards, and sinks.",bg="white")
    L8.config(font=("Arial Nova",15))
    L8.place(x=0,y=190)
    
    L9=Label(root,text="3)Be alert for symptoms watch for fever, cough,shortness of breath, or other symptoms of COVID-19.",bg="white")
    L9.config(font=("Arial Nova",15))
    L9.place(x=0,y=250)

    L13=Label(root,text="4)Ensure that the food you eat is well-cooked and nutritious",bg="white")
    L13.config(font=("Arial Nova",15))
    L13.place(x=0,y=310)
    
    root.mainloop()
    
def thankyou():
    global root
    root.destroy()
    root=Tk()
    root.geometry("250x70+550+250")
    root.title("MESSAGE!")

    L1=Label(root,text="We thank you for you generous donation!")
    L1.pack()

    B1=Button(root,text="RETURN BACK TO HOMESCREEN",command=mainscreen)
    B1.pack()
    root.mainloop
def DNTwin():
    global root
    root.destroy()
    root=Tk()
    root.geometry("1366x768+0+0")
    root.title("DONATIONS")

    img= ImageTk.PhotoImage(Image.open("BACKGROUND.jpeg").resize((1500,710)))
    L1=Label(root,image=img)
    L1.place(x=0,y=0)
    
    B2=Button(root,text="RETURN TO HOME PAGE",command=mainscreen)
    B2.place(x=1100,y=650,width=250,height=30)
    
    B3=Button(root,text="DONATE TO THE ORGANISATION",command=thankyou)
    B3.place(x=500,y=200)
    B3.config(font=("Arial Nova",17),height=5,width=30)

    L4=Label(root,text="EVERY DONATION EITHER BIG OR SMALL EVERY DONATION MATTERS!",bg="white")
    L4.config(font=("Arial Nova",30))
    L4.place(x=10,y=0)

    L5=Label(root,text="NAME:",bg="white")
    L5.config(font=("Arial Nova",15))
    L5.place(x=130,y=193)

    L6=Label(root,text="AMOUNT:",bg="white")
    L6.config(font=("Arial Nova",15))
    L6.place(x=105,y=246)

    L7=Label(root,text="REMARKS:",bg="white")
    L7.config(font=("Arial Nova",15))
    L7.place(x=99,y=293)

    E1=Entry(root,width=40)
    E1.place(x=200,y=200)

    E2=Entry(root,width=15)
    E2.place(x=200,y=250)

    E3=Entry(root,width=15)
    E3.place(x=200,y=300,width=200,height=100)

    B7=Button(root,text="CLARIFY!",command=lambda:OK(E1.get(),E2.get(),E3.get()))#it is a small function which can tae any number of arguements#
    B7.place(x=200,y=400)

    frm1 = Frame(root)
    scrollbarx=Scrollbar(frm1,orient = HORIZONTAL)
    scrollbary=Scrollbar(frm1,orient = VERTICAL)
    tree1 = ttk.Treeview(frm1,columns=("NAME","AMOUNT","REMARKS"),selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    tree1["columns"] = ("1","2","3")
    tree1.heading("1",text="NAME")              #Tree view is a widget which can be used to display the values in a tabular form#
    tree1.heading("2",text="AMOUNT")
    tree1.heading("3",text="REMARKS")
    tree1.column("#0",minwidth=10,width=10)
    scrollbary.config(command=tree1.yview)
    scrollbarx.config(command=tree1.xview)
    scrollbary.pack(side = RIGHT,fill = Y)
    scrollbarx.pack(side = BOTTOM,fill = X)
    tree1.pack()
    frm1.place(x=450,y=400)
    
    sql1 = "select * from dono"
    dbcursor.execute(sql1)
    var1=dbcursor.fetchall()
    for record in var1:
        tree1.insert('','end',values=(record[0],record[1],record[2]))
    
    root.mainloop()

def OK(name,amount,remarks):
    sql1 = "select * from dono"
    dbcursor.execute(sql1)           #Cursor is a mechanism that enables traversal over the records in a database#
    var1=dbcursor.fetchall()
    for record in var1:
        if name==record[0]:
            sql1="update dono set amount={}".format(int(amount)+int(record[1]))
            dbcursor.execute(sql1)
            var2=0
            break
        else:
            var2=1
            
    if var2==1:
        sql1 = "INSERT INTO dono VALUES('{}',{},'{}')".format(name,amount,remarks)
        dbcursor.execute(sql1)

    dbcon.commit()                  #saves the data#

    root.mainloop()

def Q():
    root.destroy()
    root.mainloop()

def mainscreen():
    global root
    try:
        root.destroy()
    except:
        pass
           
    root = Tk()                             #here root,acts as a variable which is given to the opening window#
    root.geometry("1380x768+0+0")
    root.title("CORONAVIRUS")

    img= ImageTk.PhotoImage(Image.open("COVER3.jpg").resize((1500,710)))
    L1=Label(root,image=img)
    L1.place(x=-10,y=0)

    HEADING=Label(root,text="ALL ABOUT COVID-19",bg="deep sky blue")
    HEADING.config(font=("Arial Nova",30))
    HEADING.place(x=480,y=0)

    MB=Label(root,text="MADE BY:-Aakash Gangurde and Yug Patel")
    MB.config(font=("Arial Nova",10))
    MB.place(x=0,y=675)
    
    B1=Button(root,text="CLICK HERE TO VIEW GUJARAT INFO",command=GUJwin)
    B1.place(x=200,y=250,width=250,height=30)

    B3=Button(root,text="CLICK HERE TO VIEW INDIA INFO",command=INDwin)
    B3.place(x=1000,y=250,width=250,height=30)

    B4=Button(root,text="CLICK HERE TO CHECK OUT PRECAUTIONS",command=PRCwin)
    B4.place(x=600,y=250,width=250,height=30)
    
    B5=Button(root,text="CLICK HERE TO DONATE TO THE UNICEF",command=DNTwin)
    B5.place(x=605,y=450,width=250,height=30)

    B6=Button(root,text="QUIT",command=Q)
    B6.place(x=1280,y=650)
    B6.config(font=("Arial Nova",17),height=1,width=5)
    
    root.mainloop()

mainscreen()
