from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Login/Register - Software")
root.geometry("700x400")
def clear():
    tmsg.showinfo("Login","Successfully Logined")
def clear1():
    tmsg.showinfo("Register","Successfully Register")
def log():
    # f2 = Frame(width=700,height=400,bg="#111E6C")
    # f2.pack()
    # loglab = Label(f2,text="Enter Username : ",font="Roboto 20 bold")
    # loglab.place(x=100,y=100)
    # logent = Entry(f2)
    # logent.place(x=150,y=100)
    newwindow = Toplevel(root)
    newwindow.geometry("700x400")
    
    
    f2 = Frame(newwindow,width=700,height=400,bg="#111E6C")
    f2.pack(fill=BOTH,expand=True)
    loglab = Label(newwindow,text="Enter Username : ",font="Roboto 15 bold",bg="#111E6C",fg="white")
    loglab.place(x=100,y=150)
    logent = Entry(newwindow,font="Roboto 10",width=30)
    logent.place(x=350,y=150)
    loglab2 = Label(newwindow,text="Enter Password : ",font="Roboto 15 bold",bg="#111E6C",fg="white")
    loglab2.place(x=100,y=200)
    logent2 = Entry(newwindow,show="***",width=35)
    logent2.place(x=350,y=200)
    logbut = Button(newwindow,text="Login",width=5,height=-10,font="Roboto 15 bold",command=clear)
    logbut.place(x=440,y=270)
    newwindow1.destroy()
    
    
    
def reg():
    newwindow2 = Toplevel(root)
    newwindow2.geometry("700x400")
    
    
    f2 = Frame(newwindow2,width=700,height=400,bg="#111E6C")
    f2.pack()
    reglab = Label(newwindow2,text="Enter Username : ",font="Roboto 15 bold",bg="#111E6C",fg="white")
    reglab.place(x=100,y=100)
    regent = Entry(newwindow2,font="Roboto 10",width=30)
    regent.place(x=350,y=100)
    reglab2 = Label(newwindow2,text="Enter Password : ",font="Roboto 15 bold",bg="#111E6C",fg="white")
    reglab2.place(x=100,y=150)
    regent2 = Entry(newwindow2,show="***",width=35)
    regent2.place(x=350,y=200)
    # regent2.place(x=350,y=100)
    reglab3 = Label(newwindow2,text="Confirm Password : ",font="Roboto 15 bold",bg="#111E6C",fg="white")
    reglab3.place(x=100,y=200)
    regent3 = Entry(newwindow2,show="***",width=35)
    regent3.place(x=350,y=150)
    regbut = Button(newwindow2,text="Regsiter",width=10,height=-10,font="Roboto 15 bold",command=clear1)
    regbut.place(x=440,y=300)
    
    
f1 = Frame(root,width=700,height=400,bg="#111E6C")
f1.pack()
logb1 = Button(text="Login",width=15,height=-4,font="Roboto 20 bold",command=log)
logb1.place(x=250,y=100)
logb2 = Button(text="Register",width=15,height=-4,font="Roboto 20 bold",command=reg)
logb2.place(x=250,y=200)




root.mainloop()