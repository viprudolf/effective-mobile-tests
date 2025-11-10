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

Тесты организованы по паттерну **Page Object** для удобства поддержки и расширяемости.

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

