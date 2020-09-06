from src.common.packs import Card, Pack

import os
import yaml


class PackfileParser(object):
    """
    Utilities for converting stored Pack/Card data into usable objects.
    """

    card_data_root = '/usr/src/app/packs/'
    pack_data_root = '/usr/src/app/packs/'

    card_map = {
        'single' : 'single.yaml'
    }
    pack_map = {
        'git' : 'git.yaml',
        'kubectl' : 'kubectl.yaml',
        'single': 'single.yaml'
    }

    #################################
    ###   Pack specific loaders   ###
    #################################
    @staticmethod
    def load_packs(pack_names):
        """
        Takes a list of pack names, creates the associated Pack and Card objects, and returns them
        :param pack_names: list of strings
        :return:
        """
        return [PackfileParser.load_pack(p) for p in pack_names]

    @staticmethod
    def load_pack(pack_name):
        pack_data = PackfileParser.load_local_pack_data(pack_name)
        return Pack(pack_data)

    @staticmethod
    def validate_pack_data(pack_data):
        # TODO
        pass

    @staticmethod
    def load_local_pack_data(pack_name):
        return yaml.load(open(os.path.join(PackfileParser.pack_data_root, PackfileParser.pack_map[pack_name])))

    #################################
    ###   Card specific loaders   ###
    #################################
    @staticmethod
    def load_cards(card_names):
        return [PackfileParser.load_card(card_name) for card_name in card_names]

    @staticmethod
    def load_card(card_name):
        card_data = PackfileParser.load_local_card_data(card_name)
        return Card(card_data, "card")

    @staticmethod
    def load_local_card_data(card_name):
        return yaml.load(open(os.path.join(PackfileParser.card_data_root, PackfileParser.pack_map[card_name])))
