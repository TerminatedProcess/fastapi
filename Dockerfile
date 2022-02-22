FROM python:3.9.7

WORKDIR /usr/src/app

RUN apt update && apt upgrade -y && apt autoremove

RUN /usr/local/bin/python -m pip install --upgrade pip

# Setup Poetry
RUN pip install poetry

RUN /usr/local/bin/poetry config virtualenvs.in-project true

#Copy in config files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN cat ./login_script.sh >> /root/.bashrc

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]