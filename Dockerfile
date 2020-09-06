FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/src/app/run.sh"]

