## Простое API на Django Rest Framework для просмотра списка задач и создания новых. 

## Пример POST запроса

![image](https://github.com/user-attachments/assets/94e6ff34-674b-42e9-807f-845afc19446e)

Список дел
![image](https://github.com/user-attachments/assets/b5057257-8b21-4115-a513-81f40c357fb1)

## Установка
1. Клонируйте репозиторий
2. Установки зависимости: обратите внимание в проекте используется менеджер ```pipenv``` https://pipenv.pypa.io/en/latest/installation.html#installing-packages-for-your-project
3. Выполните миграции: ```py manage.py makemigrations``` > ```python manage.py migrate``` 
4. Запустите сервер: ```py manage.py runserver```

Endpoints: http://127.0.0.1:8000/tasks/ на ```GET``` и ```POST```- запросы. 

