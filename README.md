**Для запуска**:
1) Клонировать репозиторий.
2) В терминале прописать pip install -r requirmants.txt.
3) Прописать команду createdb -U postgres db_workers
4) В settings.py установить пароль и настройки для БД.
5) Прописать команду python manage.py migrate
5) Прописать команду python manage.py runserver
 

6) Для создания графика смен прописать команды python manage.py createmounths и python manage.py createplan
   