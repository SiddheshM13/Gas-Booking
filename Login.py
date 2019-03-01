import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import MySQLdb as ms

class LoginFrame():
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Frame")
        self.label_username = Label(self.root, text="Username")
        self.label_password = Label(self.root, text="Password")
        self.entry_username = Entry(self.root)
        self.entry_password = Entry(self.root, show="*")
        self.entry_username.focus()
        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.logbtn = Button(self.root, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(row = 2, column = 0)
        self.regbtn = Button(self.root, text = "Return", command = self.ret)
        self.regbtn.grid(row = 2, column = 1)
        self.entry_password.bind("<Return>",self._login_btn_clicked)
        self.root.mainloop()
        
    def ret(self):
        self.root.destroy()
        from StartupFinal import StartPage
        
    def _login_btn_clicked(self,event = None):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username and password:
            db = ms.connect(host="localhost", user="root", passwd="", db="gasproject")
            cursor = db.cursor()
            sql = "SELECT name,password FROM registrationform WHERE name = '{username}'".format(username=username)
            cursor.execute(sql)
            conn = cursor.fetchone()
            if username == conn[0] and password == conn[1]:
                tm.showinfo("login", "Logged in successfully")
                self.root.destroy()
                from BookingFinal import BookingWindow
                
            else:
                tm.showerror("Error", "Invalid Username or password")
        elif not (username or password):
            tm.showerror("Error","Empty username or password field")
            
LoginFrame()