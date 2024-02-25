                                ###########################################
                                #   This file contains login dashboard    #
                                #   for trading bot.                      #
                                #-----------------------------------------#
                                #   written by Onur Oduncu                #
                                #                                         #
                                ###########################################
import sqlite3 as db
from tkinter import *
from tkinter import ttk,messagebox
from db import Sql

class Login:

    def __init__(self) -> None:
        self.__gui = Tk(className=" Binance Trading Bot\t\tLogin Panel")
        self.__gui.iconbitmap('icons/favicon.ico')
        self.__gui.config(bg="black")
        self.__width = 540
        self.__height = 640
        self.__screen_width = self.__gui.winfo_screenwidth()
        self.__screen_height = self.__gui.winfo_screenheight()
        x = (self.__screen_width / 2) - (self.__width / 2)
        y = (self.__screen_height / 2) - (self.__height / 2)
        self.__gui.geometry("%dx%d+%d+%d" % (self.__width, self.__height, x, y))
        self.__gui.resizable(0, 0)
        self.__gui.protocol('WM_DELETE_WINDOW', self.__quit)
        self.__username = StringVar(value="")
        self.__password = StringVar(value="")
        self.__api_key = StringVar(value="")
        self.__api_secret = StringVar(value="")
        self.__user = StringVar(value="Guest")
        self.__exchange = StringVar(value="Binance")
        self.__adminpass = StringVar(value="")
        self.__sql = Sql("login")
        self.__sql.createUserLogin()
        self.__objPanel()

                       
    def getLogin(self):
        return self.__gui
    def getWidth(self):
        return self.__width
    def setWidth(self,newWidth):
        self.__width = newWidth
    def getUsername(self):
        return self.__username.get()
    def __quit(self):
        if messagebox.askyesno("Log Out", "Are you sure?") == True:
            self.__gui.quit()
            exit(0) 
    def getuser(self):
        return self.__user.get()
 
    def __checkmod(self,event):
            if self.__user.get() == "Admin":
                self.__at = ttk.Entry(self.__loginframe2, width=30,foreground="red",textvariable=self.__adminpass,font="Roboto 14",show='*')
                self.__at.place(x=160,y=300,height=40)
                self.__at.focus()
                self.__registerb.config(state=DISABLED)
            else:
                self.__registerb.config(state=NORMAL)
                self.__at.destroy()

    def __checkuser(self):
        if self.__user.get() == "Guest":
            if self.__sql.userExist(self.__username.get(),self.__password.get()):
                self.__success()
            else:
                self.__fail()
        elif self.__user.get() == "Admin" and self.__adminpass.get() == "1234":
            self.__success()
        else:
            self.__fail()
            
    def __success(self):
        messagebox.showinfo("Success","Login successful")
        self.__gui.quit()

    def __fail(self):
        self.__pt.delete(0,"end")
        if self.__user.get() == "Admin":
            self.__at.delete(0,"end")
        messagebox.showerror("Error","The username or password is incorrect")

    def __back(self):
        self.__toplabel.config(text="Login")
        self.__signin.config(text="Login",command=self.__checkuser)
        self.__el.config(text="Exchange:")
        self.__cmb1 = ttk.Combobox(self.__loginframe2,textvariable=self.__exchange,width=35,font="Roboto 12 bold",)
        self.__cmb1.place(x=160,y=180,height=40)
        self.__cmb2 = ttk.Combobox(self.__loginframe2,textvariable=self.__user,width=35,font="Roboto 12 bold",)
        self.__cmb2.place(x=160,y=240,height=40)
        self.__cmb2["values"] = ["Guest","Admin"]
        self.__gl.config(text="User Type:")
        self.__registerb.config(text="Register",command=self.__register)
        self.__gui.title(" Binance Trading Bot\t\tLogin Panel")
        self.__cmb2.bind('<<ComboboxSelected>>', self.__checkmod)

    def __register(self):
        self.__toplabel.config(text="Register")
        self.__signin.config(text="OK",command=self.__insert)
        self.__el.config(text="api_key:")
        self.__apit = ttk.Entry(self.__loginframe2, width=30,foreground="black", textvariable=self.__api_key,font="Roboto 14")
        self.__apit.place(x=160,y=180,height=40)
        self.__keyt = ttk.Entry(self.__loginframe2, width=30,foreground="black", textvariable=self.__api_secret,font="Roboto 14")
        self.__keyt.place(x=160,y=240,height=40)
        self.__gl.config(text="api_secret:")
        self.__registerb.config(text="BACK",command=self.__back)
        self.__gui.title(" Binance Trading Bot\t\tRegister Panel")
    
    def __insert(self):
        if self.__sql.userExist(self.__username.get(),self.__password.get()):
            messagebox.showerror("Error", "Username already exist")
            self.__success()
        elif(len(self.__username.get()) == 0 or len(self.__password.get()) == 0 or len(self.__username.get())>20 or len(self.__password.get())>20) or len(self.__api_key.get()) != 64 or len(self.__api_secret.get()) !=64:
            messagebox.showerror("Error", "Invalid user informations")
            self.__pt.delete(0,"end")
            self.__apit.delete(0,"end")
            self.__ut.delete(0,"end")
            self.__keyt.delete(0,"end")
            self.__ut.focus()
        else:
            self.__sql.insertUserlogin(self.__username.get(),self.__password.get(),self.__api_key.get(),self.__api_secret.get())
            messagebox.showinfo("Success", "User registered")
            self.__success()
            

    def __objPanel(self):
        self.__loginframe1=LabelFrame(self.__gui,bg="white",height=70,width=520,borderwidth=5)
        self.__loginframe1.place(x=10,y=10)
        self.__loginframe2=LabelFrame(self.__gui,bg="gray",height=535,width=520,borderwidth=5)
        self.__loginframe2.place(x=10,y=95)
        self.__toplabel = Label(self.__loginframe1, fg="black", bg="white", anchor="center", text="Login", font="Roboto 25 bold")
        self.__toplabel.place(x=200,y=10)
        self.__ul = Label(self.__loginframe2, fg="black", bg="gray", text="Username:", font="Roboto 14 bold")
        self.__ul.place(x=40,y=60,height=40)
        self.__ut = ttk.Entry(self.__loginframe2, width=30,foreground="black", textvariable=self.__username,font="Roboto 14")
        self.__ut.place(x=160,y=60,height=40)
        self.__ut.focus()
        self.__pl = Label(self.__loginframe2, fg="black", bg="gray", text="Password:", font="Roboto 14 bold")
        self.__pl.place(x=40,y=120,height=40)
        self.__pt = ttk.Entry(self.__loginframe2, width=30, textvariable=self.__password,font="Roboto 14 ",foreground="red",show='*')
        self.__pt.place(x=160,y=120,height=40)
        self.__el = Label(self.__loginframe2, fg="black", bg="gray", text="Exchange:", font="Roboto 14 bold")
        self.__el.place(x=40,y=180,height=40)
        self.__cmb1 = ttk.Combobox(self.__loginframe2,textvariable=self.__exchange,width=35,font="Roboto 12 bold")
        self.__cmb1.place(x=160,y=180,height=40)
        self.__cmb1["values"] = ("Binance")
        self.__gl = Label(self.__loginframe2, fg="black", bg="gray", text="User Type:", font="Roboto 14 bold")
        self.__gl.place(x=40,y=240,height=40)
        self.__cmb2 = ttk.Combobox(self.__loginframe2,textvariable=self.__user,width=35,font="Roboto 12 bold")
        self.__cmb2.place(x=160,y=240,height=40)
        self.__cmb2["values"] = ("Guest","Admin")
        self.__cmb2.bind('<<ComboboxSelected>>', self.__checkmod)  
        self.__signin = Button(self.__loginframe2,width=20, text="Login",bg="black",fg="white",font="Roboto 14 bold",command=self.__checkuser)
        self.__signin.place(x=240,y=390,height=40)
        self.__registerb = Button(self.__loginframe2,width=20, text="Register",bg="black",fg="white",font="Roboto 14 bold",command=self.__register)
        self.__registerb.place(x=240,y=440,height=40)


    def __str__(self) -> str:
        pass

    
def Main():
    login = Login()
    login.getLogin().mainloop()


if __name__ == "__main__":
    Main()