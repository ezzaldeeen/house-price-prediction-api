FROM python:3.8-slim-buster

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app .

ENV APP_CONFIGURATION='src.config.ProductionConfig'


CMD [ "python", "run.py" ]


