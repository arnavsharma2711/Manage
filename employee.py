from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import re
import smtplib
import email_pass
from email.message import EmailMessage

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+225+150")
        self.root.title("--> Employee Menu ")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\employe.png")
        self.root.iconphoto(False,self.icon_main)
        self.root.focus_force()
        #====Variables====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        #====SearchFrame++++
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("gordy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #===option====
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Email","Employee ID","Address"),state='readonly',justify=CENTER,font=("arial",15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("groudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("groudy old style",15),bg="lightgreen",cursor="hand2").place(x=435,y=9,width=150,height=28)

        #====Title====
        title=Label(self.root,text="Employee Details",font=("arial",15),bg="#0f4d7d",fg="#ffffff").place(x=50,y=100,width=1000)

        #===Content====
        #Row1
        lbl_empid=Label(self.root,text="Employee ID",font=("arial",15),bg="#ffffff").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("arial",15),bg="#ffffff").place(x=400,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("arial",15),bg="#ffffff").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("arial",15),bg="lightyellow").place(x=180,y=150,width=180)
        cmd_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("arial",15))
        cmd_gender.place(x=500,y=150,width=180)
        cmd_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("arial",15),bg="lightyellow").place(x=850,y=150,width=180)

        #===ROw2
        lbl_name=Label(self.root,text="Name",font=("arial",15),bg="#ffffff").place(x=50,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("arial",15),bg="#ffffff").place(x=400,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("arial",15),bg="#ffffff").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("arial",15),bg="lightyellow").place(x=180,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_doj,font=("arial",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_dob,font=("arial",15),bg="lightyellow").place(x=850,y=190,width=180)

        #===ROw3
        lbl_email=Label(self.root,text="Email",font=("arial",15),bg="#ffffff").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("arial",15),bg="#ffffff").place(x=400,y=230)
        lbl_userType=Label(self.root,text="User Type",font=("arial",15),bg="#ffffff").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("arial",15),bg="lightyellow").place(x=180,y=230,width=180)
        txt_password=Entry(self.root,textvariable=self.var_pass,show='*',font=("arial",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmd_usertype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("arial",15))
        cmd_usertype.place(x=850,y=230,width=180)
        cmd_usertype.current(0)

        #===ROw4
        lbl_address=Label(self.root,text="Address",font=("arial",15),bg="#ffffff").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("arial",15),bg="#ffffff").place(x=750,y=270)
        
        self.txt_address=Text(self.root,font=("arial",15),bg="lightyellow")
        self.txt_address.place(x=180,y=270,width=310,height=65)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("arial",15),bg="lightyellow").place(x=850,y=270,width=180)

        #===button
        btn_add=Button(self.root,text="Save",command=self.add,font=("groudy old style",15),bg="#2196f3",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("groudy old style",15),bg="#4caf50",cursor="hand2").place(x=645,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15),bg="#f44336",cursor="hand2").place(x=780,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("groudy old style",15),bg="#607d8b",cursor="hand2").place(x=920,y=305,width=110,height=28)

        #====Employee Details====
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)



        self.EmployeeTable.heading("eid",text="Employee ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")

        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=90)
        self.EmployeeTable.column("doj",width=90)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#====================================================================================
#====Function====

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","Email Address is required",parent=self.root)
            elif self.email_check(self.var_email.get())==FALSE:
                messagebox.showerror("Error","Invalid Email Address",parent=self.root)
            elif self.var_contact.get()=="":
                messagebox.showerror("Error","Contact Number is required",parent=self.root)
            elif self.number_check(self.var_contact.get())==FALSE:
                messagebox.showerror("Error","Invalid Contact Number",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                cur.execute("select * from employee where email=?",(self.var_email.get(),))
                email=cur.fetchone()
                cur.execute("select * from employee where contact=?",(self.var_contact.get(),))
                contact=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID is already assigined, try different",parent=self.root)
                elif email!=None:
                    messagebox.showerror('Invaild Input',"Email address already exist",parent=self.root)
                elif contact!=None:
                    messagebox.showerror('Invaild Input',"Contact Number already exist",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,utype,address,salary,password) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0',END),
                            self.var_salary.get(),    
                            self.var_pass.get(),
                        ))

                    con.commit()
                    chk=self.send_email_newMember(self.var_email.get(),self.var_name.get())
                    if chk!='s':
                        messagebox.showerror('Error',"Connection Error, Try Again Later",parent=self.root)
                    messagebox.showinfo("Sucess","Employee Added Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_utype.set(row[7])
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[8]),
        self.var_salary.set(row[9])            
        self.var_pass.set(row[10])
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                elif self.var_email.get()=="":
                    messagebox.showerror("Error","Email Address is required",parent=self.root)
                elif self.email_check(self.var_email.get())==FALSE:
                    messagebox.showerror("Error","Invalid Email Address",parent=self.root)
                elif self.var_contact.get()=="":
                    messagebox.showerror("Error","Contact Number is required",parent=self.root)
                elif self.number_check(self.var_contact.get())==FALSE:
                    messagebox.showerror("Error","Invalid Contact Number",parent=self.root)
                cur.execute("select * from employee where email=? and eid!=?",(self.var_email.get(),self.var_emp_id.get(),))
                email=cur.fetchone()
                if email!=None:
                    messagebox.showerror('Invaild Input',"Email address already exist",parent=self.root)
                cur.execute("select * from employee where contact=? and eid!=?",(self.var_contact.get(),self.var_emp_id.get(),))
                contact=cur.fetchone()
                if contact!=None:
                    messagebox.showerror('Invaild Input',"Contact Number already exist",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,utype=?,address=?,salary=? where eid=?",(
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0',END),
                            self.var_salary.get(),                        
                            self.var_emp_id.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Sucess","Employee Updated Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Sucess","Employee Deleted Sucessfully",parent=self.root)
                        self.root.focus_force()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_email.set("")
        self.var_pass.set("")
        self.var_utype.set("Employee")
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,""),
        self.var_salary.set("")  
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:

            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by Option",parent=self.root) 
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input is required",parent=self.root) 
            elif self.var_searchby.get()=="Employee ID":
                cur.execute("select * from employee where eid LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def email_check(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex, email)

    def number_check(self,number):
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        return Pattern.match(number)

    def send_email_newMember(self,to_,name_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()

        email_=email_pass.email_
        pass_=email_pass.pass_
        s.login(email_,pass_)

        msg = EmailMessage()
        msg.set_content(f'Hello {str(name_)},\n\nYour IMS acoount has been created.\nThis mailing address will be used for all future distribution of information from the administrator to you.\n\nWith Regards, \nIMS Team')
        msg['Subject'] = f'Welcome to IMS'
        msg['From'] = 'gamerash007@gmail.com'
        msg['To'] = to_
        s.send_message(msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()