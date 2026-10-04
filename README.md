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
- environs (environment variables)

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
git clone https://github.com/YOUR-USERNAME/cafe-deng.git
cd cafe-deng
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
pip install -r requirements.txt
```

Create your environment file from the example and set a new secret key:

```bash
cp .env.example .env
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Put the generated key in `.env` as `DJANGO_SECRET_KEY`, then:

```bash
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.