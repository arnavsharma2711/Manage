from tkinter import *
from PIL import ImageTk
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+225+150")
        self.root.title("--> Category Menu ")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\categories.png")
        self.root.iconphoto(False,self.icon_main)
        self.root.focus_force()
        #====Variables====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #====Title====
        title=Label(self.root,text="Manage Product Category",font=("arial",15),bg="#0f4d7d",fg="#ffffff").place(x=50,y=20,width=1000)
        
        self.image=ImageTk.PhotoImage(file="images\category.png")
        self.lbl_inage=Label(self.root,image=self.image,bd=0).place(x=180,y=220)
        #===Content====
        lbl_cat_name=Label(self.root,text="Enter Category Name",font=("arial",15),bg="#ffffff").place(x=60,y=70)
        txt_cat_name=Entry(self.root,textvariable=self.var_name,font=("arial",15),bg="lightyellow").place(x=280,y=70,width=260)
        
        #===button
        btn_add=Button(self.root,text="Add",command=self.add,font=("groudy old style",15),bg="#4caf50",cursor="hand2").place(x=280,y=130,width=110,height=28)
        btn_update=Button(self.root,text="Delete",command=self.delete,font=("groudy old style",15),bg="#f44336",cursor="hand2").place(x=400,y=130,width=110,height=28)

        #====Category Details====
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=600,y=70,width=430,height=380)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        
        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid",text="Category ID")
        self.categoryTable.heading("name",text="Name")

        self.categoryTable["show"]="headings"
        
        self.categoryTable.column("cid",width=60)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#====================================================================================
#====Function====

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name must be required",parent=self.root)
                self.root.focus_force()
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category is already exist, try different",parent=self.root)
                    self.root.focus_force()
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))

                    con.commit()
                    messagebox.showinfo("Sucess","Category Added Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Category must be selected",parent=self.root)
                self.root.focus_force()
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category Name",parent=self.root)
                    self.root.focus_force()
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Sucess","Category Deleted Sucessfully",parent=self.root)
                        self.root.focus_force()
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_name.set("")
        self.show()
 

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()