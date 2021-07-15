from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from PG import *


def dataregister():
    
    baseid = datainfo1.get()
    username = datainfo2.get()
    password = datainfo3.get()
    domain = datainfo4.get()
    domain = domain.capitalize()
    
    insertData = "insert into "+datatable+" values('"+baseid+"','"+username+"','"+password+"','"+domain+"')"
    try:
        cur.execute(insertData)
        con.commit()
        messagebox.showinfo('Success',"Data added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(baseid)
    print(username)
    print(password)
    print(domain)


    root.destroy()
    
def adddata(): 
    
    global datainfo1,datainfo2,datainfo3,datainfo4,Canvas1,con,cur,datatable,root
    
    root = Tk()
    root.title("ADDING NEW ENTRY")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mypass = "root"
    mydatabase="pgwdbm"

    con = pymysql.connect(host="localhost",user="Amol",password=mypass,database=mydatabase)
    cur = con.cursor()

    datatable = "pgwdbm" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Data", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
        
    
    lb1 = Label(labelFrame,text="Base Id : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    datainfo1 = Entry(labelFrame)
    datainfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        

    lb2 = Label(labelFrame,text="Username : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    datainfo2 = Entry(labelFrame)
    datainfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        

    lb3 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    datainfo3 = Entry(labelFrame)
    datainfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        

    lb4 = Label(labelFrame,text="Domain : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    datainfo4 = Entry(labelFrame)
    datainfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
    
    Pass_Gen=Button(root,text="GENERATE PASSWORD",bg='#d1ccc0', fg='black',command=PasswordGen)
    Pass_Gen.place(relx=0.38,rely=0.8, relwidth=0.25,relheight=0.08)
 
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=dataregister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
        
    root.mainloop()