import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,utype text,address text,salary text,password text)")
    con.commit()
    cur.execute("Select * from employee")
    row=cur.fetchone()
    print(row)
    if row==None:
        cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,utype,address,salary,password) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            "1001",
                            "Admin",
                            "none@gmail.com",
                            "Others",
                            "9876543210",
                            "11.11.2011",
                            "11.11.2011",
                            "Admin",
                            "Address",
                            "NA",    
                            "123",
                        ))
        con.commit()
        cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,utype,address,salary,password) values(?,?,?,?,?,?,?,?,?,?,?)",(
                            "2001",
                            "Emp",
                            "none@gmail.com",
                            "Others",
                            "9876543210",
                            "11.11.2011",
                            "11.11.2011",
                            "Employee",
                            "Address",
                            "NA",    
                            "123",
                        ))
        con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(sid INTEGER PRIMARY KEY AUTOINCREMENT,name text,location text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,category text,supplier text,name text,price text,quantity text,status text)")
    con.commit()
    
create_db()