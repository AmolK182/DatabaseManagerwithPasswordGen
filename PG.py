from tkinter import *
import random, string
import pyperclip


    

def PasswordGen():    
    root =Tk()
    root.geometry("600x500")
    root.resizable(0,0)
    root.title("PASSWORD GENERATOR")
    Canvasp = Canvas(root)
    Canvasp.config(bg="#1e1111")
    Canvasp.pack(expand=True,fill=BOTH)


    heading = Label(root, text = 'PASSWORD GENERATOR_H11 ' ,font ='arial 15 bold')
    heading.place(relx=0.19,rely=0.15, relwidth=0.65,relheight=0.1)

    pass_label = Label(root, text = 'PASSWORD LENGTH=12', font = 'arial 12 bold').pack()

    pass_str = StringVar()
    
    def Generator():
        password = ''
        for x in range (0,12):
            password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)        
        pass_str.set(password)
    
    
    

    b1=Button(root, text = "GENERATE PASSWORD" , font = 'arial 12 bold', command = Generator)
    b1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    def Copy_password():
        pyperclip.copy(pass_str.get())


    

    b2=Button(root, text = 'COPY TO CLIPBOARD', font = 'arial 12 bold', command = Copy_password)
    b2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)

    root.mainloop()
















