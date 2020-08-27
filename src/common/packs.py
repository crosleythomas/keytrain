import random

class Deck(object):
    """
    A Deck is created using cards from one or more packs
    """
    def __init__(self, pack_names):
        self.packs = [Pack(n) for n in pack_names]

    @classmethod
    def from_spec(cls, spec):
        return cls()

class Pack(object):
    """
    Represents a single flash card pack - a grouping of related Cards
    created by a user.
    """
    def __init__(self, pack_data):
        for k, v in pack_data.items():
            setattr(self, k, v)
        self.cards = [Card(c) for c in self.spec['cards']]

    def shuffle(self):
        random.shuffle(self.cards)

class Card(object):
    """
    Contains one or more Turns

    The atomic unit of a concept to be learned.  A Card can take many forms,
    but it:
        * Cannot be broken into smaller pieces when shuffling a Pack
        * Is always asked in a deterministic order
        * Does not take any input to its first step
        * Must implement some form of equality

    Types of cards:
        * Single question, single answer
        * Single question, multi-part answer
        * Multi-part question, response, question, response

    Brainstorm
        * Make a Card aware of what pack it came from
        * For multi-step answers, provide abstraction so we can track where
            in the answer the user gets the question wrong
        * Make it easy to implement different forms of equality (strict equals, wild-carded, regex, etc)
        * Ability to store metadata about the card so we can add features in the future
            * ex - average difficulty, expected difficulty for current user, last guessed currectly
    """
    def __init__(self, spec):
        """
        Constructor to create a card based on a set of raw data "lines"
        :param lines:
        """
        for k, v in spec.items():
            setattr(self, k, v)
        print(dir(self))


class Turn(object):
    """
    Contains a single Prompt with one or more Responses
    """
    def __init__(self, prompt, responses):
        self.prompt = prompt
        self.responses = responses
        pass

class Prompt(object):
    def __init__(self):
        pass

class Response(object):
    def __init__(self):
        pass
