# Python FastAPI Project Template
This project functions as a template for FastAPI projects. 

*note:* This example assumes python is called using "python3" and pip is called using "pip3". your installation may differ.

## Virtual env
In order to keep dependencies localized, it is possible to create a lightweight virtual environment (venv). 
Each venv gets their own independent set of python packages installed.

```shell
python3 -m venv .venv
source .venv/bin/activate
```

This creates the new virtual environment and also activates it

## Install dependencies
```
pip3 install -r requirements.txt
```

## Running the app
The application requires a database to be available.
In the root directory of the project create or edit the '.env' file and add the following contents:

```
DATABASE_PORT=5432
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_DB=fastapi
POSTGRES_HOST=localhost
POSTGRES_HOSTNAME=127.0.0.1
```
Note that these are the docker postgres defaults and do NOT reflect the credentials of a real server.

Whether running the application from shell or docker, we will always need to startup the postgres db via docker-compose.

```shell
docker compose up postgres pgadmin
```

### shell
`cd` into the 'src' folder and run the following command:

```shell
uvicorn main:app --host localhost --port 8000 --reload
```

### docker-compose
In order to run the entire stack using docker-compose execute `docker compose up web`
If you want to run things in the background use `docker compose up -d web` instead.

The setup runs the app, postgres and pgadmin4.

The credentials can be found in the docker-compose.yml.

To access the app: localhost:8000
To access pgadmin4: localhost:5000

To connect from pgadmin to the database use 'postgres' as host.

## Linting and formatting
My preference goes to ruff, which is a fast Python linter and formatter written in Rust.
Ruff uses tools such as Flake8, isort and Black and has good IDE support.

In order to lint and format all files run: 

```shell
./lint.sh
```
