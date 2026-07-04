# Bayessiaan_technology_assignment

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License" />
</p>

---

## 🚀 Project Overview
**Bayessiaan_technology_assignment** is a specialized web application developed by [Alok345](https://github.com/Alok345). This project serves as a robust backend-driven system designed to handle flight search operations efficiently. Built on the Django framework, it provides a structured approach to managing data queries and search functionalities within the aviation domain.

---

## ✨ Key Features
- **Efficient Querying**: Optimized search logic to handle flight data requests.
- **Robust Backend**: Built on Django’s high-level framework for reliability and security.
- **Database Management**: Integrated with SQLite for seamless development and lightweight deployment.
- **Modular Architecture**: Clean separation of concerns between core flight logic and search utilities.

---

## 🛠 Tech Stack
| Component | Technology |
| :--- | :--- |
| **Backend** | Python, Django |
| **Database** | SQLite3 |
| **Environment** | Virtual Environment (Recommended) |

---

## 📂 Project Structure
```text
Bayessiaan_technology_assignment/
├── db.sqlite3            # SQLite database file
├── manage.py             # Django project management script
├── flight_search/        # Core configuration & settings
└── search/               # Main application logic
```

---

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/Alok345/Bayessiaan_technology_assignment.git
cd Bayessiaan_technology_assignment
```

### 2. Set up virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

---

## 🚀 Usage

Once the environment is set up and migrations are applied, launch the server:

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to interact with the application. Ensure your database contains the necessary data to perform searches effectively.

---

## 📝 License
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## 👨‍💻 Author
**Alok345**
*GitHub: [@Alok345](https://github.com/Alok345)*

---
*Built with precision for the Bayessiaan Technology Assignment.*