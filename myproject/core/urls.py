# core/urls.py

from django.urls import path, include  # <-- Добавь 'include'
from rest_framework.routers import DefaultRouter
from .views import SignUpView, HomeView, PostViewSet # <-- Убедись, что PostViewSet импортирован
from django.contrib.auth import views as auth_views

# Создаём router и регистрируем наш ViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet)

# Основные URL-адреса нашего приложения
urlpatterns = [
    # URL-ы для нашего сайта (страницы)
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL-ы для нашего API
    path('api/', include(router.urls)),
]