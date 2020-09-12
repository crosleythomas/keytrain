![Test, Build, Publish](https://github.com/crosleythomas/keytrain/workflows/Test,%20Build,%20Publish/badge.svg)
![Code Coverage](https://img.shields.io/codecov/c/github/crosleythomas/keytrain)

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
docker run -it keytrain -p git kubectl
stop minikube and remove all associated resources
minikube delete
``` 

Multi-step Answer:
```bash
docker run -it keytrain -p git kubectl
add all locally modified files to a remote branch?
git add .
git commit -m "message"
git push
```

You will see either :white_check_mark: or :x: in response to your answer.
## Development

Run the image without re-building every time with:
```
docker run  -v $(pwd):/usr/src/app keytrain -p git kubectl
```

## Design

### Data Model

The primary abstractions are:
* `Deck` - the group of Cards a user is training with currently. A Deck can have Cards
from one or more Packs.
* `Pack` - a group of Cards stored together in a logical group
* `Card` - the atomic unit of a concept to be trained on, containing one or more Turns
* `Turn` - a Prompt with an expected series of Responses (answers)
* `Prompt` - the prompt given to the user to solicit a response
* `Response` - the expected input from the user to answer the `Prompt` correctly


### Flashcard Data Storage Format

All Cards are represented in yaml files taking inspiration from Kubernetes objects.
There are currently two definitions representing a `Pack` and a `Card`.  This
format makes it easy to define simple cards and is also extensible to add in
metadata as the system grows to use features like labels, selectors, annotations, etc.

```
apiVersion: beta1
type: Pack
metadata:
    name: Github CLI Commands
spec:
  template:
    metadata:
      labels:
        pack: github
    spec:
      cards:
      - name: Github Empty Commit
        turns:
        - prompt: push an empty commit
          response:
          - git commit --allow-empty -m "message"
      - name: Commit Local Changes
        turns:
        - prompt: add all locally modified files to a remote branch?
          response:
          - git add .
          - git commit -m "message"
          - git push


---
apiVersion: beta1
type: Card
metadata:
  name: Example Single Card
spec:
  name: A Sample prompt
  turns:
  - prompt: first prompt
    response:
    - first response
  - prompt: second prompt
    response:
    - second response

```

## Brainstorm

* Filter cards to train on (ex: only cards I missed last time, cards with expectation
of getting right < 80%, cards I haven't practiced with before, etc.). Implement this both
for the full deck (global CLI arg) and with per Pack option (CLI option to each Pack)
* Create IntelliJ plugin to easily create cards/packs
* Add labels and selectors to gather certain cards
* Add annotations on cards for things like `lastTimeCorrect`, `lastTimeIncorrect`, `probabilityCorrect`
* Auto-import content from "cheat-sheet" style data banks, i.e. https://devhints.io/bash
* Define markup language for responses (regex-ish?) to allow for varying, correct answers
    * Define escape characters
* Add ability to say assumptions for a Pack/Card
    * i.e. "(kubectl pack) Assume namespace is default unless otherwise specified."