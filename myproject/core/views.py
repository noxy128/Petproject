# core/views.py
from rest_framework import viewsets
from .serializers import PostSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView # <-- Добавь этот импорт

# View для регистрации
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# View для главной страницы (новая)
class HomeView(TemplateView):
    template_name = 'registration/home.html'


from .models import Post #-- этот импорт у нас уже должен быть, но убедись

# ViewSet для API Постов
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer