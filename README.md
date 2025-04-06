Here’s a polished and professional README for your **Managé - Inventory Management System**, keeping it developer-friendly, informative, and visually neat. I’ve improved grammar, fixed typos, and organized everything for a better experience. Let’s go! 🚀

---

# 📦 Managé – Inventory Management System

**Managé** is a Python-based desktop application that helps manage inventory and generate bills. Designed with a GUI using **Tkinter**, it allows for real-time tracking of products, categories, suppliers, employees, and sales records — all tied together with SQLite. Two types of user roles provide secure and scalable access.

---

## 📋 Prerequisites

- ✅ [Python 3.x](https://www.python.org/downloads/) installed
- ✅ Install dependencies via pip:

```bash
pip install pillow
pip install pyglet
```

> If any additional module errors occur, install them individually as prompted.

> 🖥️ **Note**: This project was built on a 1366x768 screen resolution using 100% display scaling. If the UI looks off, tweak widget dimensions in code to suit your system.

---

## ✉️ Email Services Setup

To enable **email services** (e.g., for password recovery):

1. Go to your [Google Account](https://myaccount.google.com/)
2. Search for “App Passwords” in the security settings
3. Select:
   - App: **Mail**
   - Device: **Windows Computer**
4. Click **Generate** to get a secure password
5. Copy the generated password and paste it into the [`email_pass.py`](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/email_pass.py) file, replacing the placeholder string

---

## 🧑‍💻 How to Run the Project

Launch the project by executing:

```bash
python login.py
```

### 🔐 Default Login Credentials

| User Type | ID | Password | Access |
|-----------|----|----------|--------|
| Admin     | 1001 | 123 | Full Dashboard + CRUD |
| Employee  | 2001 | 123 | Billing System Only |

- **Admin View**: Complete access (add/update/delete/view records)
- **Employee View**: Limited to billing operations

---

## 🧠 Project Features (Synopsis)

The system was developed to provide:

- 📇 Management of **Employees, Suppliers, Categories, Products**
- 🔗 Product database linked with Suppliers and Categories
- 🔐 **Role-based Access**:
  - Admins can perform **CRUD** operations and view **Sales Reports**
  - Employees can **generate bills** and add to sales records
- 🧾 Smart **Billing System** with cart-based item handling
- 🔐 Login verification and a **Forgot Password** module
- Local **SQLite database** for data storage

---

## 🧭 Flow Chart

![Flow Chart](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/FLOW%20CHART.png?raw=true)

---

## 🖼️ Screenshots

| Feature | Preview |
|--------|---------|
| Login Page | ![Login](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/1.1.Login%20Page.png?raw=true) |
| Dashboard | ![Dashboard](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/2.1.Dashboard.png?raw=true) |
| Employee Menu | ![Emp Menu](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/3.1.Emp-Menu.png?raw=true) |
| Supplier Menu | ![Supplier](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/4.1.Sup-menu.png?raw=true) |
| Category Menu | ![Category](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/5.1.Cat-Menu.png?raw=true) |
| Product Menu | ![Product](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/4.1.Sup-menu.png?raw=true) |
| Sales Menu | ![Sales](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/7.2.Sales-View.png?raw=true) |
| Billing Menu | ![Billing](https://github.com/arnavsharma2711/Inventory-Management-System/blob/main/Screenshot/9.1.Bill-Menu.png?raw=true) |

---

## 🔮 Future Scope

In future iterations, this project could expand to include:

- 📱 **SMS notification system** for billing and admin alerts
- 🧑‍💼 **Customer support module** for resolving product or billing concerns
- ☁️ **Cloud-hosted database** to support real-time, multi-user access across systems
- 📊 **Advanced analytics** and graphical reports for sales and stock insights

---

## 📚 References

- **Tkinter (GUI)** → https://www.w3schools.in/python-tutorial/gui-programming/
- **Pillow (Image handling)** →  
  - https://pillow.readthedocs.io/en/stable/reference/Image.html  
  - https://pillow.readthedocs.io/en/stable/reference/ImageTk.html
- **Pyglet (Audio/Media)** → https://pyglet.readthedocs.io/en/latest/
- **Time Module** → https://docs.python.org/3/library/time.html
- **OS Module** → https://docs.python.org/3/library/os.html
- **smtplib (Email)** →  
  - https://docs.python.org/3/library/smtplib.html  
  - https://docs.python.org/3/library/email.examples.html
- **SQLite (Database)** → https://www.tutorialspoint.com/sqlite/sqlite_python.htm

---

Let me know if you’d like help adding a `requirements.txt`, packaging into `.exe`, adding unit tests, or versioning your modules! ⚙️📦
