                                        ###########################################
                                        #   This file contains user dashboard     #
                                        #   for trading bot.                      #
                                        #-----------------------------------------#
                                        #   written by Onur Oduncu                #
                                        #                                         #
                                        ###########################################

import sqlite3 as db
from tkinter import messagebox,ttk
from datetime import datetime
from userLogin import Login
from PIL import ImageTk
import PIL.Image
import time
from parity import Chart
from tkinter import * 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#class User(Login):
class User():
    def __init__(self):
        #Login.__init__(self)
        #self.getLogin().mainloop()
        #self.getLogin().state('withdraw')
        self.__gui = Tk(className=" Stock Market Trade Bot")
        self.__gui.config(bg="black") ##eff5f6
        """self.__width= self.__gui.winfo_screenwidth()               
        self.__height= self.__gui.winfo_screenheight()               
        self.__gui.geometry("%dx%d" % (self.__width, self.__height))
        self.__gui.attributes('-fullscreen', True)
        self.__gui.resizable(0, 0)"""
        self.__gui.iconbitmap('icons/favicon.ico')
        """icon = PhotoImage(file="")
        self.__gui.iconphoto(True,icon)"""
        self.__gui.geometry("1920x1080")
        self.__gui.state("zoomed")
        self.__gui.bind('<Escape>',self.__quit)
        self.__gui.protocol('WM_DELETE_WINDOW', self.__quit2)
        self.__gui.resizable(0, 0)
        self.__sidebar = Frame(self.__gui,bg = "white")
        self.__sidebar.place(x=3,y=3,width=250,height=837)

        self.__bodyFrame1 = Frame(self.__gui,bg="white")
        self.__bodyFrame1.place(x=267, y=8,width=300,height=662)
        self.__indLabel1 = Label(self.__bodyFrame1,bg="black",fg="white",text="Crypto Data\n-----------------",font=("", 12, "bold"))
        self.__indLabel1.place(x=5,y=8)

        self.__bodyFrame7 = Frame(self.__gui,bg="white")
        self.__bodyFrame7.place(x=587, y=8,width=300,height=662)
        self.__indLabel7 = Label(self.__bodyFrame7,bg="black",fg="white",text="Stock Market Data\n-----------------",font=("", 12, "bold"))
        self.__indLabel7.place(x=5,y=8)

        self.__bodyFrame8 = Frame(self.__gui,bg="white")
        self.__bodyFrame8.place(x=907, y=8,width=300,height=662)
        self.__indLabel8 = Label(self.__bodyFrame8,bg="black",fg="white",text="Global Market Data\n----------------------",font=("", 12, "bold"))
        self.__indLabel8.place(x=5,y=8)
        #PNR
        self.__bodyFrame2 = Frame(self.__gui,bg="white")
        self.__bodyFrame2.place(x=267, y=680,width=300,height=155)
        self.__indLabel2 = Label(self.__bodyFrame2,bg="black",fg="white",text="PNR\n-----------------",font=("", 12, "bold"))
        self.__indLabel2.place(x=5,y=8)
        #Prediction
        self.__bodyFrame3 = Frame(self.__gui,bg="white")
        self.__bodyFrame3.place(x=587, y=680,width=300,height=155)
        self.__preLabel = Label(self.__bodyFrame3,bg="black",fg="white",text="Prediction\n-----------------",font=("", 12, "bold"))
        self.__preLabel.place(x=5,y=8)
        self.__prehigh = Label(self.__bodyFrame3,bg="green",fg="white",text="High : ",font=("", 14, "bold"))
        self.__prehigh.place(x=5,y=68)
        self.__prelow = Label(self.__bodyFrame3,bg="red",fg="white",text="Low : ",font=("", 14, "bold"))
        self.__prelow.place(x=5,y=108)
        #Bot status
        self.__bodyFrame4 = Frame(self.__gui,bg="white")
        self.__bodyFrame4.place(x=907, y=680,width=300,height=155)
        self.__botLabel = Label(self.__bodyFrame4,bg="black",fg="white",text="Bot Status\n-----------------",font=("", 12, "bold"))
        self.__botLabel.place(x=5,y=8)
        self.__botBuy = Label(self.__bodyFrame4,bg="green",fg="white",text="Buy : ",font=("", 14, "bold"))
        self.__botBuy.place(x=5,y=68)
        self.__botSell = Label(self.__bodyFrame4,bg="red",fg="white",text="Sell : ",font=("", 14, "bold"))
        self.__botSell.place(x=5,y=108)
        #Overall Indicator Status
        self.__bodyFrame5 = Frame(self.__gui,bg="white")
        self.__bodyFrame5.place(x=1227, y=680,width=300,height=155)
        self.__staLabel = Label(self.__bodyFrame5,bg="black",fg="white",text="Overall Indicator Status\n\
------------------------------------",font=("", 12, "bold"))
        self.__staLabel.place(x=5,y=8)
        self.__staBuy = Label(self.__bodyFrame5,bg="green",fg="white",text="Buy : ",font=("", 14, "bold"))
        self.__staBuy.place(x=5,y=68)
        self.__staSell = Label(self.__bodyFrame5,bg="red",fg="white",text="Sell : ",font=("", 14, "bold"))
        self.__staSell.place(x=5,y=108)
        #indicators
        self.__bodyFrame6 = Frame(self.__gui,bg="white")
        self.__bodyFrame6.place(x=1227, y=8,width=300,height=662)
        self.__indLabel6 = Label(self.__bodyFrame6,bg="black",fg="white",text="Indicators\n-----------------",font=("", 12, "bold"))
        self.__indLabel6.place(x=5,y=8)

        self.__logoImage = PIL.Image.open("icons/admin.png")
        photo = ImageTk.PhotoImage(self.__logoImage)
        self.__logo = Label(self.__sidebar,image=photo,bg="white")
        self.__logo.image = photo
        self.__logo.place(x=25,y=60)
        self.__brandname = Label(self.__sidebar,text="Admin",bg="black",fg="white",font=("",15,"bold"))
        self.__brandname.place(x=94,y=270)
        #dashboard
        self.__dashboardImage = ImageTk.PhotoImage(file='icons/dashboard-icon.png')
        self.__dashboard = Label(self.__sidebar, image=self.__dashboardImage, bg='#ffffff')
        self.__dashboard.place(x=40, y=350)
        self.__dashboard_text = Button(self.__sidebar, text="Dashboard", bg='#eff5f6', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.__dashboard_text.place(x=80, y=350)

        # Manage
        self.__manageImage = ImageTk.PhotoImage(file='icons/manage-icon.png')
        self.__manage = Label(self.__sidebar, image=self.__manageImage, bg='#ffffff')
        self.__manage.place(x=40, y=390)

        self.__manage_text = Button(self.__sidebar, text="Manage", bg='#eff5f6', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.__manage_text.place(x=80, y=395)

        # Settings
        self.__settingsImage = ImageTk.PhotoImage(file='icons/settings-icon.png')
        self.__settings = Label(self.__sidebar, image=self.__settingsImage, bg='#ffffff')
        self.__settings.place(x=40, y=440)

        self.__settings_text = Button(self.__sidebar, text="Settings", bg='#eff5f6', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.__settings_text.place(x=80, y=440)

        # Exit
        self.__ExitImage = ImageTk.PhotoImage(file='icons/exit-icon.png')
        self.__Exit = Label(self.__sidebar, image=self.__ExitImage, bg='#ffffff')
        self.__Exit.place(x=25, y=780)

        self.__Exit_text = Button(self.__sidebar, text="Exit", bg='#eff5f6', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff',command=self.__quit2)
        self.__Exit_text.place(x=80, y=790)

        # date and Time
        self.__clock_image = ImageTk.PhotoImage(file="icons/time.png")
        self.__date_time_image = Label(self.__sidebar, image=self.__clock_image, bg="white")
        self.__date_time_image.place(x=50, y=20)

        self.__date_time = Label(self.__gui, bg='#eff5f6')
        self.__date_time.place(x=90, y=15)
        self.__show_time()

    def __show_time(self):
        self.__time = time.strftime("%H:%M:%S")
        self.__date = time.strftime('%Y/%m/%d')
        self.__set_text = f"  {self.__date} \n {self.__time}"
        self.__date_time.configure(text=self.__set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.__date_time.after(100, self.__show_time)
        #self.__userDashboard()

    def __AdminStart(self):
        self.__username = "onur"

    def __UserStart(self):
        pass

    def getUser(self):
        return self.__gui

    def __quit(self,event):
        if messagebox.askyesno("Log Out", "Are you sure?") == True:
            #self.getLogin().quit()
            self.__gui.quit()
            exit(0)
    def __quit2(self):
        if messagebox.askyesno("Log Out", "Are you sure?") == True:
            #self.getLogin().quit()
            self.__gui.quit()
            exit(0)

    """def plot(self,screen,frame):
        (x,y) = frame
        fig = Figure(figsize = (5, 5),dpi = 100)  
        plot1 = fig.add_subplot(221)
        plot1.plot(x,y)
        canvas = FigureCanvasTkAgg(fig,master = screen)  
        canvas.draw()
        canvas.get_tk_widget().pack()"""
    
    """def animate(self,frame):
        plt.cla()
        plt.plot(frame.index,frame.Close)
        plt.xlabel('Time')
        plt.ylabel('Open')
        plt.title("BTCUSDT15m")
        plt.gcf().autofmt_xdate()
        plt.tight_layout()"""







def Main():
    login = User()
    login.getUser().mainloop()

if __name__ == "__main__":
    Main()