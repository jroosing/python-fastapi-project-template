# Python FastAPI Project Template
This project functions as a template for FastAPI projects. 
It is opinionated and loosely follows a DDD type of directory structure

*note:* This example assumes python is called using "python3". your installation may differ.

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

## Linting and formatting
My preference goes to ruff, which is a fast Python linter and formatter written in Rust.
Ruff uses tools such as Flake8, isort and Black and has good IDE support.

In order to lint and format all files run: 

```shell
./lint.sh
```