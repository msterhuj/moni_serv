# moni_serv

## Run dev

```bash
poetry install
poetry shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Run prod

```bash
poetry install
poetry shell
python manage.py migrate
python manage.py collectstatic
uvicorn moni_serv.wsgi:application
```
