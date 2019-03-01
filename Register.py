import tkinter as tk
from tkinter import ttk
from tkinter import Text
from tkinter import Entry
from tkinter.constants import RAISED, DISABLED
from tkinter import filedialog
import MySQLdb as db
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import IntVar  
from tkinter import messagebox  
import PIL.Image
import base64
from PIL import Image

class RegistrationWindow(object):        
    def __init__(self,parent):
        
        def connectionForm():
            con = db.connect('localhost', 'root', '', 'gasproject')
            cur = con.cursor()  
            cur.execute('insert into registrationform(Name,Password,AadharNo,CustPhone,Email,PriAddress,DelAdress)values("{a}","{p}","{b}","{c}","{d}","{e}","{f}")'.format(a=CustName.get("1.0","end-1c"),p=PasswordField.get(),b=AadharNo.get("1.0","end-1c"),c=CustPhone.get("1.0","end-1c"),d=e3.get("1.0","end-1c"),e=PrimAddress.get("1.0","end-1c"),f=DeliveryAddress.get("1.0","end-1c")))
            con.commit()
            con.close()
        
        def DocumentUpload1():            
            doc1 = filedialog.askopenfile(parent=root , mode='rb') 
             
        def DocumentUpload2():
            doc2 = filedialog.askopenfile(parent=root , mode='rb')
#             image2 = Image.open(doc2)
#             blob_value2 = open(image2, 'rb').read()
#             
#             
#         def CheckFields():
#                 if len(CustName.get("1.0","end-1c") and AadharNo.get("1.0","end-1c") and CustPhone.get("1.0","end-1c") and e3.get("1.0","end-1c") and PrimAddress.get("1.0","end-1c") and DeliveryAddress.get("1.0","end-1c")) == 0:
#                     tk.messagebox.showinfo("Warning!", "Box is empty! Complete the information")
#                 else:
#                     SubmButton.config(state = 'ENABLED')
#                              
        self.parent = root
        root.title(" Customer Registration Form")
        
        tk.Label(root,text="Name : ").grid(row=0,column=0)
        CustName = Text(height="1",width="45")
        CustName.grid(row=0,column=1,pady=10)
       
        tk.Label(root,text = "Password : ").grid(row=1,column=0)
        PasswordField =Entry(width = '60',show="*")
        PasswordField.grid(row=1,column=1,pady=10,sticky=tk.W) 
        tk.Label(root,text="Aadhar No : ").grid(row=2,column=0)
        AadharNo = Text(height="1",width="45")
        AadharNo.grid(row=2,column=1,pady=10)
         
        tk.Label(root,text="Contact No : ").grid(row=3,column=0)
        CustPhone  = Text(height="1",width="45")
        CustPhone.grid(row=3,column=1,pady=10)
        
        tk.Label(root, text='Email Address: ').grid(row=4, column=0)
        e3 = Text(height="1",width="45")
        e3.grid(row=4, column=1,pady=10)
        
        tk.Label(root, text="Primary Address:  ").grid(row=5,column=0)
        PrimAddress = Text(height="5",width="45")
        PrimAddress.grid(row=5,column=1,pady=10)
        
        tk.Label(root, text="Correspondence Address:  ").grid(row=6,column=0)
        DeliveryAddress = Text(height="5",width="45")
        DeliveryAddress.grid(row=6,column=1,pady=10)
    
        tk.Label(root ,text="Documents for Proof of Address:").grid(row=7,column=0)
        elements = ["Ration Card","Electricity Bill(Within Last Three Months)","Landline Telephone Bill(Within Last Three Months)","Passport","Employer's Certificate","Flat allotment / possession letter from Builder","House registration papers /Property Tax Document","LIC policy","Voter’s Identity Card","Registered Leave and License Document","Driving License","Bank Passbook"]
        combobox = ttk.Combobox(root, values=elements)
        combobox.current(0) 
        combobox.grid(row=7 , column=1)
        tk.Button(root, text='Choose a File', relief = RAISED , command=DocumentUpload1).grid(row=7, column=2)
            
                
        tk.Label(root ,text="Documents for Proof of Identity:").grid(row=8,column=0)
        elements1 = ["PAN Card","Passport","Voter’s Identity Card","Driving License","Central/State Government Issued ID cards","Bank Passbook with Photograph"]
        combobox = ttk.Combobox(root, values=elements1)
        combobox.current(0) 
        combobox.grid(row=8, column=1)
        tk.Button(root, text='Choose a File', relief = RAISED , command=DocumentUpload2).grid(row=8, column=2)
        
#         var1 = IntVar() 
#         tk.Checkbutton(root,text='Agree to the terms and conditions',variable=var1,command =CheckFields).grid(row=10, column=0) 
        tk.Button(root, text='Quit',command=quit,relief =RAISED).grid(row=11, column=1)   
        SubmButton = tk.Button(root, text='Submit', command=connectionForm, relief = RAISED ).grid(row=11, column=2)
        #tk.Button(root, text='ImageCheck', command=ImageUpload, relief = RAISED).grid(row=11, column=3)
              
    

root = tk.Tk()
root.geometry("800x500")
MyApp = RegistrationWindow(root)
root.mainloop()
    