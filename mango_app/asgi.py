import os
from django.core.asgi import get_asgi_application
from fastapi_app.api import app as fastapi_app
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mango_app.settings')

django_app = get_asgi_application()

# Combine FastAPI with Django
application = WSGIMiddleware(fastapi_app)
