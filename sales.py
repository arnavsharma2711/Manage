from tkinter import *
from tkinter import messagebox
import os

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+225+150")
        self.root.title("--> Sales Menu ")
        self.root.config(bg="white")
        self.icon_main=PhotoImage(file="images\sales.png")
        self.root.iconphoto(False,self.icon_main)
        self.root.focus_force()
        #====Variables====
        self.var_invoice=StringVar()
        self.list_bill=[]

        #====Title====
        title=Label(self.root,text="View Customer Bills",font=("arial",15),bg="#0f4d7d",fg="#ffffff").place(x=50,y=20,width=1000)

        lbl_invoice=Label(self.root,text="Search by Invoice No.",font=("arial",15),bg="#ffffff").place(x=80,y=70)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("arial",15),bg="lightyellow").place(x=300,y=70,width=180)
        btn_search=Button(self.root,text="Search",command=self.search,font=("groudy old style",15),bg="lightgreen",cursor="hand2").place(x=260,y=110,width=100,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("groudy old style",15),bg="#607d8b",cursor="hand2").place(x=380,y=110,width=100,height=28)

        #===Sales List
        sales_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        sales_frame.place(x=140,y=150,width=340,height=320)
        lbl_title_bill=Label(sales_frame,text="Bill List",font=("groudy old style",15),bg="orange").pack(side=TOP,fill=X)

        scrolly=Scrollbar(sales_frame,orient=VERTICAL)        
        self.sales_list=Listbox(sales_frame,font=("groudy old style",15),bg="#ffffff",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)
        #====Bill Area====
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#ffffff")
        bill_frame.place(x=520,y=69,width=500,height=400)
        lbl_title_bill=Label(bill_frame,text="Customer Bill Area",font=("groudy old style",15),bg="orange").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=("gordy old style",12),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        self.show()
        #====

    def show(self):
        del self.list_bill[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.list_bill.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. is required",parent=self.root)
        else:
            if self.var_invoice.get() in self.list_bill:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invoice No. is invalid",parent=self.root)

    def clear(self):
        self.show()
        self.var_invoice.set("")
        self.bill_area.delete('1.0',END)

if __name__=="__main__":
    root=Tk()
    obj=salesClass(root)
    root.mainloop()