import tkinter as tk
from tkinter import ttk
from tkinter import Text
from tkinter.constants import RAISED
import MySQLdb as db
from tkinter import messagebox as ms

class BookingWindow(object):
    def __init__(self,parent):
        
        def ConnectBook():
            con = db.connect('localhost', 'root', '', 'gasproject')
            cur = con.cursor()  
            cur.execute('insert into bookingform(CustIdBook,Name,AadharNo,Last_Book)values(NULL,"{a}","{b}","{c}")'.format(a=CustId.get("1.0","end-1c"),b=Name.get("1.0","end-1c"),c=AadharNo.get("1.0","end-1c")))
            con.commit()
            con.close()
            amt = 700
            ms.showinfo("Booking","Booking Successful. Amount Payable is {amt} ".format(amt= amt))
            
#         def Amount():
#             if x.value.get()==1  and m.value.get()==1 :
#                 tk.Label(root,Text="Amount").grid(row=8,column=0)
#                 tk.Label(root,Text="1000").grid(row=8,column=1)
#             elif y.value.get()==2  and m.value.get()== 1 :
#                 tk.Label(root,Text="Amount").grid(row=8,column=0)
#                 tk.Label(root,Text="2000").grid(row=8,column=1)
#             elif n.value.get()==2  and x.value.get()== 1 : 
#                 tk.Label(root,Text="Amount").grid(row=8,column=0)
#                 tk.Label(root,Text="700").grid(row=8,column=1)
#             else :
#                 tk.Label(root,Text="Amount").grid(row=8,column=0)
#                 tk.Label(root,Text="700").grid(row=8,column=1)
                            
        self.parent = root 
        root.title("Booking Window")
        #tk.Label(root,text="BOOKING FORM").grid(row=0,column=1)
        
        tk.Label(root,text="CustomerID").grid(row=1,column=0)
        CustId = Text(height="1",width="45")
        CustId.grid(row=1,column=1,pady=10)
        
        tk.Button(root,text='Search').grid(row=1,column=2)
        tk.Label(root,text="Name").grid(row=2,column=0)
        Name = Text(height="1",width="45")
        Name.grid(row=2,column=1,pady=10)
        
        tk.Label(root,text="Aadhar no").grid(row=3,column=0,pady=10)
        AadharNo = Text(height="1",width="45")
        AadharNo.grid(row=3,column=1,pady=10)
        
        tk.Label(root,text="Type").grid(row=5,column=0,pady=10)
        v2 = tk.IntVar()
        tk.Radiobutton(root,text="Commercial", variable='v2' , value = 1 ).grid(row=5,column=1)
        tk.Radiobutton(root,text="Domestic", variable='v2' , value = 2).grid(row=5,column=2)
        
        
        tk.Label(root,text="Quantity").grid(row=6,column=0,pady=10)
        v1 = tk.IntVar()
        tk.Radiobutton(root,text="One", variable='v1' , value = 1 ).grid(row=6,column=1)
        tk.Radiobutton(root,text="Two", variable='v1' , value = 2).grid(row=6,column=2)
        
        if v1==1:
            a=1
        else:
            a=2
        
        print(a)
        
        tk.Button(root, text='Confirm Booking',command=ConnectBook,relief =RAISED).grid(row=9, column=1)
        tk.Button(root, text='Quit',command=quit,relief =RAISED).grid(row=9, column=2)
        
        tk.Label(root,text="Quantity").grid(row=6,column=0,pady=10)
        
root = tk.Tk()
root.geometry("600x350")
MyBook = BookingWindow(root)
root.mainloop()

