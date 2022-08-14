import tkinter as tk 
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk
import pymysql

master = tkinter.Tk()
master.title('IMMUNIZATION SCHEDULER')
master.geometry("1000x1200")

rough=tkinter.Label(master, text = "                          ", anchor= "center", font = ("HELVETICA", 15)).grid(column = 0, row = 0)

h=tkinter.Label(master, text = "WELCOME TO", anchor= "center", font = ("Times New roman", 20)).grid(column = 1, row = 0)
h=tkinter.Label(master, text = "IMMUNIZATION",  font = ("Times New roman", 19)).grid(column = 2, row = 0)
p=tkinter.Label(master, text = "SCHEDULER",anchor= "center",font = ("Times New roman", 21)).grid(column = 3, row = 0)
l=tkinter.Label(master, text = "            ", anchor= "center", font = ("Times New roman", 15)).grid(column =2, row = 3)
#savetolist
g=tkinter.Label(master, text = "Select Your Child's Age :", font = ("Times New roman", 12)).grid(column = 1, row = 1, padx = 10, pady = 25) 

def ck():
    db=pymysql.connect('localhost','root','1234','test1')
    c=db.cursor()
    ok=n.get()

    
    if ok=="0 month":
        c.execute("select * from month0")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master,justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)
           
    if ok=="1 month":
        c.execute("select * from month1")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master,justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master,justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)



    if ok=="2 months":
        c.execute("select * from months2")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master,justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                scrollbar = tk.Scrollbar(orient="horizontal")
                
                e =ttk.Entry(master, justify="center",width=20,xscrollcommand="scrollbar.set",font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)
                #scrollbar.grid()
                #scrollbar.config(command=e.xview)  
                #row=i+4,column=j


                    
    if ok=="3 months":
        c.execute("select * from month3")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master,justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+5, column=j)

                    
    if ok=="5-6 months":
        c.execute("select * from month6")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master,justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master,justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

    if ok=="8-9 months":
        c.execute("select * from month9")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master,justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master,justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

                    
    if ok=="11-12 months":
        c.execute("select * from month12")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center",width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master, justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

                    
    if ok=="14-15 months":
        c.execute("select * from month15")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master,justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master,justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

                    
    if ok=="16-18 months":
        c.execute("select * from month16")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master, justify="center",width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

    if ok=="3-6 years":        
        c.execute("select * from year4")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master,justify="center",width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=i3, column=j)
                e =ttk.Entry(master, justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)


    if ok=="8-11 years":
        c.execute("select * from year9")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master, justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

                    
    if ok=="14-16 years":
        cur.execute("select * from year9")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center", width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master, justify="center",width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

                    
    if ok=="17-18 years":
        c.execute("select * from year9")
        l=c.fetchall()
        total_rows = len(l)
        total_columns = len(l[0])
        V=[" NO."," Age","Name","Doses","Content Tag","Price"]
        for i in range(total_rows):
            for j in range(total_columns):
                f =ttk.Entry(master, justify="center",width=20, font=('Arial',12,'bold'))
                f.insert(0,V[j])
                f.grid(row=3, column=j)
                e =ttk.Entry(master, justify="center", width=20, font=('Arial',12))
                e.insert(0,l[i][j])
                e.grid(row=i+4, column=j)

agechoosen = ('0 month',
              '1 month',
              '2 months',
              '3 months ',
              '5-6 months',
              '8-9 months',
              '11-12 months',
              '14-15 months',
              '16-18 months',
              '3-6 years',
              '8-11 years',
              '14-16 years',
              '17-18 years')


n = tkinter.StringVar()
n.set(agechoosen[0])
menu = ttk.OptionMenu(master,n, *agechoosen,)
menu.grid(column = 2, row = 1)
submits=ttk.Button(master, text="SUBMIT", command=ck).grid(column=2,row=2)

master.mainloop() 
