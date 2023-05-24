# Бот для записи в салон красоты


## Требования
Должны быть установлены:
- git, чтобы вы могли скачать код; 
- pip, чтобы установить необходимые библиотеки;
- python3, чтобы запустить код.

## Запуск

Скачайте код с помощью команды в командной строке
```
https://github.com/Boltasov/devman-django-orm-watching-storage
```
Установите необходимые библиотеки командой
```
python pip install -r requirements.txt
```
Сделайте миграции
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```

Запустите командой 
```
python manage.py runserver
``` 
Cайт можно будет открыть по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Чтобы потыкаться в админку сначала создайте суперпельзователя
```commandline
python createsuperuser
```
Далее заполните имя и придумайте пароль

После этого зайдите в админку [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
