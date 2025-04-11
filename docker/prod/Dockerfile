FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY app /code

COPY app/requirements.txt /code

RUN pip install --no-cache-dir -r ./requirements.txt    

COPY . /code/

ENV PORT 8080

# CMD gunicorn --bind :$PORT --workers 3 code/lina_ai.wsgi

CMD gunicorn --bind :$PORT --workers 3 main.wsgi