# 1. Базовый образ с Python
FROM python:3.11-slim

# 2. Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 4. Копируем файлы с зависимостями и устанавливаем их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 5. Копируем весь остальной код проекта в контейнер
COPY . /app/

# 6. Указываем команду для запуска приложения (пока закомментирована)
# CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]