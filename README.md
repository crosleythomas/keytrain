![Test, Build, Publish](https://github.com/crosleythomas/keytrain/workflows/Test,%20Build,%20Publish/badge.svg)

Welcome to flash cards for software engineers.

## Running the App

Invoke the training session with:
```
docker run -it keytrain -p <list of pack names to train on>

# Examples:
docker run -it keytrain -p git

docker run -it keytrain -p git kubectl
```

A series of flashcards will start printing out, for example:
```bash
➜  keytrain git:(master) ✗ docker run -it keytrain -p git kubectl
stop minikube and remove all associated resources
```

Type your answer and press `return`/`enter`.  If it is a multi-step answer,
enter the answer for each step and press `return`/`enter` between each.

Single-Step Answer:
```bash
➜  keytrain git:(master) ✗ docker run -it keytrain -p git kubectl
stop minikube and remove all associated resources
minikube delete
``` 

Multi-step Answer:
```bash
➜  keytrain git:(master) ✗ docker run -it keytrain -p git kubectl
add all locally modified files to a remote branch?
git add .
git commit -m "message"
git push
```

You will see either :white_check_mark: or :x: in response to your answer.
