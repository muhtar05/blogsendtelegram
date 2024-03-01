# blogsendtelegram
Это исходный код для примеров в статье https://gadjimuradov.ru/post/publikuem-posty-bloga-na-kanale-telegram-ispolzuya-django/

## **Для запуска blogsendtelegram**
1. Переходим в директорию blogsendtelegram
2. Создаем виртуальное окружение через командную строку python -m venv venv
3. Активируем виртуальное окружение:
   1. Для Linux/Mac:  source venv/bin/activate 
   2. Для Windows: venv/Scripts/activate

4. Выполняем команду pip install -r requirements.txt
5. Выполняем миграции python manage.py migrate
6. Запускаем приложение python manage.py runserver

