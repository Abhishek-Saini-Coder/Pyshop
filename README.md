# 🛒 PyShop (Django Project)

A simple Django-based web application for managing products and offers.  
This project is built to learn Django fundamentals like models, views, templates, and the Django Admin.

---

## 🚀 Features
- Product management (add, edit, delete products)
- Offer system with discounts
- Django Admin integration
- SQLite database support
- Clean project structure

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend:** Django Templates (HTML, CSS, Bootstrap)

---

## 📂 Project Structure
```
pyshop/
│── manage.py
│── pyshop/        # Main project settings
│── products/      # Products app (models, views, admin)
│── db.sqlite3
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/pyshop.git
   cd pyshop
   ```

2. **Create & activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run server**
   ```bash
   python manage.py runserver
   ```

7. Open in browser:  
   👉 http://127.0.0.1:8000/  
   👉 Admin: http://127.0.0.1:8000/admin/

---

## 📝 Requirements
Create a `requirements.txt` with:
```
Django>=5.0
```

(You can generate exact versions with: `pip freeze > requirements.txt`)

---

## 📸 Screenshots (Optional)
_Add screenshots of your app UI or Django Admin here._

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.

---

## 📄 License
This project is licensed under the MIT License.
