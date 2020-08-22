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

All Cards are represented in a text file representing a `Pack`.  A `Pack` text
file has the following format:

```
Name of Card 1
P: This is a prompt that will be given to a user for a single response prompt
R: This is the expected Reponse

Name of Card 2
P: This is a prompt with multiple expected responses
R: This is the first expected Response
R: This is the second expected Response

Name of Card 3
P: This is the first Prompt for a card with multiple Prompts
R: This is a response
P: This is the second Prompt
R: This is the first response to the second Prompt
R: This is the second response to the second Prompt
P: This could go on forever
R: But it won't
```


## Brainstorm

* Filter cards to train on (ex: only cards I missed last time, cards with expectation
of getting right < 80%, cards I haven't practiced with before, etc.). Implement this both
for the full deck (global CLI arg) and with per Pack option (CLI option to each Pack)
