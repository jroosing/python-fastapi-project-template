FROM python:3.12-alpine
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

CMD ["fastapi", "run", "src/main.py", "--port", "80"]