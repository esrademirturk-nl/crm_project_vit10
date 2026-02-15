# 🖥️ CRM Project (FastAPI + PyQt + Google Sheets)

A lightweight desktop CRM system built with **PyQt (GUI)** and **FastAPI (Backend)**.  
The application manages users, mentors, applications, interviews, and preferences using **Google Sheets as a database** via Google APIs.

---

## 🚀 Project Overview

This CRM system replaces manual spreadsheet workflows with a structured application that includes:

- 🔑 Custom login system
- 👥 Role-based authorization (Admin / User)
- 🧑‍🏫 Mentor management
- 📝 Application tracking
- 📅 Interview management
- ⚙️ Preferences & admin controls
- ☁️ Google Sheets API integration
- 📆 Google Calendar API integration
- 📧 Google Gmail API integration (email authentication & notifications)

---

## 🏗️ Architecture

The project follows a layered architecture:

```
UI (PyQt)
   ↓
FastAPI Routers
   ↓
Services
   ↓
Repositories
   ↓
Google Sheets API
```

This structure ensures:

- Clear separation of concerns  
- Maintainable and scalable design  
- Clean data flow between UI and backend  

---

## 🔑 Authentication & Authorization

- Users authenticate using credentials stored in a Google Sheets file.
- Role-based redirection:
  - **Admin → Preferences Admin Panel**
  - **User → Preferences Panel**
- Failed login attempts display warning messages.
- Styled UI with hover effects, rounded buttons, and consistent design.

---

## 📂 Core Modules

### 👤 User Management
- Store and manage users in Google Sheets
- Role-based access control
- Admin-level configuration

### 🧑‍🏫 Mentor Management
- Add / Edit / List mentors
- Dedicated Mentor Menu interface

### 📝 Application Management
- Store participant applications
- Filter and search functionality
- Integrated with Google Sheets

### 📅 Interview Management
- Record interview details
- Assign mentors
- Update interview statuses

---

## 🖼️ Screenshots

| Login | Admin Preferences |
|-------|-------------------|
| <img src="docs/screenshots/login.png" width="400"/> | <img src="docs/screenshots/admin_preferences.png" width="400"/> |

| Mentor Menu | Applications |
|-------------|-------------|
| <img src="docs/screenshots/mentor_menu.png" width="400"/> | <img src="docs/screenshots/applications.png" width="400"/> |

---

## 🛠️ Tech Stack

- Python 3.11+
- PyQt5
- FastAPI
- Uvicorn
- Pydantic
- Google Sheets API
- Google Drive API
- Google Gmail API
- gspread
- python-dotenv

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/crm-project.git
cd crm-project
```

### 2️⃣ Create a virtual environment

```bash
python -m venv env
source env/bin/activate   # macOS/Linux
# env\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file using `.env.example`.

Example:

```
USERS_SHEET_ID=your_sheet_id
MENTORS_SHEET_ID=your_sheet_id
APPLICATIONS_SHEET_ID=your_sheet_id
INTERVIEWS_SHEET_ID=your_sheet_id
```

---

## ▶️ Running the Project

### Run Backend

```bash
uvicorn backend.main:app --reload
```

### Run Desktop UI

```bash
python run.py
```

---

## 🔐 Security Notes

- `credentials.json`, `token.json`, and `.env` are excluded via `.gitignore`.
- No sensitive information is stored in the repository.
- Google OAuth authentication is required on first run.

---

## 📌 Future Improvements

- JWT authentication
- Docker containerization
- Cloud deployment
- Role-based API protection
- Migration to PostgreSQL

---

## 👩‍💻 Author

**Esra Demirturk**  
CRM Project – 2026
