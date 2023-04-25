import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 

cID = ""
prodList = []
quantList = []


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Login, SignUpIntro, SignUpCustomer, SignUpAdmin, SignUpSupplier, SignUpComplete, LoginCustomer, LoginAdmin, LoginSupplier, Membership, ListOfProducts, EditAddCustomerInformation, ShoppingCart):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Login)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART", font=('Arial',40))
        label.pack(padx=20,pady=20)
        label = tk.Label(self, text = "Login", font=('Arial', 16))
        label.pack(padx=100,pady=100)

        label = tk.Label(self, text = "Username", font=('Arial', 14))
        label.place(x=350, y=335)

        options = [
            "Customer",
            "Admin",
            "Supplier"
        ]

        clicked = tk.StringVar(self)
        clicked.set("Customer")


        label = tk.Label(self, text = "Login As", font=('Arial', 14))
        label.place(x=350, y=270)

        drop = tk.OptionMenu( self , clicked , *options)
        drop.place(x=500,y=270)

        def retrieve_input():
            inputName=textBox1.get()
            inputPwd=textBox2.get()
            accType = clicked.get()

        
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')

            if(conn):
                print('connection successful')

            else:
                print('connection failed')

            mycursor = conn.cursor()
            inputName = '"'+inputName+'"'
            inputPwd = '"'+inputPwd+'"'
            accType = '"'+accType+'"'

            global cID
            Result = mycursor.execute('Select ReferenceID from Login where Username = '+inputName+' AND Password ='+inputPwd+' AND Acc_Type ='+accType)
            Result = mycursor.fetchone()

            mycursor.execute('Select * from Login where Username = '+inputName+' AND Password = '+inputPwd+' AND Acc_Type ='+accType)

            myresult = mycursor.fetchall()
            if myresult:
                cID = Result[0]
                print('Login Succesful')
                if clicked.get() == "Customer":
                    controller.show_frame(LoginCustomer)
                elif clicked.get() == "Admin":
                    controller.show_frame(LoginAdmin)
                elif clicked.get() == "Supplier":
                    controller.show_frame(LoginSupplier)
            else:
                messagebox.showerror("Invalid", "Invalid Credentials")

            #Handle login pages
        textBox1=tk.Entry(self,width=20)
        textBox1.place(x=500,y=342)

        label = tk.Label(self, text = "Password", font=('Arial', 14))
        label.place(x=350, y=400)

        textBox2=tk.Entry(self,width=20, show="*")
        textBox2.place(x=500,y=405)

        buttonCommit=tk.Button(self, height=1, width=10, text="Login", 
                    command=lambda: retrieve_input())

        buttonCommit.place(x=450, y=500)

        label = tk.Label(self, text = "Not a Member? Sign up!", font=('Arial', 14))
        label.place(x=200, y=600)

        buttonCommit=tk.Button(self, height=1, width=10, text="SignUp", 
                    command=lambda: controller.show_frame(SignUpIntro))
        buttonCommit.place(x=550, y=600)

class SignUpIntro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART - Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Account Type", font=('Arial', 14))
        label.place(x=350, y=270)

        options = [
            "Customer",
            "Admin",
            "Supplier"
        ]

        clicked = tk.StringVar(self)
        clicked.set("Customer")

        drop = tk.OptionMenu(self, clicked , *options)
        drop.place(x=500,y=270)

        def retrieve_input():
            accType = clicked.get()
            if accType == "Customer":
                controller.show_frame(SignUpCustomer)
            elif accType == "Admin":
                controller.show_frame(SignUpAdmin)
            elif accType == "Supplier":
                controller.show_frame(SignUpSupplier)

        buttonCommit = tk.Button(self, height=1, width=10, text="Continue",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=400)

