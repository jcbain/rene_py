FROM python:3.10.0a5-buster
WORKDIR /code
COPY . .
ENTRYPOINT ["python"]