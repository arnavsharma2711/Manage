from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile

class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.title("Inventory Management System | Developed by Arnav Sharma")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\logo.png")
        self.root.iconphoto(False,self.icon_main)
        
        #=========Variable=======
        self.list_cart=[]
        self.chk_print=0
        self.var_search=StringVar()
        self.var_customer_name=StringVar()
        self.var_contact_no=StringVar()
        self.var_pid=StringVar()
        self.var_pro_name=StringVar()
        self.var_pro_price=StringVar()
        self.var_pro_qty=StringVar()
        self.var_pro_stock=StringVar()
        
        #====Title====        
        title=Label(self.root,text="Inventory Management System",image=self.icon_main,compound=LEFT,font=("times new roman",40,"bold"),bg="#0063B2",fg="#ffffff",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=70)
        
        #====Logout_BTN====
        btn_logout=Button(self.root,text="LOGOUT",command=self.logout,font=("times new roman",17,"bold"),bg="yellow",cursor="hand2").place(x=1200,y=10,height=50,width=140)
        
        #====Header====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t|\t Date: DD-MM-YYY\t|\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====Product_frame
        ProductFrame_Main=Frame(self.root,bd=4,relief=RIDGE,bg="#ffffff")
        ProductFrame_Main.place(x=10,y=110,width=450,height=550)

        pTitle=Label(ProductFrame_Main,text="All Product List",font=("goudy old style",20,"bold"),bg="#262626",fg="#ffffff").pack(side=TOP,fill=X)

        ProductFrame_Search=Frame(ProductFrame_Main,bd=2,relief=RIDGE,bg="#ffffff")
        ProductFrame_Search.place(x=2,y=42,width=438,height=90)

        lbl_search=Label(ProductFrame_Search,text="Search Product | By Name",font=("arial",15,"bold"),bg="#ffffff",fg="green").place(x=2,y=5)

        lbl_name=Label(ProductFrame_Search,text="Product Name",font=("arial",15,"bold"),bg="#ffffff").place(x=2,y=45)
    
        txt_search=Entry(ProductFrame_Search,textvariable=self.var_search,font=("arial",15),bg="lightyellow").place(x=150,y=49,width=150,height=22)
        
        btn_search=Button(ProductFrame_Search,text="Show All",command=self.show,font=("groudy old style",15),bg="#2196f3",fg="#ffffff",cursor="hand2").place(x=310,y=8,width=115,height=23)
        btn_search=Button(ProductFrame_Search,text="Search",command=self.search,font=("groudy old style",15),bg="lightgreen",cursor="hand2").place(x=310,y=48,width=115,height=23)

        #====Product Details====
        ProductFrame_Table=Frame(ProductFrame_Main,bd=3,relief=RIDGE)
        ProductFrame_Table.place(x=1,y=135,width=438,height=380)

        scrolly=Scrollbar(ProductFrame_Table,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame_Table,orient=HORIZONTAL)
        
        self.ProductDetail=ttk.Treeview(ProductFrame_Table,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductDetail.xview)
        scrolly.config(command=self.ProductDetail.yview)



        self.ProductDetail.heading("pid",text="Product ID")
        self.ProductDetail.heading("name",text="Name")
        self.ProductDetail.heading("price",text="Price")
        self.ProductDetail.heading("qty",text="Quantity")
        self.ProductDetail.heading("status",text="Status")
        self.ProductDetail["show"]="headings"        
        self.ProductDetail.column("pid",width=25)
        self.ProductDetail.column("name",width=85)
        self.ProductDetail.column("price",width=35)
        self.ProductDetail.column("qty",width=35)
        self.ProductDetail.column("status",width=30)
        self.ProductDetail.pack(fill=BOTH,expand=1)
        self.ProductDetail.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        lbl_note=Label(ProductFrame_Main,text="Note:- Enter 0 in QTY to REMOVE the PRODUCT from CART",font=("arial",12),bg="#ffffff",fg="red").pack(side=BOTTOM,fill=X)


        #====Customer_Frame===============

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="#ffffff")
        CustomerFrame.place(x=465,y=110,width=440,height=105)

        customerTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15,"bold"),bg="lightgrey",fg="#000000").pack(side=TOP,fill=X)

        lbl_name=Label(CustomerFrame,text="Customer Name",font=("arial",15),bg="#ffffff").place(x=2,y=32)    
        txt_name=Entry(CustomerFrame,textvariable=self.var_customer_name,font=("arial",15),bg="lightyellow").place(x=180,y=33,width=240,height=24)

        lbl_contact=Label(CustomerFrame,text="Customer Contact",font=("arial",15),bg="#ffffff").place(x=2,y=65)    
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact_no,font=("arial",15),bg="lightyellow").place(x=180,y=66,width=240,height=24)

        #====Cart_Frame===============
        CartFrame_Main=Frame(self.root,bd=4,relief=RIDGE,bg="#ffffff")
        CartFrame_Main.place(x=465,y=220,width=440,height=440)

        self.customerTitle=Label(CartFrame_Main,text="CUSTOMER'S CART \t Total Product: 0",font=("goudy old style",15,"bold"),bg="lightgrey",fg="#000000")
        self.customerTitle.pack(side=TOP,fill=X)

        CartFrame_Table=Frame(CartFrame_Main,bd=3,relief=RIDGE)
        CartFrame_Table.place(x=1,y=30,width=428,height=285)

        scrolly=Scrollbar(CartFrame_Table,orient=VERTICAL)
        
        self.CartDetail=ttk.Treeview(CartFrame_Table,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.CartDetail.yview)



        self.CartDetail.heading("pid",text="Product ID")
        self.CartDetail.heading("name",text="Name")
        self.CartDetail.heading("price",text="Price")
        self.CartDetail.heading("qty",text="Quantity")

        self.CartDetail["show"]="headings"
        
        self.CartDetail.column("pid",width=35)
        self.CartDetail.column("name",width=90)
        self.CartDetail.column("price",width=40)
        self.CartDetail.column("qty",width=40)
        self.CartDetail.pack(fill=BOTH,expand=1)
        self.CartDetail.bind("<ButtonRelease-1>",self.get_data_cart)
        self.show_cart()

        CartFrame_Button=Frame(CartFrame_Main,bd=4,relief=RIDGE,bg="#ffffff")
        CartFrame_Button.place(x=1,y=320,width=428,height=110)

        lbl_product_name=Label(CartFrame_Button,text="Product Name",font=("times new roman",15),bg="#ffffff").place(x=2,y=2)    
        txt_product_name=Entry(CartFrame_Button,textvariable=self.var_pro_name,font=("times new roman",15),bg="lightgrey",state='readonly').place(x=4,y=30,width=160,height=22)
        lbl_product_price=Label(CartFrame_Button,text="Price/Item",font=("times new roman",15),bg="#ffffff").place(x=175,y=2)    
        txt_product_price=Entry(CartFrame_Button,textvariable=self.var_pro_price,font=("times new roman",15),bg="lightgrey",state='readonly').place(x=177,y=30,width=115,height=22)
        lbl_product_qty=Label(CartFrame_Button,text="Quantity",font=("times new roman",15),bg="#ffffff").place(x=310,y=2)    
        txt_product_qty=Entry(CartFrame_Button,textvariable=self.var_pro_qty,font=("times new roman",15),bg="lightyellow").place(x=312,y=30,width=95,height=22)
        self.lbl_product_stock=Label(CartFrame_Button,text="In Stock: []",font=("times new roman",15),bg="#ffffff")
        self.lbl_product_stock.place(x=2,y=67)    
       
        btn_search=Button(CartFrame_Button,text="Clear",command=self.clear,font=("groudy old style",13),bg="#607d8b",cursor="hand2").place(x=135,y=68,width=95,height=25)
        btn_search=Button(CartFrame_Button,text="Add / Update to Cart",command=self.add,font=("groudy old style",13,"bold"),bg="#ffcf3b",cursor="hand2").place(x=240,y=67,width=175,height=27)

        #====Billing_Frame===================
        BillingFrame_TextArea=Frame(self.root,bd=4,relief=RIDGE,bg="#ffffff")
        BillingFrame_TextArea.place(x=910,y=110,width=448,height=400)
        bTitle=Label(BillingFrame_TextArea,text="Customer Billing Area",font=("goudy old style",20,"bold"),bg="#ff6e40",fg="#ffffff").pack(side=TOP,fill=X)
        scrolly=Scrollbar(BillingFrame_TextArea,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_billArea=Text(BillingFrame_TextArea,yscrollcommand=scrolly.set)
        self.txt_billArea.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_billArea.yview)
    
        BillingFrame_Button=Frame(self.root,bd=4,relief=RIDGE,bg="#ffffff")
        BillingFrame_Button.place(x=910,y=515,width=448,height=145)

        self.lbl_billAmt=Label(BillingFrame_Button,text="Bill Amouont\n[0]",font=("groudy old style",15),bg="#1e3119",fg="#ffffff")
        self.lbl_billAmt.place(x=2,y=2,width=145,height=65)
        lbl_Discount=Label(BillingFrame_Button,text="Discount: \n5%",font=("groudy old style",15),bg="#1e3ff9",fg="#ffffff").place(x=149,y=2,width=145,height=65)
        btn_print=Button(BillingFrame_Button,text="Print",command=self.print,font=("groudy old style",15,"bold"),bg="#f5f0e1",fg="#000000",cursor="hand2").place(x=295,y=2,width=145,height=65)
        self.lbl_netPay=Label(BillingFrame_Button,text="Net Pay\n[0]",font=("groudy old style",15),bg="#1e3669",fg="#ffffff")
        self.lbl_netPay.place(x=2,y=70,width=145,height=65)
        btn_clearAll=Button(BillingFrame_Button,text="Clear All",command=self.clearAll,font=("groudy old style",15,"bold"),bg="grey",cursor="hand2").place(x=149,y=70,width=145,height=65)
        btn_genrate=Button(BillingFrame_Button,text="Genrate Bill",command=self.genrate,font=("groudy old style",15,"bold"),bg="#ff6e40",cursor="hand2").place(x=295,y=70,width=145,height=65)

        #====footer====
        lbl_footer=Label(self.root,text="Inventory Management System | Developed by Arnav Sharma",font=("times new roman",15),bg="#4d636d",fg="#ffffff").pack(side=BOTTOM,fill=X)
        with open('login.txt','r') as file:
            self.var_loginid = file.read()
            self.var_loginid=str(self.var_loginid)
        if self.var_loginid=="":
            self.var_loginid=101
        self.update_date_time()
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Product Name is required",parent=self.root) 

            else:
                cur.execute("select pid,name,price,quantity,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductDetail.delete(*self.ProductDetail.get_children())
                    for row in rows:
                        self.ProductDetail.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    def clear(self):
        self.var_customer_name.set("")
        self.var_contact_no.set("")
        self.var_pid.set("")
        self.var_pro_name.set("")
        self.var_pro_price.set("")
        self.var_pro_qty.set("")
        self.lbl_product_stock.config(text=f"In Stock: []")
        self.var_pro_stock.set("")
    
    def add(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Select Product from list",parent=self.root)
        elif self.var_pro_qty.get()=="":
            messagebox.showerror("Error","Quantity is required",parent=self.root)   
        elif int(self.var_pro_qty.get())>int(self.var_pro_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
            #price_cal=float(int(self.var_pro_qty.get())*float(self.var_pro_price.get()))
            price_cal=self.var_pro_price.get()
            cart_data=[self.var_pid.get(),self.var_pro_name.get(),price_cal,self.var_pro_qty.get(),self.var_pro_stock.get()]
            #=====UpdateCart=========
            present='no'
            index_=-1
            for row in self.list_cart:
                if(self.var_pid.get()==row[0]):
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                up=messagebox.askyesno('Confirm',"Product already present!\nDo you want to UPDATE/REMOVE product form the cart",parent=self.root)
                if up==True:
                    if self.var_pro_qty.get()=="0":
                        self.list_cart.pop(index_)
                    else:
                        #self.list_cart[index_][2]=price_cal
                        self.list_cart[index_][3]=self.var_pro_qty.get()
            else:
                self.list_cart.append(cart_data)
            self.show_cart()
            self.bill_update()

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            self.var_search.set("")
            cur.execute("select pid,name,price,quantity,status from product where status='Active'")
            rows=cur.fetchall()
            self.ProductDetail.delete(*self.ProductDetail.get_children())
            for row in rows:
                self.ProductDetail.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def bill_update(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.list_cart:
            self.bill_amt+=(float(row[2].replace(',',''))*int(row[3]))
        round(self.bill_amt,2)
        self.discount=((self.bill_amt*5)/100)
        self.net_pay=self.bill_amt-self.discount

        self.lbl_billAmt.config(text=f"Bill Amouont\n{str(self.bill_amt)}")
        self.lbl_netPay.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.customerTitle.config(text=f"CUSTOMER'S CART \t Total Product: {str(len(self.list_cart))}")


    def show_cart(self):
            try:                
                self.CartDetail.delete(*self.CartDetail.get_children())
                for row in self.list_cart:
                    self.CartDetail.insert('',END,values=row)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.ProductDetail.focus()
        content=(self.ProductDetail.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pro_name.set(row[1])
        self.var_pro_price.set(row[2])
        self.lbl_product_stock.config(text=f"In Stock: [{str(row[3])}]")
        self.var_pro_stock.set(str(row[3]))
        self.var_pro_qty.set("1")
    
    def get_data_cart(self,ev):
        f=self.CartDetail.focus()
        content=(self.CartDetail.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pro_name.set(row[1])
        self.var_pro_price.set(row[2])
        self.lbl_product_stock.config(text=f"In Stock: [{str(row[4])}]")
        self.var_pro_stock.set(str(row[4]))
        self.var_pro_qty.set(row[3])

    def clearAll(self):
        del self.list_cart[:]
        self.var_customer_name.set("")
        self.var_contact_no.set("")
        self.customerTitle.config(text=f"CUSTOMER'S CART \t Total Product: 0")
        self.txt_billArea.delete('1.0',END)
        self.clear()
        self.show()
        self.show_cart()
        self.bill_amt="[0]"
        self.net_pay="[0]"
        self.lbl_billAmt.config(text=f"Bill Amouont\n{str(self.bill_amt)}")
        self.lbl_netPay.config(text=f"Net Pay\n{str(self.net_pay)}")
        
    def print(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_billArea.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror('Error',"Genrate a bill first",parent=self.root)
            

    
    def genrate(self):
        if self.var_customer_name.get()=="" or self.var_contact_no.get()=="":
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.list_cart)==0:
            messagebox.showerror("Error",f"Add product to the cart",parent=self.root)

        else:
            self.total_product=len(self.list_cart)
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_billArea.get('1.0',END))
            fp.close()
            messagebox.showinfo('Bill Saved',"Your Bill has been genrated")
            self.customerTitle.config(text=f"CUSTOMER'S CART \t Total Product: 0")
            self.chk_print=1
            
    def bill_top(self):
        self.invoice="8"+str(int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y")))
        bill_top_temp=f'''
\t     Inventory Management System
\t   Phone No. 98725***** , Delhi-125001
{str("="*52)}
 Customer Name: {self.var_customer_name.get()}
 Ph no. : {self.var_contact_no.get()}
 Bill No. {str(self.invoice)}\t\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*52)}
 Product Name\t\t\t     QTY\t       Price
{str("="*52)}
        '''
        self.txt_billArea.delete('1.0',END)
        self.txt_billArea.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*52)}
 Total Product\t\t\t\t       {self.total_product} 
 Bill Amount\t\t\t\t       Rs.{self.bill_amt}
 Discount\t\t\t\t       Rs.{self.discount}
 Net Pay\t\t\t\t       Rs.{self.net_pay}
{str("="*52)}\n
        '''
        self.txt_billArea.insert(END,bill_bottom_temp)
        
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            for row in self.list_cart:
            # pid,name,price,qty,stock
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])!=int(row[4]):
                    status="Active"
                if int(row[3])>=int(row[4]):
                    status="Inactive"
                self.CartDetail.delete(*self.CartDetail.get_children())
                self.clear()
                price=float(row[2].replace(',',''))*int(row[3])
                price=str(price)
                self.txt_billArea.insert(END,"\n "+name+"\t\t\t     "+row[3]+"\t       Rs."+price)
                cur.execute("update product set quantity=?,status=? where pid=?",(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def update_date_time(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            time_=time.strftime("%I:%M %p")
            date_=time.strftime("%d/%m/%Y")
            cur.execute("select name from employee where eid=?",(self.var_loginid,))
            employee=cur.fetchall()
            self.lbl_clock.config(text=f"Hi {str(employee[0][0])}, Welcome to Inventory Management System\t|\tDate:{str(date_)}\t\t|\tTime: {str(time_)}",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
            self.lbl_clock.after(200,self.update_date_time)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python loginpage.py")
if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop( )