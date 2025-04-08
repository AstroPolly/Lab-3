# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /Lab_3

# Копируем файлы приложения в контейнер
COPY . /Lab_3

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, который будет использоваться
EXPOSE 8080

# Команда для запуска приложения
CMD ["python", "main.py"]