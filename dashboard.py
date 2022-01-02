from tkinter import *
from PIL import Image,ImageTk
import time
from tkinter import messagebox
import sqlite3
import os
import pyglet
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("MANAGÉ - Inventory Management System | Developed by Arnav Sharma")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\logo.png")
        self.root.iconphoto(False,self.icon_main)
        pyglet.font.add_file('file.ttf')

        #====Title====        
        title=Label(self.root,text="MANAGÉ",image=self.icon_main,compound=LEFT,font=("Gloria Hallelujah",35,"bold"),bg="#0063B2",fg="#ffffff",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=70)
        title=Label(self.root,text="- Inventory Management System",compound=LEFT,font=("Century",35,"bold"),bg="#0063B2",fg="#ffffff",anchor="w",padx=10).place(x=295,y=0,relwidth=1,height=70)
        
        #====Logout_BTN====
        btn_logout=Button(self.root,text="LOGOUT",command=self.logout,font=("times new roman",17,"bold"),bg="yellow",cursor="hand2").place(x=1200,y=10,height=50,width=140)
        
        #====Header====
        self.lbl_clock=Label(self.root,text="Welcome to MANAGÉ - Inventory Management System\t|\t Date: DD-MM-YYY\t|\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #====Left_menu====
        self.MenuLogo=Image.open("images/menulogo.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=0,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images\side.png")
        lbl_menu=Label(LeftMenu,text="MENU",font=("times new roman",20),bg="#768982").pack(side=TOP,fill=X)
        
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_categoery=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.root.destroy,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="#ffffff",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====content====
        self.icon_employee=PhotoImage(file="images\employe.png")
        self.lbl_Employee=Label(self.root,text="Total Employee [ 0 ]",image=self.icon_employee,compound=LEFT,font=("calibri",20,"bold"),bg="#5CC8D7",fg="#ffffff",bd=5,relief=RIDGE,padx=10)
        self.lbl_Employee.place(x=300,y=140,height=60,width=960)

        self.icon_supplier=PhotoImage(file="images\supplier.png")
        self.lbl_Supplier=Label(self.root,text="Total Supplier [ 0 ]",image=self.icon_supplier,compound=LEFT,font=("calibri",20,"bold"),bg="#DD4132",fg="#ffffff",bd=5,relief=RIDGE,padx=10)
        self.lbl_Supplier.place(x=300,y=245,height=60,width=960)

        self.icon_category=PhotoImage(file="images\categories.png")
        self.lbl_Category=Label(self.root,text="Total Category [ 0 ]",image=self.icon_category,compound=LEFT,font=("calibri",20,"bold"),bg="#5CC8D7",fg="#ffffff",bd=5,relief=RIDGE,padx=10)
        self.lbl_Category.place(x=300,y=350,height=60,width=960)

        self.icon_product=PhotoImage(file="images\product.png")
        self.lbl_Product=Label(self.root,text="Total Product [ 0 ]",image=self.icon_product,compound=LEFT,font=("calibri",20,"bold"),bg="#DD4132",fg="#ffffff",bd=5,relief=RIDGE,padx=10)
        self.lbl_Product.place(x=300,y=455,height=60,width=960)
        
        self.icon_sales=PhotoImage(file="images\sales.png")
        self.lbl_Sales=Label(self.root,text="Total Sales [ 0 ]",image=self.icon_sales,compound=LEFT,font=("calibri",20,"bold"),bg="#5CC8D7",fg="#ffffff",bd=5,relief=RIDGE,padx=10)
        self.lbl_Sales.place(x=300,y=560,height=60,width=960)


        #====footer====
        lbl_footer=Label(self.root,text="MANAGÉ - Inventory Management System | Developed by Arnav Sharma",font=("times new roman",15),bg="#4d636d",fg="#ffffff").pack(side=BOTTOM,fill=X)
        with open('login.txt','r') as file:
            self.var_loginid = file.read()
            self.var_loginid=str(self.var_loginid)
        if self.var_loginid=="":
            self.var_loginid=1001
        self.update_content()

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Product.config(text=f'Total Product [ {str(len(product))} ]')
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_Supplier.config(text=f'Total Supplier [ {str(len(supplier))} ]')
            cur.execute("select * from employee where utype='Employee'")
            employee=cur.fetchall()
            self.lbl_Employee.config(text=f'Total Employee [ {str(len(employee))} ]')
            cur.execute("select name from employee where eid=?",(self.var_loginid,))
            employee=cur.fetchall()
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_Category.config(text=f'Total Category [ {str(len(category))} ]')
            sales=len(os.listdir('bill'))
            self.lbl_Sales.config(text=f'Total Sales [ {str(sales)} ]')
            time_=time.strftime("%I:%M %p")
            date_=time.strftime("%d/%m/%Y")
            self.lbl_clock.config(text=f"Hi {str(employee[0][0])}, Welcome to MANAGÉ - Inventory Management System\t|\tDate:{str(date_)}\t|\tTime: {str(time_)}",font=("times new roman",15),bg="#4d636d",fg="#ffffff")
            self.lbl_clock.after(200,self.update_content)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python loginpage.py")

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop( )