class SignUpCustomer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="AMZKART - Customer Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Personal Details", font=('Arial', 15))
        label.place(x=250, y=125)
        
        label = tk.Label(self, text = "Create Username", font=('Arial', 10))
        label.place(x=350, y=175)

        textBox1=tk.Entry(self,width=20)
        textBox1.place(x=550,y=175)

        label = tk.Label(self, text = "Create Password", font=('Arial', 10))
        label.place(x=350, y=200)

        textBox2=tk.Entry(self,width=20, show="*")
        textBox2.place(x=550,y=200)

        label = tk.Label(self, text = "First Name", font=('Arial', 10))
        label.place(x=350, y=225)

        textBox3=tk.Entry(self,width=20)
        textBox3.place(x=550,y=225)

        label = tk.Label(self, text = "Last Name", font=('Arial', 10))
        label.place(x=350, y=250)

        textBox4=tk.Entry(self,width=20)
        textBox4.place(x=550,y=250)

        label = tk.Label(self, text = "Phone", font=('Arial', 10))
        label.place(x=350, y=275)

        textBox5=tk.Entry(self,width=20)
        textBox5.place(x=550,y=275)

        label = tk.Label(self, text = "Email", font=('Arial', 10))
        label.place(x=350, y=300)

        textBox6=tk.Entry(self,width=20)
        textBox6.place(x=550,y=300)

        label = tk.Label(self, text = "Add Primary Delivery Address", font=('Arial', 15))
        label.place(x=250, y=335)

        label = tk.Label(self, text = "Street Address", font=('Arial', 10))
        label.place(x=350, y=385)

        textBox7=tk.Entry(self,width=20)
        textBox7.place(x=550,y=385)

        label = tk.Label(self, text = "City", font=('Arial', 10))
        label.place(x=350, y=410)

        textBox8=tk.Entry(self,width=20)
        textBox8.place(x=550,y=410)

        label = tk.Label(self, text = "Postal Code", font=('Arial', 10))
        label.place(x=350, y=435)

        textBox9=tk.Entry(self,width=20)
        textBox9.place(x=550,y=435)

        label = tk.Label(self, text = "Country", font=('Arial', 10))
        label.place(x=350, y=460)

        textBox10=tk.Entry(self,width=20)
        textBox10.place(x=550,y=460)

        label = tk.Label(self, text = "Add Primary Debit/Credit Card", font=('Arial', 15))
        label.place(x=250, y=495)

        label = tk.Label(self, text = "Card Number", font=('Arial', 10))
        label.place(x=350, y=545)

        textBox11=tk.Entry(self,width=20)
        textBox11.place(x=550,y=545)

        label = tk.Label(self, text = "Card Expiry Date", font=('Arial', 10))
        label.place(x=350, y=570)

        textBox12=tk.Entry(self,width=20)
        textBox12.place(x=550,y=570)

        label = tk.Label(self, text = "CVV/Pin", font=('Arial', 10))
        label.place(x=350, y=595)

        textBox13=tk.Entry(self,width=20)
        textBox13.place(x=550,y=595)

        def retrieve_input():

            Username = '"'+textBox1.get()+'"'
            Password = '"'+textBox2.get()+'"'
            Fname  = '"'+textBox3.get()+'"'
            Lname = '"'+textBox4.get()+'"'
            Phone = '"'+textBox5.get()+'"'
            Email = '"'+textBox6.get()+'"'
            Address = '"'+textBox7.get()+'"'
            City = '"'+textBox8.get()+'"'
            Pcode = textBox9.get()
            Country = '"'+textBox10.get()+'"'
            Cno =  textBox11.get()
            Cexp = '"'+textBox12.get()+'"'
            Cpin = textBox13.get()
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')

            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()
            mycursor.execute('INSERT INTO Customer (FirstName,LastName,Phone,Email,Address,City,PostalCode,Country) VALUES ('+Fname+','+Lname+','+Phone+','+Email+','+Address+','+City+','+Pcode+','+Country+');')
            conn.commit()
            Result = mycursor.execute('Select CustomerID from Customer where Email = '+Email)
            Result = mycursor.fetchone()
            TypeID = Result[0]
            mycursor.execute('INSERT INTO Login (Username,Password,Acc_Type,ReferenceID) VALUES ('+Username+','+Password+',"Customer",'+str(TypeID)+');')
            conn.commit()
            mycursor.execute('INSERT INTO CARD_Details (CustomerID,Card_Number,Card_Pin,Card_Exp_Date,Name_On_Card,Billing_Addr) VALUES ('+str(TypeID)+','+Cno+','+Cpin+','+Cexp+','+Fname+','+Address+');')
            conn.commit()
            mycursor.execute('INSERT INTO Customer_Delivery_Address (CustomerID,Address,City,Postal_Code,Country) VALUES ('+str(TypeID)+','+Address+','+City+','+Pcode+','+Country+');')
            conn.commit()
            controller.show_frame(SignUpComplete)

        buttonCommit = tk.Button(self, height=1, width=10, text="Sign Up",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=700)

class SignUpComplete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sign Up Complete!", font=('Arial',40))
        label.pack(padx=20,pady=20)
        label = tk.Label(self, text = "Please go to Login page and Sign in with your created details", font=('Arial', 16))
        label.pack(padx=100,pady=100)

        def retrieve_input():
            controller.show_frame(Login)

        buttonCommit = tk.Button(self, height=1, width=10, text="Login",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=400)

class SignUpAdmin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART - Admin Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Personal Details", font=('Arial', 15))
        label.place(x=250, y=125)
        
        label = tk.Label(self, text = "Create Username", font=('Arial', 10))
        label.place(x=350, y=175)

        textBox1=tk.Entry(self,width=20)
        textBox1.place(x=550,y=175)

        label = tk.Label(self, text = "Create Password", font=('Arial', 10))
        label.place(x=350, y=200)

        textBox2=tk.Entry(self,width=20, show="*")
        textBox2.place(x=550,y=200)

        label = tk.Label(self, text = "First Name", font=('Arial', 10))
        label.place(x=350, y=225)

        textBox3=tk.Entry(self,width=20)
        textBox3.place(x=550,y=225)

        label = tk.Label(self, text = "Last Name", font=('Arial', 10))
        label.place(x=350, y=250)

        textBox4=tk.Entry(self,width=20)
        textBox4.place(x=550,y=250)

        def retrieve_input():

            Username = '"'+textBox1.get()+'"'
            Password = '"'+textBox2.get()+'"'
            Fname  = '"'+textBox3.get()+'"'
            Lname = '"'+textBox4.get()+'"'
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            
            
            mycursor = conn.cursor()
            mycursor.execute('INSERT INTO Admin (FirstName,LastName) VALUES ('+Fname+','+Lname+');')
            conn.commit()
            Result = mycursor.execute('Select AdminID from Admin where FirstName = '+Fname+' AND LastName = '+Lname)
            Result = mycursor.fetchone()
            TypeID = Result[0]
            mycursor.execute('INSERT INTO Login (Username,Password,Acc_Type,ReferenceID) VALUES ('+Username+','+Password+',"Admin",'+str(TypeID)+');')
            conn.commit()
            controller.show_frame(SignUpComplete)

        buttonCommit = tk.Button(self, height=1, width=10, text="Sign Up",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=350)

