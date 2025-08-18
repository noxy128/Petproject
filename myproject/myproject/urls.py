# myproject/urls.py (основной файл)

from django.contrib import admin
from django.urls import path, include  # <-- Убедись, что 'include' импортирован

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # <-- Добавь эту строку, чтобы подключить адреса из приложения
]