#!/bin/sh

alembic revision --autogenerate -m "Create user messages model"
alembic upgrade heads
python bot/main.py