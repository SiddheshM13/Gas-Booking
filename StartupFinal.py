import tkinter as tk

class StartPage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gas Booking")
        self.root.geometry("5000x6000")
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        
        from PIL import Image, ImageTk
        image1=Image.open(r'1.jpg')
        img = ImageTk.PhotoImage(image1)
        w = 360
        h = 455
                
        self.root.geometry("%dx%d" % (w,h))
        self.panel = tk.Label(self.root, image=img)
        self.panel.grid(row=5,column=0)
        self.panel.image = img
       
        tk.Label(self.frame,text='BHARAT GAS',fg='red',font='Arial 14 bold underline').grid(row=1,column=1)
        tk.Label(self.frame,text='BOOKING SYSTEM',fg='red',font='Arial 14 bold underline').grid(row=2,column=1)
        tk.Button(self.frame,text='Quit',command=quit,fg='green',font='Arial').grid(row=3,column=0, pady=10)  
        tk.Button(self.frame,text="Register",command=self.register,fg='green',font='Arial').grid(row=3,column=1)
        tk.Button(self.frame,text='Login',command=self.login,fg='green',font='Arial').grid(row=3,column=2)
        self.root.mainloop()
    def login(self):
        self.root.destroy()
        from LoginFinal import LoginFrame
    
    def register(self):
        self.root.destroy()
        from RegisterFinal import RegistrationWindow

    def hide(self):
        self.root.withdraw()
        
    def show(self):
        self.root.update()
        self.root.deiconify()
            
if __name__== "__main__":
    
    StartPage()
