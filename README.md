# DevTrack API 🚀

## 📌 Overview

DevTrack is a minimal backend API for tracking engineering issues.
Engineers can create reporters, file issues, assign priorities, and track statuses.

---

## ⚙️ Tech Stack

* Python
* Django
* JSON file storage (no database)

---

## ▶️ How to Run the Project

```bash
git clone https://github.com/<your-username>/devtrack-api.git
cd devtrack-api

python3 -m venv venv
source venv/bin/activate

pip install django

python manage.py runserver
```

Server runs at:
http://127.0.0.1:8000/

---

## 📡 API Endpoints

### 👤 Reporter APIs

#### POST /api/reporters/

Create a reporter

#### GET /api/reporters/

Get all reporters

#### GET /api/reporters/?id=1

Get reporter by ID

---

### 🐞 Issue APIs

#### POST /api/issues/

Create an issue

#### GET /api/issues/

Get all issues

#### GET /api/issues/?id=1

Get issue by ID

#### GET /api/issues/?status=open

Filter issues by status

---

## ✅ Example Success Response

```json
{
  "id": 1,
  "title": "Login issue",
  "description": "Button not working",
  "status": "open",
  "priority": "critical",
  "reporter_id": 1,
  "message": "[URGENT] Login issue — needs immediate attention"
}
```

---

## ❌ Example Error Response

```json
{
  "error": "Title cannot be empty"
}
```

---

## 🧠 Design Decision

I used inheritance for handling issue priorities.
Critical and low-priority issues override the `describe()` method to provide customized messages.

This follows the **Open/Closed Principle**, allowing new priority types to be added without modifying existing code.

---

## 📸 Postman Screenshots

(Add screenshots here)

---
