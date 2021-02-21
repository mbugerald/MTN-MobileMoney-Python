FROM python:latest

USER root

RUN apt-get update

RUN mkdir /webapp

COPY . /webapp

WORKDIR /webapp

RUN ls
RUN chmod 644 /usr/share/fonts/*
RUN fc-cache -fv

RUN pip install -r requirements.txt
RUN pip install gunicorn eventlet
RUN rm -f ../celerybeat.pid

EXPOSE 80

CMD ["gunicorn", "-k", "eventlet", "-w", "2", "-b", "0.0.0.0:80", "run:app", "--log-level", "debug", "--reload", "--timeout", "320"]
