from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+225+150")
        self.root.title("--> Product Menu ")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\product.png")
        self.root.iconphoto(False,self.icon_main)
        self.root.focus_force()
         #====Variables====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.list_cat=[]
        self.list_sup=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()


        #====Title====
        title=Label(self.root,text="Product Details",font=("arial",15),bg="#0f4d7d",fg="#ffffff").place(x=50,y=20,width=1000)

        product_frame=LabelFrame(self.root,text="Manage Product",font=("gordy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=55,y=60,width=480,height=410)

        #===Content====
        lbl_category=Label(product_frame,text="Category",font=("arial",15),bg="#ffffff").place(x=30,y=20)
        lbl_supplier=Label(product_frame,text="Supplier",font=("arial",15),bg="#ffffff").place(x=30,y=75)
        lbl_name=Label(product_frame,text="Product Name",font=("arial",15),bg="#ffffff").place(x=30,y=130)
        lbl_price=Label(product_frame,text="Price",font=("arial",15),bg="#ffffff").place(x=30,y=185)
        lbl_quantity=Label(product_frame,text="Quantity",font=("arial",15),bg="#ffffff").place(x=30,y=240)
        lbl_status=Label(product_frame,text="Status",font=("arial",15),bg="#ffffff").place(x=30,y=295)
        
        cmd_category=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.list_cat,state='readonly',justify=CENTER,font=("arial",15))
        cmd_category.place(x=220,y=20,width=200)
        cmd_category.current(0)
        cmd_supplier=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.list_sup,state='readonly',justify=CENTER,font=("arial",15))
        cmd_supplier.place(x=220,y=75,width=200)
        cmd_supplier.current(0)
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("arial",15),bg="lightyellow").place(x=220,y=130,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("arial",15),bg="lightyellow").place(x=220,y=185,width=200)
        txt_quantity=Entry(product_frame,textvariable=self.var_quantity,font=("arial",15),bg="lightyellow").place(x=220,y=240,width=200)
        cmd_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("arial",15))
        cmd_status.place(x=220,y=295,width=200)
        cmd_status.current(0)
        
        #===button
        btn_add=Button(product_frame,text="Save",command=self.add,font=("groudy old style",15),bg="#2196f3",cursor="hand2").place(x=25,y=345,width=100,height=28)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("groudy old style",15),bg="#4caf50",cursor="hand2").place(x=135,y=345,width=100,height=28)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("groudy old style",15),bg="#f44336",cursor="hand2").place(x=245,y=345,width=100,height=28)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("groudy old style",15),bg="#607d8b",cursor="hand2").place(x=355,y=345,width=100,height=28)

        #====SearchFrame++++
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("gordy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=550,y=60,width=490,height=70)

        #===option====
        cmd_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("arial",15))
        cmd_search.place(x=10,y=10,width=140)
        cmd_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("groudy old style",15),bg="lightyellow").place(x=160,y=10,width=210)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("groudy old style",15),bg="lightgreen",cursor="hand2").place(x=380,y=9,width=100,height=28)

       
        #====Product Details====
        pro_frame=Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=549,y=135,width=491,height=335)

        scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)
        
        
        self.productTable=ttk.Treeview(pro_frame,columns=("pid","category","supplier","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)



        self.productTable.heading("pid",text="Pro. ID")
        self.productTable.heading("category",text="Category")
        self.productTable.heading("supplier",text="Supplier")
        self.productTable.heading("name",text="Name") 
        self.productTable.heading("price",text="Price")
        self.productTable.heading("quantity",text="Quantity")
        self.productTable.heading("status",text="Status")

        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=40)
        self.productTable.column("category",width=75)
        self.productTable.column("supplier",width=80)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=60)
        self.productTable.column("quantity",width=50)
        self.productTable.column("status",width=50)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#====================================================================================
#====Function====
    
    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:     
            self.list_cat.append("Empty")
            self.list_sup.append("Empty")

            cur.execute("Select name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.list_cat[:]
                self.list_cat.append("Select")
                for i in cat:
                    self.list_cat.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.list_sup[:]
                self.list_sup.append("Select")
                for i in sup:
                    self.list_sup.append(i[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_sup.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","Category, Supplier and Product Name must be required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product Name is already assigined, try different",parent=self.root)
                else:
                    if int(self.var_quantity.get())<=0:
                        self.var_status.set("Inactive")
                    cur.execute("Insert into product (category,supplier,name,price,quantity,status) values(?,?,?,?,?,?)",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_quantity.get(),
                            self.var_status.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Sucess","Product Added Sucessfully")
                    self.root.focus_force()
                    self.show()
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])   
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select Product form list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product Name",parent=self.root)
                else:
                    if int(self.var_quantity.get())<=0:
                        self.var_status.set("Inactive")
                    cur.execute("Update product set category=?, supplier=?, name=?, price=?, quantity=?, status=? where pid=?",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_quantity.get(),
                            self.var_status.get(),
                            self.var_pid.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Sucess","Product Updated Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_sup.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","Category, Supplier and Product Name must be required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product Name",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Sucess","Product Deleted Sucessfully",parent=self.root)
                        self.root.focus_force()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_name.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_status.set("Active")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by Option",parent=self.root) 
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select Input is required",parent=self.root) 

            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 


if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()