class SignUpSupplier(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="AMZKART - Supplier Sign up!", font=('Arial',40))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text = "Supplier Details", font=('Arial', 15))
        label.place(x=250, y=125)
        
        label = tk.Label(self, text = "Create Username", font=('Arial', 10))
        label.place(x=350, y=175)

        textBox1=tk.Entry(self,width=20)
        textBox1.place(x=550,y=175)

        label = tk.Label(self, text = "Create Password", font=('Arial', 10))
        label.place(x=350, y=200)

        textBox2=tk.Entry(self,width=20, show="*")
        textBox2.place(x=550,y=200)

        label = tk.Label(self, text = "Supplier Name", font=('Arial', 10))
        label.place(x=350, y=225)

        textBox3=tk.Entry(self,width=20)
        textBox3.place(x=550,y=225)

        label = tk.Label(self, text = "Phone", font=('Arial', 10))
        label.place(x=350, y=250)

        textBox4=tk.Entry(self,width=20)
        textBox4.place(x=550,y=250)

        label = tk.Label(self, text = "Email", font=('Arial', 10))
        label.place(x=350, y=275)

        textBox5=tk.Entry(self,width=20)
        textBox5.place(x=550,y=275)

        label = tk.Label(self, text = "Add Primary Warehouse Address", font=('Arial', 15))
        label.place(x=250, y=310)

        label = tk.Label(self, text = "Street Address", font=('Arial', 10))
        label.place(x=350, y=360)

        textBox7=tk.Entry(self,width=20)
        textBox7.place(x=550,y=360)

        label = tk.Label(self, text = "City", font=('Arial', 10))
        label.place(x=350, y=385)

        textBox8=tk.Entry(self,width=20)
        textBox8.place(x=550,y=385)

        label = tk.Label(self, text = "Postal Code", font=('Arial', 10))
        label.place(x=350, y=410)

        textBox9=tk.Entry(self,width=20)
        textBox9.place(x=550,y=410)

        label = tk.Label(self, text = "Country", font=('Arial', 10))
        label.place(x=350, y=435)

        textBox10=tk.Entry(self,width=20)
        textBox10.place(x=550,y=435)


        def retrieve_input():

            Username = '"'+textBox1.get()+'"'
            Password = '"'+textBox2.get()+'"'
            Sname  = '"'+textBox3.get()+'"'
            Phone = '"'+textBox4.get()+'"'
            Email = '"'+textBox5.get()+'"'
            Saddress = '"'+textBox7.get()+'"'
            City = '"'+textBox8.get()+'"'
            Pcode = '"'+textBox9.get()+'"'
            Country = '"'+textBox10.get()+'"'

            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()
            mycursor.execute('INSERT INTO Supplier (SupplierName,Phone,Email) VALUES ('+Sname+','+Phone+','+Email+');')
            conn.commit()

            Result = mycursor.execute('Select SupplierID from Supplier where Email = '+Email)
            Result = mycursor.fetchone()
            TypeID = Result[0]

            mycursor.execute('INSERT INTO Supplier_Addr (SupplierID,Address,City,Postal_Code,Country) VALUES ('+str(TypeID)+','+Saddress+','+City+','+Pcode+','+Country+');')
            conn.commit()


            mycursor.execute('INSERT INTO Login (Username,Password,Acc_Type,ReferenceID) VALUES ('+Username+','+Password+',"Supplier",'+str(TypeID)+');')
            conn.commit()



            controller.show_frame(SignUpComplete)

        buttonCommit = tk.Button(self, height=1, width=10, text="Sign Up",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=450, y=500)

class LoginCustomer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART", font=('Arial',30))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text="Become a Member Today! 10% discount on all orders!", font=('Arial',20))
        label.pack(padx=50,pady=50)

        buttonCommit = tk.Button(self, height=1, width=20, text="Purchase Membership!",
                                command = lambda: controller.show_frame(Membership))

        buttonCommit.place(x=400, y=225)

        label = tk.Label(self, text="Already a Member? Continue to Shopping with AmzKart ->", font=('Arial',20))
        label.pack(padx=60,pady=60)

        buttonCommit = tk.Button(self, height=1, width=20, text="Continue to AmzKart",
                                command = lambda: controller.show_frame(ListOfProducts))

        buttonCommit.place(x=400, y=360)

