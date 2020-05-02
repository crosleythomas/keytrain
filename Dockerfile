FROM python:3

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python3", "train.py", "--packs", "packs/git.txt", "packs/kubectl.txt"]

