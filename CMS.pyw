import Tkinter as tk
import ttk
from Tkinter import *
import tkMessageBox
import sqlite3
import smtplib
from random import randint
import ttk
from datetime import datetime, date
from datetime import timedelta
import webbrowser

top=Tk()
top.configure(bg="Lightgray")
top.title('Courier Management System')

#linux
img = PhotoImage('icon.ico');
top.tk.call('wm', 'iconphoto', top._w, img)

#windows
#top.iconbitmap('icon.ico')
w,h=top.winfo_screenwidth(),top.winfo_screenheight()
top.geometry("%dx%d+0+0" % (w, h))

def change_background():
    global canvas
    global myimg
    global gif2
    canvas.itemconfig(myimg,image = gif2)

canvas = Canvas(width = 1350, height = 900)
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'bg.gif')
myimg=canvas.create_image(0,0, image = gif1, anchor = NW)
gif2 = PhotoImage(file = 'dark.gif')
gif3 = PhotoImage(file = 'mix.gif')


# function to remove window
def remove():
    Mframe.pack_forget()

# function to call login window    
def login_remove():
    remove()
    login()

# function to call new user window
def newuser_remove():
    remove()
    newuser()

# function to call track window
def track_remove():
    remove()
    track(0," "," ")

def callback(event):
    webbrowser.open_new(r"http://linkedin.com/in/varinder-singh-08667788?trk=nav_responsive_tab_profile_pic")
    
# Login window    
def login():   
    def remove_login():
        frame2.pack_forget()

    def login_to_main():
        frame2.pack_forget()
        main()

    # function to call menu
    def menu_remove(user1,pas1):
        remove_login()
        menu(user1,pas1)

    # To verify login
    def login_verfiy():
        user1=EA1.get()
        pas1=EA2.get()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT username,password FROM user where username='%s'"%user1)
        verify=c.fetchone()
        conn.close()
        
        if(verify!=None):
            if(verify[1]==pas1):
                menu_remove(user1,pas1)
            else:
                tkMessageBox.showwarning("Warning","Worng password!")
        else:
                tkMessageBox.showwarning("Warning","User do not exist!")
                

    frame2=Frame(canvas,borderwidth=30,bg="snow")
    LA=Label(frame2,text="Login Page",bg="snow",font="times 15")
    LA.grid(row=0,columnspan=2,padx=10,pady=10)

    LA1=Label(frame2,text="User Name :",bg="snow")
    LA1.grid(row=1,column=0,padx=10,pady=10,sticky=E)
    EA1=ttk.Entry(frame2)
    EA1.grid(row=1,column=1,padx=10,pady=10)

    LA2=Label(frame2,text="Password :",bg="snow")
    LA2.grid(row=2,column=0,padx=10,pady=10,sticky=E)
    EA2=ttk.Entry(frame2,show="*")
    EA2.grid(row=2,column=1,padx=10,pady=10)

    BA1=ttk.Button(frame2,text="Login Now",command=login_verfiy)
    BA1.grid(row=3,columnspan=2,padx=10,pady=10)

    BA3=ttk.Button(frame2,text="Back",command=login_to_main)
    BA3.grid(row=4,columnspan=2,padx=10,pady=10)

    frame2.pack(pady=50)

