# Базовый образ Python
FROM python:3.10-slim

# Копируем зависимости и ставим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем Chromium и ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    unzip \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем Allure CLI
RUN wget -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.35.1/allure-2.35.1.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && rm /tmp/allure.zip

# Добавляем Allure и Chromium в PATH
ENV PATH="/opt/allure-2.35.1/bin:$PATH"
ENV PATH="/usr/lib/chromium/:$PATH"
ENV CHROME_BIN=/usr/bin/chromium

# Команда по умолчанию: только запуск Pytest
CMD ["pytest", "Tests/", "--alluredir=/app/allure-results"]

