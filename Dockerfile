FROM python:3.9

RUN pip install -U pip poetry

COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes -f requirements.txt -o requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN chmod +x bot/startup.sh

CMD ["bot/startup.sh"]