# New user window
def newuser():

    Passcode=(randint(0,9999))
    
    def newuser_to_main():
        frame1.pack_forget()
        main()

    def details():
        conn=sqlite3.connect('database.db')
        con = conn.cursor()
        con.execute("CREATE TABLE if not exists user (name text, mobile text, email text, username text UNIQUE, password text)")
        name=str(E1.get())
        mobile=str(E4.get())
        email=str(E5.get())
        username=str(E6.get())
        password=str(E7.get())
        v_otp=E5A.get()
        if(str(Passcode)==v_otp and email!=""):
            if(username!="" and password!=""and name!="" and mobile!=""):
                try:
                    con.execute("INSERT INTO user VALUES (?,?,?,?,?)",(name,mobile,email,username,password))
                    conn.commit()
                    conn.close()
                    tkMessageBox.showinfo("Registered","You have successfully registered, Now you can Login.")
                    newuser_to_main()
                except:
                    tkMessageBox.showerror("Warning","Username already exist.")
                
                
            else:
                tkMessageBox.showerror("Warning","Some fields are left empty")
        else:
            tkMessageBox.showerror("Error","Wrong Passcode \nPasscode is sent to your entered email")
            
    def OTP():
        try:
            reciver=str(E5.get())
            Message="""Subject: Important Information
                       Your Passcode is """+str(Passcode)

            
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.starttls()
            mail.login('cmslpu1@gmail.com','pythonaccount')
            mail.sendmail('cmslpu1@gmail.com',reciver,Message)
        except:
            tkMessageBox.showerror("Error","Check your internet connection")
              
    frame1=Frame(canvas,borderwidth=30,bg="snow")
    L=Label(frame1,text="Fill the details",bg="snow",font="times 15")
    L.grid(row=0,columnspan=2,padx=10,pady=10)

    L1=Label(frame1,text="Name",bg="snow")
    L1.grid(row=1,column=0,padx=10,pady=10)
    E1=ttk.Entry(frame1)
    E1.grid(row=1,column=1,padx=10,pady=10)

    L3=Label(frame1,text="Gender",bg="snow")
    L3.grid(row=3,column=0,padx=10,pady=10)
    R1=ttk.Radiobutton(frame1,text="Male",value=2)
    R2=ttk.Radiobutton(frame1,text="Female",value=1)
    R1.grid(row=3,column=1,padx=10,pady=10)
    R2.grid(row=4,column=1,padx=10,pady=10)

    L4=Label(frame1,text="Mobile No",bg="snow")
    L4.grid(row=5,column=0,padx=10,pady=10)
    E4=ttk.Entry(frame1)
    E4.grid(row=5,column=1,padx=10,pady=10)
 
    L5=Label(frame1,text="Email Id",bg="snow")
    L5.grid(row=6,column=0,padx=10,pady=10)
    E5=ttk.Entry(frame1)
    E5.grid(row=6,column=1,padx=10,pady=10)

    BB=ttk.Button(frame1,text="Send Passcode",command=OTP)
    BB.grid(row=7,column=0)
    E5A=ttk.Entry(frame1)
    E5A.grid(row=7,column=1)

    LL=Label(frame1,text="Enter new username and password:",font="times 15",bg="snow")
    LL.grid(row=8,columnspan=2,padx=10,pady=10)

    L6=Label(frame1,text="User Name /",bg="snow")
    L61=Label(frame1,text="Registration No.",bg="snow")
    L6.grid(row=9,column=0,padx=10)
    L61.grid(row=10,column=0,padx=10)
    E6=ttk.Entry(frame1)
    E6.grid(row=9,rowspan=2,column=1,padx=10,pady=10)

    L7=Label(frame1,text="Password",bg="snow")
    L7.grid(row=11,column=0,padx=10,pady=10)
    E7=ttk.Entry(frame1)
    E7.grid(row=11,column=1,padx=10,pady=10)

    B1=ttk.Button(frame1,text="Submit",command=details)
    B1.grid(row=12,columnspan=2,padx=10,pady=10)

    B2=ttk.Button(frame1,text="Back",command=newuser_to_main)
    B2.grid(row=13,columnspan=2,padx=10,pady=10)

    frame1.pack(pady=50)

