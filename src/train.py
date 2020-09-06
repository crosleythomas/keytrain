
import argparse

from src.common.packfile_parser import PackfileParser
from src.common.trainer import Trainer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # TODO: validate these
    parser.add_argument('-c', '--cards', nargs='+', required=True, )
    parser.add_argument('-p', '--packs', nargs='+', required=True, choices=list(PackfileParser.pack_map.keys()))

    # TOOD: Configure session. Can be either completely local or integrated with remote for pulling packs
    #   and reporting telemetry.

    args = parser.parse_args()

    cards = PackfileParser.load_cards(args.cards)
    packs = PackfileParser.load_packs(args.packs)

    for pack in packs:
        cards.extend(pack.cards)

    print("Training on %d cards." % len(cards))
    for card in cards:
        print(card.name)

    print("\n")
    trainer = Trainer(cards)
    trainer.shuffle()

    trainer.train()
