from random import shuffle

class Trainer(object):

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        shuffle(self.cards)

    def train(self):
        for card in self.cards:
            Trainer.train_card(card)

    @staticmethod
    def train_card(card):
        for turn in card.turns:
            print(turn.prompt.prompt)
            for response in turn.responses:
                ans = input('')
                if not ans == response.response:
                    print(u'\u274C')
                    for response in turn.responses:
                        print(response.response)
                    print()
                    return
        print(u'\u2705' + '\n')
