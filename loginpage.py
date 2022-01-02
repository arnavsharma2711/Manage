from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import time
import sqlite3
import os
from email.message import EmailMessage
import smtplib
import email_pass
import pyglet

class loginClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.title("Login Page | MANAGÉ - Inventory Management System")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\login_icon.png")
        self.root.iconphoto(False,self.icon_main)
        pyglet.font.add_file('file.ttf')


        #=========Variable=============
        self.var_empid=StringVar()
        self.var_password=StringVar()
        self.var_otp=StringVar()
        self.var_otp_test=StringVar()
        self.otp=''
        self.var_newPass=StringVar()
        self.var_confirmPass=StringVar()
        self.image=ImageTk.PhotoImage(file="images\login.png")
        self.lbl_inage=Label(self.root,image=self.image,bd=0).place(x=150,y=80)
        
        loginFrame=Frame(self.root,bd=0,bg="#ffffff")
        loginFrame.place(x=700,y=110,width=450,height=500)

        lbl_title1=Label(loginFrame,text="MANAGÉ",font=("Gloria Hallelujah",30,"bold"),bg="#ffffff").pack(side=TOP,fill=Y)
        lbl_title1=Label(loginFrame,text="Inventory Management System",font=("Gloria Hallelujah",20,"bold"),bg="#ffffff").pack(side=TOP,fill=Y)

        lbl_EmployeeID=Label(loginFrame,text="Employee ID",font=("candara",20),bg="#ffffff").place(x=50,y=140)
        txt_EmployeeID=Entry(loginFrame,textvariable=self.var_empid,font=("candara",15),bg="#ececec").place(x=55,y=180,width=300,height=35)

        lbl_Password=Label(loginFrame,text="Password",font=("candara",20),bg="#ffffff").place(x=50,y=260)
        txt_Password=Entry(loginFrame,textvariable=self.var_password,show='*',font=("candara",15),bg="#ececec").place(x=55,y=300,width=300,height=35)
        self.icon_empid=PhotoImage(file="images\log.png")
        self.icon_pass=PhotoImage(file="images\passwordforgot.png")

        btn_login=Button(loginFrame,text=" Login",command=self.login,image=self.icon_empid,compound=LEFT,padx=5,anchor="w",font=("candara",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").place(x=20,y=400,width=140)
        btn_forgot=Button(loginFrame,text="Forgot Password",command=self.forgot,image=self.icon_pass,compound=LEFT,padx=5,anchor="w",font=("candara",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").place(x=175,y=400)
        
    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            os.system("python create_db.py")
            if self.var_empid.get()=="" or self.var_password.get()=="":
                messagebox.showerror('Invaild Input',"All feilds are required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? and password=?",(
                    self.var_empid.get(),
                    self.var_password.get()
            ))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Invaild Input',"Invalid Employee ID/Password",parent=self.root)
                else:
                    self.login_name()
                    if user[0]=="Admin":                        
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def login_name(self):
        file=open(f'login.txt','w')
        file.write(self.var_empid.get())

    def forgot(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror('Invaild Input',"Employee ID is required",parent=self.root)
            else:
                cur.execute("select email,name from employee where eid=?",(self.var_empid.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror('Invaild Input',"Invalid Employee ID",parent=self.root)
                else:
                    chk=self.send_email(email[0],email[1])
                    if chk!='s':
                        messagebox.showerror('Error',"Connection Error, Try Again Later",parent=self.root)
                    else:
                        self.verification_win=Toplevel(self.root)
                        self.verification_win.title('Verification | Reset Password')
                        self.verification_win.geometry('400x200+500+100')
                        self.verification_win.focus_force()
                        self.verification_win.config(bg="white")
                        
                        title=Label(self.verification_win,text="Verify Its You",font=("candara",30),bg="#ffffff").pack(side=TOP,fill=X)
                        lbl_reset1=Label(self.verification_win,text="Enter OTP",font=("candara",20),bg="#ffffff").place(x=10,y=70)
                        lbl_reset2=Label(self.verification_win,text="(Sent on registered email)",font=("candara",10),bg="#ffffff").place(x=140,y=85)
                        txt_otp_test=Entry(self.verification_win,textvariable=self.var_otp,show='*',font=("candara",20),bg="lightgrey").place(x=15,y=110,width=210,height=30)
                        self.btn_submit=Button(self.verification_win,text="Submit",command=self.otp_verification,font=("candara"),bg="#4caf50",bd=3,cursor="hand2")
                        self.btn_submit.place(x=235,y=109,width=150,height=30)
                        self.lbl_spam=Label(self.verification_win,text="(If you have not recieved your OTP, please check your spam.)",font=("candara",10),bg="#ffffff")
                        self.lbl_spam.after(5000, self.show_spam)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
           
    def show_spam(self):
        self.lbl_spam.place(x=10,y=150)

    def otp_verification(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.verification_win.destroy()
            self.reset_pass_win=Toplevel(self.root)
            self.reset_pass_win.title('Reset Password')
            self.reset_pass_win.geometry('400x250+500+100')
            self.reset_pass_win.focus_force()
            self.reset_pass_win.config(bg="white")
            
            title=Label(self.reset_pass_win,text="Reset Password",font=("candara",30),bg="#ffffff").pack(side=TOP,fill=X)
            lbl_newPass=Label(self.reset_pass_win,text="New Password",font=("candara",17),bg="#ffffff").place(x=10,y=70)
            txt_newPass=Entry(self.reset_pass_win,textvariable=self.var_newPass,show='*',font=("candara",20),bg="lightgrey").place(x=15,y=107,width=210,height=30)
            lbl_confirmPass=Label(self.reset_pass_win,text="Confirm Password",font=("candara",17),bg="#ffffff").place(x=10,y=150)
            txt_confirmPass=Entry(self.reset_pass_win,textvariable=self.var_confirmPass,show='*',font=("candara",20),bg="lightgrey").place(x=15,y=187,width=210,height=30)
            self.btn_update=Button(self.reset_pass_win,text="Update",command=self.pass_update,font=("candara"),bg="#2196f3",bd=3,cursor="hand2")
            self.btn_update.place(x=235,y=186,width=150,height=30)
        else:
            messagebox.showerror("Error",f"Invalid OTP, Try Again",parent=self.root)
            self.verification_win.focus_force()

    
    def send_email(self,to_,name_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime("%H%M%S"))+int(time.strftime("%S"))

        msg = EmailMessage()
        msg.set_content(f'Hello {str(name_)},\n\nYour OTP for your IMS acoount to reset password request is {str(self.otp)}.\nIf you have not inciated this request please contact the administrator.\n\nWith Regards, \nIMS Team')
        msg['Subject'] = f'IMS-Reset Password OTP'
        msg['From'] = 'gamerash007@gmail.com'
        msg['To'] = to_
        s.send_message(msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

    def pass_update(self):
        if self.var_newPass.get()=="" or self.var_confirmPass.get()=="":
            messagebox.showerror("Error",f"All Fields not entered",parent=self.root)
            self.reset_pass_win.focus_force()
        elif self.var_newPass.get()!=self.var_confirmPass.get():
            messagebox.showerror("Error",f"Confirm password and new password are not same.",parent=self.root)
            self.reset_pass_win.focus_force()
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("update employee SET password=? where eid=?",(self.var_newPass.get(),self.var_empid.get(),))
                con.commit()            
                messagebox.showinfo("Sucess","Password updated sucessfully",parent=self.reset_pass_win)
                self.reset_pass_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=loginClass(root)
    root.mainloop()