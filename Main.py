from tkinter import *
from PIL import ImageTk
import pymysql
from AddData import *
from DeleteData import *
from ViewData import *
from gui import *
from PG import *
def cheak():
    if main_pass.get()=="CWPH11":
        my_new()
    else:
        messagebox.showinfo('Failed','Please check the  Password')
first_window=Tk()
first_window.title("SECURITY CHECK")
first_window.geometry("600x500")
Canvask = Canvas(first_window)
Canvask.config(bg="#1e1111")
Canvask.pack(expand=True,fill=BOTH)
l2=Label(first_window,text="PLEASE ENTER THE MASTER PASSWORD", font= ' calibri 15 bold')
l2.place(relx=0.19,rely=0.2, relwidth=0.65,relheight=0.1)
main_pass=StringVar()
e = Entry(first_window,textvariable=main_pass,borderwidth=5)
e.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
bt=Button(first_window,text="VERIFY",command=cheak,font="arial 15 bold")
bt.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

def my_new():
    first_window.destroy()
    mypass = "root"
    mydatabase="pgwdbm"
    
    con = pymysql.connect(host="localhost",user="Amol",password=mypass,database=mydatabase)
    cur = con.cursor()
    
    root = Tk()
    root.title("H11_CWP_PROJECT")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#1e1111")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#ed0400",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    
    
    headingLabel = Label(headingFrame1, text=" Welcome to H11 CWP Project ", bg='black', fg='white', font=('Arial',17,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Add New Entry",bg='black', fg='white', font='arial 12 bold',command=New_Entry)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    btn2 = Button(root,text=" Delete Data ",bg='black', fg='white',font='arial 12 bold', command=delete)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1) 
    btn3 = Button(root,text="Show Database",bg='black', fg='white',font='arial 12 bold', command=View)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn6=Button(root,text="Exit ",bg="black",fg="white",command=root.destroy,font='arial 11 bold')
    btn6.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)
    root.mainloop()
first_window.mainloop()