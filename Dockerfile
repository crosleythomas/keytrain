FROM python:3

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python3", "src/train.py"]

