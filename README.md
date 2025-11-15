# effective-mobile-tests

UI автотесты для сайта [effective-mobile.ru](https://effective-mobile.ru) с использованием Python + Selenium.  
Структура проекта реализована по паттерну **Page Object**, отчётность через **Allure**.

---

## Описание

Автоматизированные UI-тесты для сайта [effective-mobile.ru](https://effective-mobile.ru).  
Используются:

- **Python**
- **Selenium** для работы с браузером
- **Pytest** для запуска тестов
- **Allure** для генерации красивых отчётов
- **Docker** для запуска тестов в контейнере без необходимости настраивать локальное окружение

Тесты организованы по паттерну **Page Object** для удобства поддержки и расширяемости.

---

## Структура проекта

- `Pages/` — Page Object для страниц
- `Tests/` — тестовые сценарии
- `conftest.py` — фикстуры pytest и конфигурация Selenium
- `allure-results/` — результаты тестов для Allure (создаются при запуске)
- `reports/` — временная папка для генерации и просмотра отчёта Allure
- `requirements.txt` — зависимости Python
- `Dockerfile` — конфигурация для запуска тестов в контейнере

---

## Установка и запуск

1. Клонируем репозиторий:

```bash
git clone https://github.com/viprudolf/effective-mobile-tests.git
```

2. Переходим в папку проекта:

```bash
cd effective-mobile-tests
```

3. Устанавливаем зависимости:

```bash
pip install -r requirements.txt
```

4. Запускаем тесты и собираем результаты Allure:

```bash
pytest --alluredir=reports/
```

5. Открываем Allure отчет в браузере:

```bash
allure serve reports/
```

## Запуск через Docker

1. Собираем Docker-образ:

```bash
docker build -t effective-tests .
```

2. Создаём папку для Allure-результатов на хосте:

```bash
mkdir .\allure-results
```

3. Запускаем контейнер с монтированием папки для Allure:

```bash
docker run --rm -it -v ${PWD}/allure-results:/app/allure-results -e RUN_IN_DOCKER=1 effective-tests pytest --alluredir=/app/allure-results
```

4. Генерируем и открываем HTML-отчет:

```bash
allure serve ./allure-results
```