# Track window
def track(flag,user1,pas1):
    
    def track_to_back():
        if(flag==0):
            frame3.pack_forget()
            main()
        else:
            frame3.pack_forget()
            menu(user1,pas1)

    def track_order():
        def track_order_to_track():
            frame8.pack_forget()
            track(flag,user1,pas1)
            
        frame3.pack_forget()
        track1=str(EB2.get())
        conn = sqlite3.connect('database.db')
        con = conn.cursor()
        try:
            con.execute("SELECT sname,sphone,rname,rcompany,rphone,raddress,ship_date,delivery_date FROM shipments WHERE track='%s'"%track1)
            x=con.fetchone()
            frame8=Frame(canvas,borderwidth=30,bg="snow")
            lis=['Sender Information:','Name ','Phone','Receiver information:','Name','Company','Phone','Address','Shipdate','Delivery date']

            for i in range(10):
                e=ttk.Entry(frame8)
                e.grid(row=i, column=0, sticky=NSEW,padx=5)
                e.insert(END,lis[i])
                e.configure(state='readonly')

            j=0  
            for i in range(10):
                if(i==0 or i==3 ):
                    continue
                e =ttk.Entry(frame8)
                e.grid(row=i, column=1, sticky=NSEW,padx=5)
                e.insert(END,x[j])
                e.configure(state='readonly')
                j+=1

            current_date=str(date.today())
            delivery_date=str(x[7])
            if (current_date==delivery_date):
                L81=Label(frame8,text = "Consignment will be delivered today ")
                L81.grid(row=12,columnspan=2,padx=10,pady=20)

            elif(current_date<delivery_date):
                t="Consignment will be delivered on "+(delivery_date)
                L81=Label(frame8,text = t)
                L81.grid(row=12,columnspan=2,padx=10,pady=20)

            else:
                L81=Label(frame8,text = "Consignment is already delivered")
                L81.grid(row=12,columnspan=2,padx=10,pady=20)
            conn.close

                
            B81=ttk.Button(frame8,text="Back",command=track_order_to_track)
            B81.grid(row=13,columnspan=2,padx=10,pady=10)
            frame8.pack(pady=100)
        except:
            tkMessageBox.showerror("Error","Invaild Consignment no.")
            track(flag,user1,pas1)
        con.close()
        
    frame3=Frame(canvas,borderwidth=30,bg="snow")
    LB=Label(frame3,text="Track Consignment",bg="snow",font="times 15")
    LB.grid(row=0,columnspan=2,padx=10,pady=10)
 
    LB1=Label(frame3,text="Consignment No",bg="snow")
    LB1.grid(row=2,column=0,padx=10,pady=10)
    EB2=ttk.Entry(frame3)
    EB2.grid(row=2,column=1,padx=10,pady=10)
 
    BB1=ttk.Button(frame3,text="Track",command=track_order)
    BB1.grid(row=3,columnspan=2,padx=10,pady=10)

    BB2=ttk.Button(frame3,text="Back",command=track_to_back)
    BB2.grid(row=8,columnspan=2,padx=10,pady=10)

    frame3.pack(pady=50)

