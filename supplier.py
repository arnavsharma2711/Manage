from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+225+150")
        self.root.title("--> Supplier Menu ")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\supplier.png")
        self.root.iconphoto(False,self.icon_main)
        self.root.focus_force()
         #====Variables====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.var_sup_id=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_location=StringVar()

       #====SearchFrame++++
        SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("gordy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=545,y=65,width=485,height=70)

        #===option====
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Supplier ID","Description","Location"),state='readonly',justify=CENTER,font=("arial",12))
        cmd_search.place(x=10,y=10,width=140,height=28)
        cmd_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("groudy old style",15),bg="lightyellow").place(x=160,y=10,width=180)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("groudy old style",15),bg="lightgreen",cursor="hand2").place(x=350,y=9,width=120,height=28)

        #====Title====
        title=Label(self.root,text="Supplier Details",font=("arial",15),bg="#0f4d7d",fg="#ffffff").place(x=50,y=20,width=1000)

        #===Content====
        lbl_sup_id=Label(self.root,text="Supplier ID",font=("arial",15),bg="#ffffff").place(x=60,y=80)
        txt_sup_id=Entry(self.root,textvariable=self.var_sup_id,font=("arial",15),bg="lightyellow").place(x=190,y=80,width=200)
        
        lbl_name=Label(self.root,text="Name",font=("arial",15),bg="#ffffff").place(x=60,y=132)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("arial",15),bg="lightyellow").place(x=190,y=132,width=200)

        lbl_location=Label(self.root,text="Location",font=("arial",15),bg="#ffffff").place(x=60,y=184)
        txt_location=Entry(self.root,textvariable=self.var_location,font=("arial",15),bg="lightyellow").place(x=190,y=184,width=200)
        
        lbl_contact=Label(self.root,text="Contact",font=("arial",15),bg="#ffffff").place(x=60,y=236)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("arial",15),bg="lightyellow").place(x=190,y=236,width=230)
                
        lbl_address=Label(self.root,text="Description",font=("arial",15),bg="#ffffff").place(x=60,y=288)
        self.txt_desc=Text(self.root,font=("arial",15),bg="lightyellow")
        self.txt_desc.place(x=190,y=288,width=310,height=65)
        
        #===button
        btn_add=Button(self.root,text="Save",command=self.add,font=("groudy old style",15),bg="#2196f3",cursor="hand2").place(x=60,y=400,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("groudy old style",15),bg="#4caf50",cursor="hand2").place(x=180,y=400,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15),bg="#f44336",cursor="hand2").place(x=300,y=400,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("groudy old style",15),bg="#607d8b",cursor="hand2").place(x=420,y=400,width=110,height=28)

        #====Supplier Details====
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=545,y=150,width=485,height=300)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.SupplierTable=ttk.Treeview(emp_frame,columns=("sid","name","location","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)



        self.SupplierTable.heading("sid",text="Supplier ID")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("location",text="Location")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("desc",text="Description")

        self.SupplierTable["show"]="headings"
        
        self.SupplierTable.column("sid",width=40)
        self.SupplierTable.column("name",width=50)
        self.SupplierTable.column("location",width=40)
        self.SupplierTable.column("contact",width=40)
        self.SupplierTable.column("desc",width=50)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#====================================================================================
#====Function====

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier ID is already assigined, try different",parent=self.root)
                    self.root.focus_force()
                else:
                    cur.execute("Insert into supplier (sid,name,location,contact,desc) values(?,?,?,?,?)",(
                            self.var_sup_id.get(),
                            self.var_name.get(),
                            self.var_location.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0',END),
                        ))

                    con.commit()
                    messagebox.showinfo("Sucess","Supplier Added Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        self.var_sup_id.set(row[0])
        self.var_name.set(row[1])
        self.var_location.set(row[2])
        self.var_contact.set(row[3])
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[4]),   
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,location=?,contact=?,desc=? where sid=?",(
                            self.var_name.get(),
                            self.var_location.get(),
                            self.var_contact.get(),
                            self.txt_desc.get('1.0',END),                    
                            self.var_sup_id.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Sucess","Supplier Updated Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get()=="":
                messagebox.showerror("Error","Supplier ID must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where sid=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where sid=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Sucess","Supplier Deleted Sucessfully",parent=self.root)
                        self.root.focus_force()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_id.set("")
        self.var_name.set("")
        self.var_location.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,""),
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
            elif self.var_searchby.get()=="Supplier ID":
                cur.execute("select * from supplier where sid LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            elif self.var_searchby.get()=="Description":
                cur.execute("select * from supplier where desc LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
            else:
                cur.execute("select * from supplier where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root) 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
                

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()