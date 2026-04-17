# PythonAnywhere deployment instructions

## 1. Setup on PythonAnywhere

### Create virtual environment:
```bash
# Open Bash console on PythonAnywhere
mkvirtualenv --python=python3.11 myenv
pip install -r requirements.txt
```

### Create WSGI file:
Create/edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`:

```python
import os
import sys

# Add your project directory to path
path = '/home/YOUR_USERNAME/portoapp'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio.settings')

# Activate virtual environment
activate_this = '/home/YOUR_USERNAME/.virtualenvs/myenv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Create static files directory:
```bash
mkdir -p /home/YOUR_USERNAME/portoapp/staticfiles
```

---

## 2. Database Setup

Use SQLite on PythonAnywhere (no setup needed) or PostgreSQL:

### For PostgreSQL:
```bash
# In Bash console
pip install dj-database-url psycopg2-binary
```

### For SQLite (simpler):
The app will use SQLite by default.

---

## 3. Configure Web App on PythonAnywhere

1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select Python 3.11
5. Click **Next**

### Settings:
- **Source code:** `/home/YOUR_USERNAME/portoapp`
- **Working directory:** `/home/YOUR_USERNAME/portoapp`
- **Virtual environment:** `/home/YOUR_USERNAME/.virtualenvs/myenv`

### Static files:
- **URL:** `/static/`
- **Directory:** `/home/YOUR_USERNAME/portoapp/staticfiles`

---

## 4. Environment Variables

Create a `.env` file in your project:

```bash
# In Bash
nano /home/YOUR_USERNAME/portoapp/.env
```

Add:
```
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourusername.pythonanywhere.com
```

---

## 5. Run Migrations

```bash
# In Bash console
cd /home/YOUR_USERNAME/portoapp
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

---

## 6. Reload Web App

Go to **Web** tab → Click **Reload** yourusername.pythonanywhere.com

---

## Files to upload to PythonAnywhere:

1. Upload all project files to `/home/YOUR_USERNAME/portoapp/`
2. Or use Git:
```bash
cd /home/YOUR_USERNAME
git clone https://github.com/DJIBEYROU/portoapp.git
```
