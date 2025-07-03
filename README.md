# ☁️ Cloud Status API

واجهة برمجية بسيطة (API) تعرض حالة خدمات السحابة مثل AWS و Azure و Google Cloud، مع واجهة HTML مدمجة لعرض الحالة بشكل مباشر.

A simple cloud service status API with an HTML dashboard. Built using **FastAPI**, **SQLite**, and **Jinja2 Templates**.

---

## 🧰 التقنيات المستخدمة | Tech Stack

- ⚙️ Python 3.13
- 🚀 FastAPI
- 🧱 SQLAlchemy
- 🖼️ Jinja2 Templates
- 🗄️ SQLite (File-based database)
- 🐳 Docker (optional)

---

## 📦 تشغيل محلي | Run Locally

```bash
git clone https://github.com/hussamAl-hassoun/cloud-status-api.git
cd cloud-status-api
pip install -r requirements.txt
uvicorn app.main:app --reload

🌐 افتح: http://127.0.0.1:8000 لواجهة المستخدم

📑 توثيق API: http://127.0.0.1:8000/docs
