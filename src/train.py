
import argparse
import random
from common.packfile_parser import PackfileParser
from common.trainer import Trainer

from src.protos.generated.card_pb2 import Card

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # TODO: validate these
    parser.add_argument('-p', '--packs', nargs='+', required=True, choices=list(PackfileParser.pack_map.keys()))

    # TOOD: Configure session. Can be either completely local or integrated with remote for pulling packs
    #   and reporting telemetry.

    args = parser.parse_args()

    packs = PackfileParser.load_packs(args.packs)

    trainer = Trainer(packs)

    trainer.train()
    
