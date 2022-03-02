# test_db_bot

ДАААААА! ДАВАЙ!!! ДАВАААААЙ!!

```bash
docker-compose up --build
```

И не забудь заполнить ```.env```

А потом в другом окне

```bash
poetry run alembic revision --autogenerate -m "Create user messages model"
```
и
```bash
poetry run alembic upgrade heads
```
