# ☕ Cafe Deng

A small multi-page website for a cozy coffee shop, built with **Django**.

This is a practice project to learn the fundamentals of Django:
apps, URL routing, function-based and class-based views, templates,
template inheritance, context, and named URLs with namespaces.

## Pages

| Page     | URL               |
|----------|-------------------|
| Home     | `/`               |
| About    | `/about/`         |
| Menu     | `/menu/`          |
| Drinks   | `/menu/drinks/`   |
| Desserts | `/menu/desserts/` |

## Tech Stack

- Python 3.12+
- Django 6.1

## Project Structure

```text
cafe_deng/
├── config/        # Project settings and root URLs
├── pages/         # Home and About pages
├── menu/          # Menu and categories (namespace: menu)
└── templates/     # Shared templates (_base.html, home.html)
```

## Run Locally

```bash
git clone https://github.com/mohammad82aminn/cafe-deng.git
cd cafe-deng
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.