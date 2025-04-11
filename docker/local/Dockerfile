FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code

RUN pip install --no-cache-dir -r ./requirements.txt    

COPY . /code/

ENV PORT 8080

CMD gunicorn --bind :$PORT --workers 3 Archetype.wsgi --capture-output --log-level=debug