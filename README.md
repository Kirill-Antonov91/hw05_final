## Проект Creative Blog
### Описание  
  Проект представляет собой социальную сеть для публикации личных микроблогов. Она даёт пользователям возможность создать учетную запись, публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи. Пользователи могут заходить на чужие страницы, и комментировать записи других авторов.
### Технологии  
  Python 3.8.10  
  Django 2.2.19
  HTML
  CSS
  Django
  Bootstrap
  Unittest
### Запуск проекта в dev-режиме
  * Клонируйте проект на свой компьютер
```
git clone git@github.com:Kirill-Antonov91/hw05_final.git
```
  * Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/bin/activate
```
  * Установите зависимости из файла requirements.txt  
```
pip install -r requirements.txt
```
  * В папке с файлом manage.py подготовить и провести миграции:
```
python manage.py makemigrations
python manage.py migrate
```
  * Там же создать суперюзера:
```
python manage.py createsuperuser
```
  * Запустить проект:
```
python manage.py runserver
```

### Автор  
[KirillAntonov](https://github.com/Kirill-Antonov91)
