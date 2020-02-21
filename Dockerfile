FROM python:3.8-alpine

LABEL Author=ilya

RUN apk add --no-cache gcc libc-dev unixodbc-dev libffi-dev

COPY requirements.txt /tmp/requirements.txt

RUN pip install setuptools pip --upgrade && \
    pip install --no-cache -r  /tmp/requirements.txt && \
    rm /tmp/requirements.txt

WORKDIR /opt/dotka_bot

COPY handlers/ handlers/
COPY media_shit/ media_shit/
COPY bot.py ./
COPY config.py ./
COPY misc.py ./

CMD [ "python", "bot.py" ]