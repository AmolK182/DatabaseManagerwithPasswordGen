from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "root"
mydatabase="pgwdbm"

con = pymysql.connect(host="localhost",user="Amol",password=mypass,database=mydatabase)
cur = con.cursor()


datatable = "pgwdbm" 


def deletedata():
    
    baseid = datainfo1.get()
    
    deleteSql = "delete from "+datatable+" where baseid = '"+baseid+"'"

    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Database Deleted Successfully")
    except:
        messagebox.showinfo("Please check the  Database")
    

    print(baseid)

    datainfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global datainfo1,datainfo2,datainfo3,datainfo4,Canvas1,con,cur,datatable,root
    
    root = Tk()
    root.title("H11 CWP Project")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="White")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="Blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Database", bg='Yellow', fg='Black', font=('Arial Black',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
   
    lb2 = Label(labelFrame,text="Database", bg='Green', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    datainfo1 = Entry(labelFrame)
    datainfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="SUBMIT",bg='Red', fg='black',command=deletedata)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='Red', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()