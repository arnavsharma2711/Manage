# Managé - Inventory Management System

A python project dealing with inventory management and bill genration.

## Prerequisite
* You must have [python](https://www.python.org/downloads//) installed in your system.

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pillow module.

```bash
pip install pillow
pip install pyglet
```
* Install remaining modules if any more error came up
* This project is made for 1366 x 768 resolution system. So, adjust the code based on your system's resolution. Also the project was made in 100% scale property of display which can be edited in settings.
### Email Servies
To get access to the email serives in the project follow the steps given below:

1.Go to your [Google Accout](https://myaccount.google.com/)\
2.Search for app password in the search menu.\
3.Select Mail in Select App Menu and Windows Computer in Select Devices Menu.\
4.Click on genrate.\
5.Copy the genrated password to [email_pass.py](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/email_pass.py) in the given quotes along with your email.

## How to access the project
Execute the login.py file from your desired code editor.

Default User ID and password are given below:\
* Administrator Path -> Opens Dashboard\
Employee Id ->1001 \
Password -> 123
* Employee Path -> Opens Billing Menu \
Employee Id ->2001 \
Password -> 123

In the administrator path you have access to all CRUD (Create Read Update Delete) operation.\
In the employee path you have access to bill genration operations only.
## Synopsis of the project
 The goal of this project 
was to help the user to get a working project which consists of:
* The employee, supplier, category, product database.
* Product database connection with supplier and category.
* Two types of account, An administrator and an employee
* Administrator has access to add, update and delete data from the database.
* Administrator also have access to the sales record.
* Employee has access to billing menu having a task to create a cart and generate the 
bills which are kept in the sales record.
* A login page for verification of account type.
* A forgot password section accessible to the user.
Taking all these into account the software was developed.

## Flow Chart
![Flow Chart](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/FLOW%20CHART.png?raw=true "Flow Chart")

## Screenshots
* Login Page : ![Login Page](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/1.1.Login%20Page.png?raw=true "Login Page")

* Dashboard : ![Dashboard](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/2.1.Dashboard.png?raw=true "Dashboard")

* Employee Menu : ![Employee Menu](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/3.1.Emp-Menu.png?raw=true "Employee Menu")

* Supplier Menu : ![Login Pag](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/4.1.Sup-menu.png?raw=true "Supplier Menu")

* Category Menu : ![Category Menu](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/5.1.Cat-Menu.png?raw=true "Category Menu")

* Product Menu : ![Product Menu](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/4.1.Sup-menu.png?raw=true "Product Menu")

* Sales Menu : ![Sales Menu](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/7.2.Sales-View.png?raw=true "Sales Menu")

* Billing Menu : ![Billing Menu](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/9.1.Bill-Menu.png?raw=true "Billing Menu")
## Future Scope of this project
In the future this project can consist of a SMSs update system where the user can get 
notification from the administrator and the customer can get his/her bill details. A customer 
service can also be created to deal with the issues of customer related to their bills and 
product. Scalability of the product can be achieved by storing the database to a server which 
makes us to access the same data to various users at the same time
## References
* Tinker Module->\
https://www.w3schools.in/python-tutorial/gui-programming/
* Pillow Module (ImageTk, Image)->\
https://pillow.readthedocs.io/en/stable/reference/Image.html
https://pillow.readthedocs.io/en/stable/reference/ImageTk.html
* Time Module->\
https://docs.python.org/3/library/time.html
* OS Module->\
https://docs.python.org/3/library/os.html
* smtplib Module->\
https://docs.python.org/3/library/smtplib.html
https://docs.python.org/3/library/email.examples.html
* sqlite3 Module-->\
https://www.tutorialspoint.com/sqlite/sqlite_python.html