class Membership(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART Premium", font=('Arial',30))
        label.pack(padx=20,pady=20)

        label = tk.Label(self, text="AmzKart Premium members are entitled to $0 in delivery fees,\n and an additional 10% discount on every order placed.\nSelect from our subscriptions below", font=('Arial',15))
        label.pack(padx=20,pady=20)
        
        def retrieve_input():
            
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')

            if(conn):
                print('connection successful')

            else:
                print('connection failed')

            mycursor = conn.cursor() 

            Result = mycursor.execute('Select Card_Number from card_details where CustomerID = '+str(cID))
            cardOptions = [str(item[0]) for item in mycursor.fetchall()]
            clicked = tk.StringVar(self)
            drop = tk.OptionMenu(self, clicked , *cardOptions)
            drop.place(x=550,y=250)


        buttonCommit = tk.Button(self, height=1, width=20, text="Continue to Payment",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=400, y=200)


        #list of cards from card table
        # cardOptions = ["XX2634", "XX2081"]
        subscriptionOptions = ["$25 Monthly($300 for 12 months)", "$200 Yearly(33% discount)"]
        # clicked = tk.StringVar(self)
        clickedSub = tk.StringVar(self)
        label = tk.Label(self, text = "Select Payment Option", font=('Arial', 10))
        label.place(x=350, y=260)
        label = tk.Label(self, text = "Select Subscription Option", font=('Arial', 10))
        label.place(x=350, y=300)
        drop = tk.OptionMenu(self, clickedSub , *subscriptionOptions)
        drop.place(x=550,y=290)
        def mem():
            messagebox.showinfo("Success!","Request Initiated")


            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()

            mycursor.execute('UPDATE Customer SET Membership = True where CustomerId = '+str(cID))
            conn.commit()



        buttonCommit = tk.Button(self, height=1, width=20, text="Purchase Membership",
                                command = lambda: mem())

        buttonCommit.place(x=400, y=360)

        buttonCommit = tk.Button(self, height=1, width=20, text="Continue to AmzKart",
                                command = lambda: controller.show_frame(ListOfProducts))

        buttonCommit.place(x=400, y=400)

class LoginAdmin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART - Admin Login", font=('Arial',30))
        label.pack(padx=20,pady=20)

        actionOptions = ["Remove a Supplier", "Remove a Customer", "Cancel an Order"]
        clicked = tk.StringVar(self)

        label = tk.Label(self, text = "Select from List of Actions", font=('Arial', 10))
        label.place(x=350, y=155)
        drop = tk.OptionMenu(self, clicked , *actionOptions)
        drop.place(x=550,y=150)

        def retrieve_input():
            action = clicked.get()
            if action == "Remove a Supplier":
                textBox1.config(state="normal")
                textBox2.config(state="normal")
                textBox3.config(state="disabled")
                textBox4.config(state="disabled")
                textBox5.config(state="disabled")
                textBox6.config(state="disabled")
            elif action == "Remove a Customer":
                textBox1.config(state="disabled")
                textBox2.config(state="disabled")
                textBox3.config(state="normal")
                textBox4.config(state="normal")
                textBox5.config(state="normal")
                textBox6.config(state="disabled")
            elif action == "Cancel an Order":
                textBox1.config(state="disabled")
                textBox2.config(state="disabled")
                textBox3.config(state="disabled")
                textBox4.config(state="disabled")
                textBox5.config(state="disabled")
                textBox6.config(state="normal")


        buttonCommit = tk.Button(self, height=1, width=10, text="Continue",
                                command = lambda: retrieve_input())
        
        buttonCommit.place(x=500, y=200)

        label = tk.Label(self, text = "Remove a Supplier", font=('Arial', 15))
        label.place(x=250, y=240)

        label = tk.Label(self, text = "Supplier Name", font=('Arial', 10))
        label.place(x=350, y=290)

        textBox1=tk.Entry(self,width=20, state="disabled")
        textBox1.place(x=550,y=290)

        label = tk.Label(self, text = "Supplier City", font=('Arial', 10))
        label.place(x=350, y=315)

        textBox2=tk.Entry(self,width=20, state="disabled")
        textBox2.place(x=550,y=315)

        label = tk.Label(self, text = "Remove a Customer", font=('Arial', 15))
        label.place(x=250, y=350)

        label = tk.Label(self, text = "Customer FirstName", font=('Arial', 10))
        label.place(x=350, y=400)

        textBox3=tk.Entry(self,width=20, state="disabled")
        textBox3.place(x=550,y=400)

        label = tk.Label(self, text = "Customer LastName", font=('Arial', 10))
        label.place(x=350, y=425)

        textBox4=tk.Entry(self,width=20, state="disabled")
        textBox4.place(x=550,y=425)

        label = tk.Label(self, text = "Customer Email", font=('Arial', 10))
        label.place(x=350, y=450)

        textBox5=tk.Entry(self,width=20, state="disabled")
        textBox5.place(x=550,y=450)

        label = tk.Label(self, text = "Cancel an Order", font=('Arial', 15))
        label.place(x=250, y=485)

        label = tk.Label(self, text = "Order ID", font=('Arial', 10))
        label.place(x=350, y=535)

        textBox6=tk.Entry(self,width=20, state="disabled")
        textBox6.place(x=550,y=535)

        def executeChanges():
            action = clicked.get()
            if action == "Remove a Supplier":
                SName = textBox1.get()
                SCity = textBox2.get()
                SName = '"'+SName+'"'
                SCity = '"'+SCity+'"'
               

                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()
                
                Result = mycursor.execute('Select Supplier.SupplierID from Supplier,Supplier_Addr Where Supplier.SupplierID = Supplier_Addr.SupplierID AND Supplier.SupplierName = '+SName+' AND Supplier_Addr.City = '+SCity)
                Result = mycursor.fetchone()
                mycursor.execute('Delete from Supplier where SupplierID ='+str(Result[0]))
                conn.commit()



            elif action == "Remove a Customer":
                CFname = textBox3.get()
                CLName = textBox4.get()
                CEmail = textBox5.get()
                
                CEmail = '"'+CEmail+'"'
                CFname = '"'+CFname+'"'
                CLName = '"'+CLName+'"'

                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()
                
                Result = mycursor.execute('Select CustomerID from Customer Where FirstName = '+CFname+' AND LastName = '+CLName+' AND Email = '+CEmail)
                Result = mycursor.fetchone()
                mycursor.execute('Delete from Customer where CustomerID ='+str(Result[0]))
                conn.commit()




            elif action == "Cancel an Order":
                OrderID = textBox6.get()
                OrderID = '"'+OrderID+'"'

                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()
                
                mycursor.execute('Delete from Orders where OrderID ='+OrderID)
                conn.commit()
                

            messagebox.showinfo("Success!","Request Initiated")

        buttonCommit = tk.Button(self, height=1, width=20, text="Initiate Changes",
                                command = lambda: executeChanges())

        buttonCommit.place(x=470, y=585)

        buttonCommit = tk.Button(self, height=1, width=10, text="Logout",
                                command = lambda: controller.show_frame(Login))

        buttonCommit.place(x=500, y=635)


class LoginSupplier(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART - Supplier Login", font=('Arial',30))
        label.pack(padx=20,pady=20)

        actionOptions = ["Add a New Product", "Add a New Warehouse", "Remove a Product"]
        clicked = tk.StringVar(self)

        label = tk.Label(self, text = "Select from List of Actions", font=('Arial', 10))
        label.place(x=350, y=155)
        drop = tk.OptionMenu(self, clicked , *actionOptions)
        drop.place(x=550,y=150)
        clickedProd = tk.StringVar(self)

        def retrieve_input():
            action = clicked.get()
            if action == "Add a New Product":
                textBox1.config(state="normal")
                textBox2.config(state="normal")
                textBox3.config(state="normal")
                textBox4.config(state="normal")
                textBox5.config(state="disabled")
                textBox6.config(state="disabled")
                textBox7.config(state="disabled")
                textBox8.config(state="disabled")
                # textBox9.config(state="disabled")
            elif action == "Add a New Warehouse":
                textBox1.config(state="disabled")
                textBox2.config(state="disabled")
                textBox3.config(state="disabled")
                textBox4.config(state="disabled")
                textBox5.config(state="normal")
                textBox6.config(state="normal")
                textBox7.config(state="normal")
                textBox8.config(state="normal")
                # textBox9.config(state="disabled")
            elif action == "Remove a Product":
                textBox1.config(state="disabled")
                textBox2.config(state="disabled")
                textBox3.config(state="disabled")
                textBox4.config(state="disabled")
                textBox5.config(state="disabled")
                textBox6.config(state="disabled")
                textBox7.config(state="disabled")
                textBox8.config(state="disabled")
                # textBox9.config(state="normal")

                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()

                Result = mycursor.execute('Select Product.ProductName from Product,Supplier_Prod_List where Supplier_Prod_List.ProductID = Product.ProductID AND Supplier_Prod_List.SupplierID = '+str(cID))
                prodOptions = [str(item[0]) for item in mycursor.fetchall()]
                drop = tk.OptionMenu(self, clickedProd , *prodOptions)
                drop.place(x=550,y=595)


        buttonCommit = tk.Button(self, height=1, width=10, text="Continue",
                                command = lambda: retrieve_input())

        buttonCommit.place(x=500, y=200)

        label = tk.Label(self, text = "Add New Product Details", font=('Arial', 15))
        label.place(x=250, y=240)

        label = tk.Label(self, text = "Product Name", font=('Arial', 10))
        label.place(x=350, y=270)

        textBox1=tk.Entry(self,width=20, state="disabled")
        textBox1.place(x=550,y=270)

        label = tk.Label(self, text = "Product Description", font=('Arial', 10))
        label.place(x=350, y=295)

        textBox2=tk.Entry(self,width=20, state="disabled")
        textBox2.place(x=550,y=295)

        label = tk.Label(self, text = "Quantity Available", font=('Arial', 10))
        label.place(x=350, y=320)

        textBox3=tk.Entry(self,width=20, state="disabled")
        textBox3.place(x=550,y=320)

        label = tk.Label(self, text = "Product Price", font=('Arial', 10))
        label.place(x=350, y=345)

        textBox4=tk.Entry(self,width=20, state="disabled")
        textBox4.place(x=550,y=345)

        label = tk.Label(self, text = "Add New Warehouse Details", font=('Arial', 15))
        label.place(x=250, y=380)

        label = tk.Label(self, text = "Address", font=('Arial', 10))
        label.place(x=350, y=430)

        textBox5=tk.Entry(self,width=20, state="disabled")
        textBox5.place(x=550,y=430)

        label = tk.Label(self, text = "City", font=('Arial', 10))
        label.place(x=350, y=455)

        textBox6=tk.Entry(self,width=20, state="disabled")
        textBox6.place(x=550,y=455)

        label = tk.Label(self, text = "Postal Code", font=('Arial', 10))
        label.place(x=350, y=480)

        textBox7=tk.Entry(self,width=20, state="disabled")
        textBox7.place(x=550,y=480)

        label = tk.Label(self, text = "Country", font=('Arial', 10))
        label.place(x=350, y=505)

        textBox8=tk.Entry(self,width=20, state="disabled")
        textBox8.place(x=550,y=505)

        label = tk.Label(self, text = "Remove a Product", font=('Arial', 15))
        label.place(x=250, y=540)

        label = tk.Label(self, text = "Select a Product", font=('Arial', 10))
        label.place(x=350, y=595)

        # textBox9=tk.Entry(self,width=20, state="disabled")
        # textBox9.place(x=550,y=595)

        def executeChanges():
            action = clicked.get()
            print(action)
            if action == "Add a New Product":
                PName = textBox1.get()
                PDesc = textBox2.get()
                Quantity = textBox3.get()
                Price = textBox4.get()
                PName = '"'+PName+'"'
                PDesc = '"'+PDesc+'"'
                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()

                mycursor.execute('INSERT INTO Product (ProductName,ProductDescription,QuantityAvailable,ProductAvailability,ProductPrice) VALUES ('+PName+','+PDesc+','+Quantity+',True,'+Price+');')
                conn.commit()

                Result = mycursor.execute('Select ProductID from Product where ProductName = '+PName+' AND ProductDescription = '+PDesc)
                Result = mycursor.fetchone()
                TypeID = Result[0]
                
                mycursor.execute('INSERT INTO Supplier_Prod_List (ProductID, SupplierID) VALUES ('+str(TypeID)+','+str(cID)+');')
                conn.commit()

            elif action == "Add a New Warehouse":
                WarAddr = textBox5.get()
                City = textBox6.get()
                PostalCode = textBox7.get()
                Country = textBox8.get()

                WarAddr = '"'+WarAddr+'"'
                City = '"'+City+'"'
                PostalCode = '"'+PostalCode+'"'
                Country = '"'+Country+'"'

                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()

                mycursor.execute('INSERT INTO Supplier_Addr (SupplierID,Address,City,Postal_Code,Country) VALUES ('+str(cID)+','+WarAddr+','+City+','+PostalCode+','+Country+');')
                conn.commit()
                
            elif action == "Remove a Product":
                PNameRemoved = clickedProd.get()
                PNameRemoved = '"'+PNameRemoved+'"'
                
                conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
                if(conn):
                    print('connection successfull')

                else:
                    print('connection failed')

                mycursor = conn.cursor()

                Result = mycursor.execute('Select Product.ProductID from Product,Supplier_Prod_List Where Supplier_Prod_List.SupplierID = '+str(cID)+' AND Supplier_Prod_List.ProductID = Product.ProductID AND Product.ProductName ='+PNameRemoved)
                Result = mycursor.fetchone()
                mycursor.execute('Delete from Product where ProductID ='+str(Result[0]))
                conn.commit()

                
            messagebox.showinfo("Success!","Request Initiated")

        buttonCommit = tk.Button(self, height=1, width=20, text="Initiate Changes",
                                command = lambda: executeChanges())

        buttonCommit.place(x=470, y=645)

        buttonCommit = tk.Button(self, height=1, width=10, text="Logout",
                                command = lambda: controller.show_frame(Login))

        buttonCommit.place(x=500, y=695)


class ListOfProducts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART", font=('Arial',30))
        label.pack(padx=20,pady=20)
        buttonCommit = tk.Button(self, height=1, width=30, text="Edit/Add Account Information",
                                command = lambda: controller.show_frame(EditAddCustomerInformation))

        buttonCommit.place(x=30, y=35)
        buttonCommit = tk.Button(self, height=1, width=10, text="Logout",
                                command = lambda: controller.show_frame(Login))

        buttonCommit.place(x=800, y=35)
        label = tk.Label(self, text = "Select a Product From the List", font=('Arial', 10))
        label.place(x=350, y=175)
        clicked = tk.StringVar(self)
        clickQuant = tk.StringVar(self)
        #Options from Product List from Product Table
        def productLists():

            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()

            Result = mycursor.execute('Select ProductName from Product')
            Result = mycursor.fetchall()

            prodOptions = [str(item[0]) for item in Result]

            drop = tk.OptionMenu(self, clicked , *prodOptions)
            drop.place(x=550,y=170)
        def displayProductInformation():
            productSelected = clicked.get()
            print(productSelected)
            resetString = "                                              "
            label = tk.Label(self, text = resetString, font=('Arial', 10))
            label.place(x=550, y=300)
            label = tk.Label(self, text = resetString, font=('Arial', 10))
            label.place(x=550, y=340)
            label = tk.Label(self, text = resetString, font=('Arial', 10))
            label.place(x=550, y=380)
            label = tk.Label(self, text = resetString, font=('Arial', 10))
            label.place(x=550, y=420)
            label = tk.Label(self, text = resetString, font=('Arial', 10))
            label.place(x=550, y=460)

            productSelected = '"'+productSelected+'"'

            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()
            

            Result = mycursor.execute('Select ProductDescription from Product where ProductName = '+productSelected)
            Result = mycursor.fetchall()
            prodDesc = [str(item[0]) for item in Result]
            temp = str(prodDesc)
            temp = temp[2:-2]

            Result1 = mycursor.execute('Select ProductPrice from Product where ProductName = '+productSelected)
            Result1 = mycursor.fetchall()
            prodPrice = [item[0] for item in Result1]



            Result2 = mycursor.execute('Select Supplier.SupplierName from Product,Supplier_Prod_List,Supplier where Product.ProductName = '+productSelected+' AND Supplier_Prod_List.ProductID  = Product.ProductID AND Supplier_Prod_List.SupplierID = Supplier.SupplierID')
            Result2 = mycursor.fetchall()
            supplierName = [str(item[0]) for item in Result2]
            print(supplierName)

            Result3 = mycursor.execute('Select QuantityAvailable from Product where ProductName = '+productSelected)
            Result3 = mycursor.fetchall()
            qAval = [item[0] for item in Result3]
            qAval = qAval[0]

            inOutStock = "In Stock" if qAval > 0 else "Sorry! Out of Stock"
            label = tk.Label(self, text = "Product Description", font=('Arial', 10))
            label.place(x=350, y=300)
            label = tk.Label(self, text = temp, font=('Arial', 10))
            label.place(x=550, y=300)
            label = tk.Label(self, text = "Price", font=('Arial', 10))
            label.place(x=350, y=340)
            label = tk.Label(self, text = "$"+str(prodPrice[0]), font=('Arial', 10))
            label.place(x=550, y=340)
            label = tk.Label(self, text = "Supplier Name", font=('Arial', 10))
            label.place(x=350, y=380)
            label = tk.Label(self, text = supplierName, font=('Arial', 10))
            label.place(x=550, y=380)
            label = tk.Label(self, text = "Product Availability", font=('Arial', 10))
            label.place(x=350, y=420)
            label = tk.Label(self, text = inOutStock, font=('Arial', 10))
            label.place(x=550, y=420)
            if inOutStock == "Sorry! Out of Stock":
                messagebox.showerror("Error", "Product Currently Out of Stock! ")
            else:
                label = tk.Label(self, text = "Select Quantity (Max: "+str(qAval)+")", font=('Arial', 10))
                label.place(x=350, y=460)
                dropDownForQuantity = [str(i+1) for i in range(qAval)]
                opt = tk.OptionMenu(self, clickQuant , *dropDownForQuantity)
                opt.place(x=550, y=455)
                
        def addToCart():
                
            Fprod = clicked.get()
            Fquant = clickQuant.get()

            global prodList 
            prodList.append(Fprod)

            global quantList 
            quantList.append(Fquant)

            print(prodList)
            print(quantList)
                   
        
        buttonCommit = tk.Button(self, height=1, width=30, text="Continue to Select Products",
                                command = lambda: productLists())

        buttonCommit.place(x=400, y=120)
        buttonCommit = tk.Button(self, height=1, width=15, text="Select Product",
                                command = lambda: displayProductInformation())
        buttonCommit.place(x=450, y=240)

        buttonCommit = tk.Button(self, height=1, width=15, text="Add to Cart",
                                command = lambda: addToCart())
        buttonCommit.place(x=450, y=550)
        buttonCommit = tk.Button(self, height=1, width=10, text="View Cart",
                                command = lambda: controller.show_frame(ShoppingCart))
        buttonCommit.place(x=450, y=625)


class EditAddCustomerInformation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART - Edit/Add Information", font=('Arial',30))
        label.pack(padx=20,pady=20)

class ShoppingCart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to AMZKART - View Cart", font=('Arial',30))
        label.pack(padx=20,pady=20)
        self.yPos = 170
        self.totalOrderPrice = 0
        
        def displayCart():
            # isMember = True
            self.yPos = 170
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()
    
            Result = mycursor.execute('Select Membership from Customer where CustomerID = '+str(cID))
            Result = mycursor.fetchall()
            mem = [item[0] for item in Result]
            mem = mem[0]
            isMember = True if mem>0 else False

            for i in range(len(prodList)):
                
                productName = '"'+prodList[i]+'"'
                Result = mycursor.execute('Select ProductPrice from Product where ProductName = '+productName)
                Result = mycursor.fetchall()
                price = [item[0] for item in Result]
                price = price[0]
                self.totalOrderPrice += price*int(quantList[i])

                label = tk.Label(self, text = "Product Name", font=('Arial', 10))
                label.place(x=200, y=self.yPos)
                label = tk.Label(self, text = "                                 ", font=('Arial', 10))
                label.place(x=400, y=self.yPos)
                label = tk.Label(self, text = prodList[i], font=('Arial', 10))
                label.place(x=400, y=self.yPos)
                self.yPos = self.yPos+25
                label = tk.Label(self, text = "Product Price", font=('Arial', 10))
                label.place(x=200, y=self.yPos)
                label = tk.Label(self, text = "                                 ", font=('Arial', 10))
                label.place(x=400, y=self.yPos)
                label = tk.Label(self, text = "$"+str(price), font=('Arial', 10))
                label.place(x=400, y=self.yPos)
                self.yPos = self.yPos+25
                label = tk.Label(self, text = "Quantity Selected", font=('Arial', 10))
                label.place(x=200, y=self.yPos)
                label = tk.Label(self, text = "                                 ", font=('Arial', 10))
                label.place(x=400, y=self.yPos)
                label = tk.Label(self, text = quantList[i], font=('Arial', 10))
                label.place(x=400, y=self.yPos)
                self.yPos = self.yPos+50
            
            label = tk.Label(self, text = "Order Price", font=('Arial', 10))
            label.place(x=200, y=self.yPos)
            label = tk.Label(self, text = "                                 ", font=('Arial', 10))
            label.place(x=400, y=self.yPos)
            label = tk.Label(self, text = "$"+str(self.totalOrderPrice), font=('Arial', 10))
            label.place(x=400, y=self.yPos)
            self.yPos = self.yPos+50
            if isMember:
                self.totalOrderPrice = self.totalOrderPrice*0.9
            label = tk.Label(self, text = "Final Order Price", font=('Arial', 10))
            label.place(x=200, y=self.yPos)
            label = tk.Label(self, text = "                                 ", font=('Arial', 10))
            label.place(x=400, y=self.yPos)
            label = tk.Label(self, text = "$"+"{:.2f}".format(self.totalOrderPrice), font=('Arial', 10))
            label.place(x=400, y=self.yPos)
            self.yPos = self.yPos+50
            
            
        def placeOrder():
            
                        
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')
            if(conn):
                print('connection successfull')

            else:
                print('connection failed')

            mycursor = conn.cursor()
            
            mycursor.execute('INSERT INTO Orders (OrderPrice,OrderDate,CompletionStatus) VALUES ('+str(self.totalOrderPrice)+',curdate(),0);')
            conn.commit()
            

            Result = mycursor.execute('Select OrderID from Orders where OrderPrice = '+str(self.totalOrderPrice))
            Result = mycursor.fetchone()
            TypeID = Result[0]


            for i in range(len(prodList)):
                prodList[i] = '"'+prodList[i]+'"'
                Result = mycursor.execute('Select ProductID from Product where ProductName = '+prodList[i])
                Result = mycursor.fetchone()
                prodID = Result[0]
                prodID = '"'+str(prodID)+'"'

                mycursor.execute('INSERT INTO Product_Orders(ProductID,OrderID) VALUES ('+str(prodID)+','+str(TypeID)+');')
                conn.commit()

                
                Result = mycursor.execute('Select QuantityAvailable from Product where ProductName = '+prodList[i])
                Result = mycursor.fetchone()
                aval = Result[0]

                curQty = aval - int(quantList[i]) 
                curQty = '"'+str(curQty)+'"'
                mycursor.execute('UPDATE Product SET QuantityAvailable = '+str(curQty)+' Where ProductName = '+prodList[i])
                conn.commit()


            messagebox.showinfo("Success!", "Order Placed!\nYour product will be delivered in 5-7 business days")

        buttonCommit = tk.Button(self, height=1, width=10, text="Place Order",
                                command = lambda: placeOrder())

        buttonCommit.place(x=725, y=120)
        buttonCommit = tk.Button(self, height=1, width=30, text="Add More Products to Cart",
                                command = lambda: controller.show_frame(ListOfProducts))

        buttonCommit.place(x=650, y=170)
        def showCards():
            conn = mysql.connector.connect(host = 'localhost', password = 'Paytmkaro@12', user = 'root', database = 'Final')

            if(conn):
                print('connection successful')

            else:
                print('connection failed')

            mycursor = conn.cursor() 

            Result = mycursor.execute('Select Card_Number from card_details where CustomerID = '+str(cID))
            cardOptions = [str(item[0]) for item in mycursor.fetchall()]
            clicked = tk.StringVar(self)
            drop = tk.OptionMenu(self, clicked , *cardOptions)
            drop.place(x=800,y=270)

            Result = mycursor.execute('Select Address from Customer where CustomerID = '+str(cID))
            deliveryOptions = [str(item[0]) for item in mycursor.fetchall()]
            clicked = tk.StringVar(self)
            drop = tk.OptionMenu(self, clicked , *deliveryOptions)
            drop.place(x=800,y=320)
        buttonCommit = tk.Button(self, height=1, width=20, text="Proceed to Payment",
                                command = lambda: showCards())

        buttonCommit.place(x=690, y=220)
            
        buttonCommit = tk.Button(self, height=1, width=10, text="View Cart",
                                command = lambda: displayCart())

        buttonCommit.place(x=300, y=120)
        label = tk.Label(self, text = "Select Payment Option", font=('Arial', 10))
        label.place(x=650, y=275)
        label = tk.Label(self, text = "Select Delivery Address", font=('Arial', 10))
        label.place(x=650, y=325)
        buttonCommit = tk.Button(self, height=1, width=10, text="Logout",
                                command = lambda: controller.show_frame(Login))

        buttonCommit.place(x=725, y=375)
        

root = tkinterApp()
root.geometry("1000x1000")
root.mainloop()