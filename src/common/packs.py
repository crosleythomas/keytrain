import random
from IPython import embed


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
        """
        :param pack_data: a yaml object of the stored pack data
        """
        for k, v in pack_data.items():
            setattr(self, k, v)
        self.cards = [Card(c, "pack") for c in pack_data['spec']['template']['spec']['cards']]

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
    def __init__(self, card_data, data_source):
        """
        Constructor to create a card based on a set of raw data "lines"
        :param lines:
        """
        #embed()
        if data_source == "pack":
            self.name = card_data['name']
            self.turns = [Turn(td) for td in card_data['turns']]
        elif data_source == "card":
            self.name = card_data['metadata']['name']
            self.turns = [Turn(td) for td in card_data['spec']['turns']]


class Turn(object):
    """
    Contains a single Prompt with one or more Responses
    """
    def __init__(self, turn_data):
        self.prompt = Prompt(turn_data['prompt'])
        self.responses = [Response(rd) for rd in turn_data['response']]


class Prompt(object):
    def __init__(self, prompt_data):
        self.prompt = prompt_data


class Response(object):
    def __init__(self, response_data):
        self.response = response_data
