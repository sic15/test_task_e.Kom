# test_task_e.Kom
###### Решение тестового задания на вакансию Junior+ Python разработчик

## Описание
Проект Flask, который выполняет сопоставление данных формы с шаблонами и возвращает соответствующий шаблон или типизацию полей полученной формы.

## Установка и запуск
1. Клонировать репозиторий:
`git clone git@github.com:sic15/test_task_e.Kom.git`

2. Перейти в папку test_task_e.Kom:
`cd e.Kom`

3. Cоздать и активировать виртуальное окружение:
`python -m venv venv source venv/scripts/activate`

4. Обновить pip и установить зависимости из файла requirements.txt:
`python -m pip install --upgrade pip pip install -r requirements.txt`

5. Запустить Flask-приложение:
`python app.py`
Приложение будет доступно по адресу http://localhost:5000

6. Для отправки тестовых запросов используйте скрипт test.py:
`python test.py`
Для ручного тестирования можно использовать Postman

## Структура проекта
- app.py: Основной файл Flask-приложения.
- templates.json: База данных шаблонов форм.
- test.py: Скрипт для тестирования приложения.
- requirements.txt: Файл с перечислением зависимостей проекта.

## Автор
Арлазарова Наталья

