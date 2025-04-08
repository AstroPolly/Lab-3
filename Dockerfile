# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /LAB 3

# Копируем файлы приложения в контейнер
COPY . /LAB_3

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, который будет использоваться
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "main.py"]