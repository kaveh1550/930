import os
import sys
from django.core.wsgi import get_wsgi_application
from waitress import serve

# اضافه کردن مسیر پروژه به sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # اضافه کردن پوشه والد به sys.path

# تنظیم DJANGO_SETTINGS_MODULE به درستی
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_consultation.settings')

# ایجاد application از Django
application = get_wsgi_application()

if __name__ == "__main__":
    # اجرای سرور با Waitress
    serve(application, host='0.0.0.0', port=8000)
