from tkinter import *
from AddData import *

def New_Entry():
    new_window =Tk()
    Canvas1 = Canvas(new_window)
    Canvas1.config(bg="#212F3C")
    Canvas1.pack(expand=True,fill=BOTH)
    new_window.geometry("600x500")
    new_window.title("ADDING NEW ENTRY")
    l0=Label(new_window,text="SELECT A DOMAIN", font= ' arial 15 bold')
    l0.place(relx=0.28,rely=0.0, relwidth=0.45,relheight=0.07)
    l1=Label(new_window,text="Website", font= ' arial 9 bold')
    l1.place(relx=0.28,rely=0.07, relwidth=0.45,relheight=0.07)
    btn1=Button(new_window,text=">>>>>",command=adddata,bg='#FFBB00',fg='red',font='bold')
    btn1.place(relx=0.28,rely=0.14, relwidth=0.45,relheight=0.07)

    l2=Label(new_window,text="Gmail / App", font= ' arial 12 bold')
    l2.place(relx=0.28,rely=0.21, relwidth=0.45,relheight=0.07)

    btn2=Button(new_window,text=">>>>>",command=adddata,bg='#FFBB00',fg='red',font='bold')
    btn2.place(relx=0.28,rely=0.28, relwidth=0.45,relheight=0.07)

    l3=Label(new_window,text="Contacts", font= ' arial 12 bold')
    l3.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.07)

    btn3=Button(new_window,text=">>>>>",command=adddata,bg='#FFBB00',fg='red',font='bold')
    btn3.place(relx=0.28,rely=0.42, relwidth=0.45,relheight=0.07)

    l4=Label(new_window,text="Important Details", font= ' arial 12 bold')
    l4.place(relx=0.28,rely=0.49, relwidth=0.45,relheight=0.07)

    btn4=Button(new_window,text=">>>>>",command=adddata,bg='#FFBB00',fg='red',font='bold')
    btn4.place(relx=0.28,rely=0.56, relwidth=0.45,relheight=0.07)

    l5=Label(new_window,text="Go to main window", font= ' arial 12 bold')
    l5.place(relx=0.28,rely=0.63, relwidth=0.45,relheight=0.1)

    btn5=Button(new_window,text="<<<<<",command=new_window.destroy,bg='#FFBB00',fg='red',font='bold')
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

