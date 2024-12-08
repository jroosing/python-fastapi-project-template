FROM python:3.12-alpine
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m venv .venv
RUN source .venv/bin/activate

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

CMD ["fastapi", "run", "main.py", "--port", "80"]
