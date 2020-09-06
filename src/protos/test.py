from generated.card_pb2 import *

class CardData(Card):
    def __init__(self):
        print(self.apiVersion)


cd = CardData()
