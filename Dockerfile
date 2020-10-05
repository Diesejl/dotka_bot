FROM python:3.7-slim

WORKDIR /dotka_bot

COPY requirements.txt /dotka_bot/
RUN pip install -r /dotka_bot/requirements.txt
COPY . /dotka_bot/

CMD python3 /dotka_bot/app.py
