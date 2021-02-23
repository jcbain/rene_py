FROM python:3.10.0a5-buster
WORKDIR .
COPY . .
ENTRYPOINT ["python", "clean.py"]