overnight_delivery=0
flag=0
# Menu window
def menu(user1,pas1):
    def remove_menu():
        Aframe.pack_forget()

    # To shipment window    
    def ship_form():
        remove_menu()
    
        def ship_form_to_menu():
            frame4.pack_forget()
            menu(user1,pas1)           

        def additional():
            
            def ship():
                global overnight_delivery
                sname=ED2.get()
                scompany=ED3.get()
                saddress=ED5.get()+"-"+ED6.get()
                sphone=ED8.get()
                rname=EDA2.get()
                rcompany=EDA3.get()
                raddress=EDA5.get()+EDA6.get()
                rphone=EDA8.get()
                ship_date = date.today()
                if (overnight_delivery==500):
                    delivery_date= ship_date + timedelta(days=1)
                else:
                    delivery_date= ship_date + timedelta(days=3)
                    
                if(sname!="" and raddress!="" and scompany!="" and saddress!="" and sphone!="" and rname!="" and rcompany!="" and rphone!=""):
                    con.execute("CREATE TABLE if not exists shipments (track integer PRIMARY KEY autoincrement,username text,sname text,scompany text,saddress text,sphone text,rname text ,rcompany text,raddress text ,rphone tex,ship_date date,delivery_date datet)")
                    con.execute("INSERT INTO shipments(username,sname,scompany,saddress,sphone,rname,rcompany,raddress,rphone,ship_date,delivery_date) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(user1,sname,scompany,saddress,sphone,rname,rcompany,raddress,rphone,ship_date,delivery_date))
                    conn.commit()
                    con.execute("SELECT track FROM shipments WHERE username='%s'"%user1)
                    i=0
                    for row in con:
                        i+=1
                    j=0
                    con.execute("SELECT track FROM shipments WHERE username='%s'"%user1)
                    for row in con:
                        j+=1
                        if(i==j):
                            track1=row[0]            
                    tkMessageBox.showinfo("Consignment no.","Your consignment no. is :%s"%track1)
                    global flag
                    flag=1
                    additional_window(0,0,'Click on check charges',0,0,0)
                else:
                    tkMessageBox.showerror("Warning","Some fields are left empty")
                    additional_window(0,0,'Click on check charges',0,0,0)
                    

            frame4.pack_forget()
            
            def additional_window(insert1,insert2,insert3,radio1,radio2,mode):
                def additional_to_ship_form():
                    frame5.pack_forget()
                    ship_form()

                def charges():
                    global overnight_delivery
                    special=int(var2.get())
                    mode=int(var3.get())
                    pack=int(ED5.get())
                    weight=int(ED6.get())
                    overnight_delivery=int(var1.get())+100
                    charges=(weight*pack)+overnight_delivery+int(var2.get())
                    if(pack==0 or weight==0):
                       tkMessageBox.showerror("Warning","Enter no. of packages and total weight")
                    frame5.pack_forget()
                    additional_window(pack,weight,charges,overnight_delivery,special,mode)

                def payment():
                    def verify_pay():
                        cardname=str(PE1.get())
                        cardno=str(PE2.get())
                        cardexp1=str(PE4.get())
                        cardexp2=str(PE5.get())
                        if (cardname!="" and cardno!="" and cardexp1!=0 and cardexp2!=""):
                            tkMessageBox.showinfo("Successful","Payment is successful")
                            pay.destroy()
                            top.deiconify()
                        else:
                            tkMessageBox.showerror("Error","Payment is unsuccessful")
                            
                    def cancel_pay():
                        pay.destroy()
                        top.deiconify()
                    
                    top.withdraw()
                    pay = tk.Toplevel(top)
                    pay.title('Payment Portal')
                    pay.iconbitmap('icon.ico')
                    pay.resizable(height=False,width=False)

                    Pframe=Frame(pay)
   
                    L=ttk.Label(Pframe,text="Payment Information:")
                    L.grid(row=0,columnspan=2,pady=10)

                    L1=ttk.Label(Pframe,text="Credit Card:")
                    L1.grid(row=1,column=0,padx=10,sticky=E)

                    img1=PhotoImage(file= 'credit-card-logos.gif')
                    imge1 = Label(Pframe, image = img1 )
                    imge1.grid(row=1,column=1,pady=10)

                    L2=ttk.Label(Pframe,text="Card Holder Name:")
                    L2.grid(row=2,column=0,padx=10,pady=10,sticky=E)
                    PE1=ttk.Entry(Pframe,width=25)
                    PE1.grid(row=2,column=1,pady=10,sticky=W)

                    L3=ttk.Label(Pframe,text="Card Number:")
                    L3.grid(row=3,column=0,padx=10,pady=10,sticky=E)
                    PE2=ttk.Entry(Pframe,width=25)
                    PE2.grid(row=3,column=1,pady=10,sticky=W)

                    L4=ttk.Label(Pframe,text="Card Expiration:")
                    L4.grid(row=4,column=0,padx=10,pady=10,sticky=E)

                    PE4=ttk.Entry(Pframe,width=10)
                    PE4.grid(row=5,column=0,padx=5,pady=10,sticky=E)

                    PE5=ttk.Entry(Pframe,width=25)
                    PE5.grid(row=5,column=1,pady=10,sticky=W)

                    B1=ttk.Button(Pframe,text="Pay",command=verify_pay)
                    B1.grid(row=7,columnspan=2,padx=10,pady=10)

                    B2=ttk.Button(Pframe,text="Cancel",command=cancel_pay)
                    B2.grid(row=8,columnspan=2,padx=10,pady=10)

                    Pframe.pack()
                    pay.mainloop()

                def before_ship():
                    frame5.pack_forget()
                    ship()
                    
                frame5=Frame(canvas,borderwidth=30,bg="snow")
                var1 = IntVar()
                var2 = IntVar()
                var3 = IntVar()
                global overnight_delivery
                
                LD=Label(frame5,text="Additional Details:",font="times 15",bg="snow")
                LD.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

                LD3=Label(frame5,text="Overnight Delivery",bg="snow")
                LD3.grid(row=1,column=0,columnspan=2,padx=5,pady=10)
    
                RD3=ttk.Radiobutton(frame5,text="Yes",variable=var1,value=400)
                if (radio1==500):
                    RD3.invoke()
                RD3.grid(row=2,column=0)
                RD4=ttk.Radiobutton(frame5,text="No",variable=var1,value=0)
                RD4.grid(row=2,column=1)

                LD4=Label(frame5,text="Special Handling",bg="snow")
                LD4.grid(row=1,column=2,columnspan=2,padx=5,pady=10)
                RD5=ttk.Radiobutton(frame5,text="Yes",variable=var2,value=100)
                if (radio2!=0):
                    RD5.invoke()
                RD5.grid(row=2,column=2)
                RD6=ttk.Radiobutton(frame5,text="No",variable=var2,value=0)
                RD6.grid(row=2,column=3)

                LD5=Label(frame5,text="Total Packages:",bg="snow")
                LD5.grid(row=3,column=0,padx=10,pady=20)
                ED5=ttk.Entry(frame5)
                ED5.grid(row=3,column=1,padx=10,pady=20)
                ED5.insert(END,insert1)
    
                LD5=Label(frame5,text="Total Weight(Kg):",bg="snow")
                LD5.grid(row=3,column=2,padx=10,pady=20)
                ED6=ttk.Entry(frame5)
                ED6.grid(row=3,column=3,padx=10,pady=20)
                ED6.insert(END,insert2)
    
                LD5=Label(frame5,text="Total Chargers(Rs):",bg="snow")
                LD5.grid(row=3,column=4,padx=10,pady=20)
                ED7=ttk.Entry(frame5)
                ED7.grid(row=3,column=5,padx=10,pady=20)
                ED7.insert(END,insert3)


                LD6=Label(frame5,text="Payment",bg="snow")
                LD6.grid(row=6,column=0,padx=10,pady=15)
                RD7=ttk.Radiobutton(frame5,text="Sender(Cash)",variable=var3,value=1)
                RD8=ttk.Radiobutton(frame5,text="Recipient(Cash)",variable=var3,value=2)
                RD9=ttk.Radiobutton(frame5,text="Credit Card",variable=var3,value=3)
                RD10=ttk.Radiobutton(frame5,text="Check",variable=var3,value=4)
                RD7.grid(row=6,column=1)
                RD8.grid(row=6,column=2)
                RD9.grid(row=6,column=3)
                RD10.grid(row=6,column=4)

                BD0=ttk.Button(frame5,text="Back",command=additional_to_ship_form)
                BD0.grid(row=12,column=1,padx=10,pady=10) 

                BD1=ttk.Button(frame5,text="Check Charges",command=charges)
                BD1.grid(row=12,column=4,padx=10,pady=10)

                BD2=ttk.Button(frame5,text="Ship",command=before_ship)
                if(overnight_delivery==0):
                    BD2.state(["disabled"])
                else:
                    BD2.state(["!disabled"])
                BD2.grid(row=12,column=5,padx=20,pady=10)

                global flag
                if(flag==1):
                    flag=0
                    menu(user1,pas1)
                else:
                    frame5.pack(pady=50)
                    
                if(mode==3 and insert1!=0 and insert2!=0):
                    payment()
    
            additional_window(0,0,'Click on check charges',0,0,0)
            
            

        conn = sqlite3.connect('database.db')
        con = conn.cursor()
        con.execute("SELECT * FROM user WHERE username='%s'"%user1)
        temp=con.fetchone()

        frame4=Frame(canvas,borderwidth=30,bg="snow")

        LD=Label(frame4,text="Fill the details:",font="times 15",bg="snow")
        LD.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

        LD1=Label(frame4,text="From Address:",font="times 15",bg="snow")
        LD1.grid(row=1,columnspan=2,padx=10,pady=15)

        LD2=Label(frame4,text="Your Name",bg="snow")
        LD2.grid(row=2,column=1,padx=10,pady=10)
        ED2=ttk.Entry(frame4)
        ED2.insert(10,temp[0])
        ED2.grid(row=2,column=2,padx=10,pady=10)

        LD3=Label(frame4,text="Company",bg="snow")
        LD3.grid(row=3,column=1,padx=10,pady=10)
        ED3=ttk.Entry(frame4)
        ED3.insert(10,"L.P.U")
        ED3.grid(row=3,column=2,padx=10,pady=10)

        LD4=Label(frame4,text="Country/Location",bg="snow")
        LD4.grid(row=4,column=1,padx=10,pady=10)
        ED4=ttk.Entry(frame4)
        ED4.insert(10,"India")
        ED4.grid(row=4,column=2,padx=10,pady=10)

        LD5=Label(frame4,text="Address",bg="snow")
        LD5.grid(row=5,column=1,padx=10,pady=15)
        ED5=ttk.Entry(frame4)
        ED5.insert(10,"L.P.U,NH-1,Phagwara,Punjab")
        ED5.grid(row=5,column=2,padx=10,pady=10)

        LD6=Label(frame4,text="Postal code",bg="snow")
        LD6.grid(row=6,column=1,padx=10,pady=10)
        ED6=ttk.Entry(frame4)
        ED6.insert(10,"144401")
        ED6.grid(row=6,column=2,padx=10,pady=10)

        LD7=Label(frame4,text="City",bg="snow")
        LD7.grid(row=7,column=1,padx=10,pady=10)
        ED7=ttk.Entry(frame4)
        ED7.insert(10,"Phagwara")
        ED7.grid(row=7,column=2,padx=10,pady=10)

        LD8=Label(frame4,text="Phone",bg="snow")
        LD8.grid(row=8,column=1,padx=10,pady=10)
        ED8=ttk.Entry(frame4)
        ED8.insert(10,temp[1])
        ED8.grid(row=8,column=2,padx=10,pady=10)

        LDA1=Label(frame4,text="To Address:",font="times 15",bg="snow")
        LDA1.grid(row=1,column=3,columnspan=2,padx=20,pady=15)

        LDA2=Label(frame4,text="Recipient name",bg="snow")
        LDA2.grid(row=2,column=4,padx=15,pady=10)
        EDA2=ttk.Entry(frame4)
        EDA2.grid(row=2,column=5,padx=15,pady=10)

        LDA3=Label(frame4,text="Company",bg="snow")
        LDA3.grid(row=3,column=4,padx=15,pady=10)
        EDA3=ttk.Entry(frame4)
        EDA3.grid(row=3,column=5,padx=15,pady=10)

        LDA4=Label(frame4,text="Country/Location",bg="snow") 
        LDA4.grid(row=4,column=4,padx=10,pady=10) 
        EDA4=ttk.Entry(frame4)
        EDA4.grid(row=4,column=5,padx=10,pady=10)

        LDA5=Label(frame4,text="Address",bg="snow")
        LDA5.grid(row=5,column=4,padx=10,pady=15)
        EDA5=ttk.Entry(frame4)
        EDA5.grid(row=5,column=5,padx=10,pady=10)

        LDA6=Label(frame4,text="Postal code",bg="snow")
        LDA6.grid(row=6,column=4,padx=10,pady=10)
        EDA6=ttk.Entry(frame4)
        EDA6.grid(row=6,column=5,padx=10,pady=10)

        LDA7=Label(frame4,text="City",bg="snow")
        LDA7.grid(row=7,column=4,padx=10,pady=10)
        EDA7=ttk.Entry(frame4)
        EDA7.grid(row=7,column=5,padx=10,pady=10)

        LDA8=Label(frame4,text="Phone",bg="snow")
        LDA8.grid(row=8,column=4,padx=10,pady=10)
        EDA8=ttk.Entry(frame4)
        EDA8.grid(row=8,column=5,padx=10,pady=10)

        BD1=ttk.Button(frame4,text="Continue",command=additional)
        BD1.grid(row=9,column=5,padx=20,pady=10)

        BD1=ttk.Button(frame4,text="Back",command=ship_form_to_menu)
        BD1.grid(row=9,column=4,padx=20,pady=10)

        frame4.pack(pady=50)

    # To ask whether you want to logout or not
    def logout():
        temp=tkMessageBox.askquestion("Logout","Do you want to Logout?")
        if temp == 'yes':
            remove_menu()
            login()

    # To change password
    def password():
        remove_menu()
    
        def password_to_menu():
            frame7.pack_forget()
            menu(user1,pas1)
            
        def change_password():
            pass0=E71.get()
            pass1=E72.get()
            if(pas1==pass0):
                conn=sqlite3.connect('database.db')
                con = conn.cursor()
                con.execute("UPDATE user SET password=? WHERE username=?",(pass1,user1))
                conn.commit()
                conn.close()
                tkMessageBox.showinfo("Warning","You are about to redirected to login page..")
                frame7.pack_forget()
                login()
            else:
                tkMessageBox.showerror("Warning","Incorrect existing password..")

        frame7= Frame(canvas,borderwidth=30,bg="snow")
        L70= Label(frame7,text="Change Password :",font="times 15",bg="snow")
        L70.grid(row=0,column=1,columnspan=2,padx=10,pady=15)
        L71= Label(frame7,text="Old Password :",bg="snow")
        L71.grid(row=1,column=1,padx=10,pady=15)
        E71= ttk.Entry(frame7)
        E71.grid(row=1,column=2,padx=10,pady=15)
        L72= Label(frame7,text="New Password :",bg="snow")
        L72.grid(row=2,column=1,padx=10,pady=15)
        E72= ttk.Entry(frame7)
        E72.grid(row=2,column=2,padx=10,pady=15)
        B71=ttk.Button(frame7,text="Change",command=change_password)
        B71.grid(row=3,column=1,columnspan=2,padx=10,pady=15)
        B72=ttk.Button(frame7,text="Back",command=password_to_menu)
        B72.grid(row=4,column=1,columnspan=2,padx=10,pady=15)
        frame7.pack(pady=50)

            
    # To print all the shipments by logged In user
    def all_shipments():
        def all_shipments_to_menu():
            frame9.pack_forget()
            menu(user1,pas1)
            
        remove_menu()
        conn=sqlite3.connect('database.db')
        con = conn.cursor()
        con.execute("SELECT track,sname,rname,rcompany,rphone,raddress,ship_date,delivery_date FROM shipments WHERE username='%s'"%user1)
        frame9=Frame(canvas,borderwidth=30,bg="snow")
        rows = []
        lis=['Consignment no.','Sender Name','Receiver Name','Receiver Company','Receiver Phone','Receiver Address','Ship Date','Delivery Date']
        for j in range(8):
            e= ttk.Entry(frame9)
            e.grid(row=0, column=j, sticky=NSEW ,pady=10)
            e.insert(END,lis[j])
            e.configure(state='readonly')

        i=1
        for r in con:
            cols = []
            for j in range(8):
                e = ttk.Entry(frame9)
                e.grid(row=i, column=j, sticky=NSEW)
                e.insert(END,r[j])
                e.configure(state='readonly')
                cols.append(e)
            rows.append(cols)
            i+=1

        B91=Button(frame9,text="Back",command=all_shipments_to_menu)
        B91.grid(row=i+2,columnspan=8,padx=10,pady=20)
        frame9.pack(pady=50)

    # to call track from menu
    def menu_to_track():
        remove_menu()
        track(1,user1,pas1)

    #change_background()
    Aframe=Frame(canvas,borderwidth=10,bg="snow")
    Alabel=Label(Aframe,text='MENU',font="times 20 bold",bg="snow")
    Alabel.grid(row=0,column=0,pady=30)

    Abutton1=ttk.Button(Aframe,text="Ship",command=ship_form)
    Abutton1.grid(row=1,column=0,padx=70,pady=10)
    Abutton2=ttk.Button(Aframe,text="Track",command=menu_to_track)
    Abutton2.grid(row=2,column=0,padx=70,pady=10)
    Abutton3=ttk.Button(Aframe,text="All Shipments",command=all_shipments)
    Abutton3.grid(row=3,column=0,padx=70,pady=10)
    Abutton4=ttk.Button(Aframe,text="Change Password",command=password)
    Abutton4.grid(row=4,column=0,padx=70,pady=10)
    Abutton4=ttk.Button(Aframe,text="Logout",command=logout)
    Abutton4.grid(row=5,column=0,padx=70,pady=10)

    Alabel=Label(Aframe,text='C M S',font="times 20 bold",bg="snow")
    Alabel.grid(row=6,column=0,pady=30)
    Aframe.pack(pady=50)

#Main cms window    

Mframe=Frame(canvas,borderwidth=30,bg="snow")
label=Label(Mframe,text='Welcome',font="times 20 bold",bg="snow")
label.grid(row=0,columnspan=4,pady=20)

img=PhotoImage(file = 'logo.gif')
imge = Label(Mframe, image = img)
imge.grid(row=1,columnspan=4,pady=20)

button1=ttk.Button(Mframe,text="Login",command=login_remove)
button1.grid(row=2,column=1,padx=10,pady=20)
button2=ttk.Button(Mframe,text="New user",command=newuser_remove)
button2.grid(row=2,column=2,padx=10,pady=20)
button3=ttk.Button(Mframe,text="Track Consignment",command=track_remove)
button3.grid(row=2,column=3,padx=10,pady=20)

label=Label(Mframe,text='Courier Management System',font="times 20",bg="snow")
label.grid(row=3,columnspan=4,pady=30)
link = Label(Mframe, text="Created By: Varinder Singh", fg="blue", cursor="hand2")
link.grid(row=4,columnspan=4,pady=10)
link.bind("<Button-1>", callback)

Mframe.pack(pady=50)

# Create main cms window again
def main():
    Mframe.pack(pady=50)
    
canvas.pack()
top.mainloop()
