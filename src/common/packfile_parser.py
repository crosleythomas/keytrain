from common.packs import Pack

import os
import yaml


class PackfileParser(object):
    """
    Utilities for converting stored Pack/Card data into usable objects.
    """

    pack_data_root = '/usr/src/app/packs/'
    pack_map = {
        'git' : 'git.yaml',
        'kubectl' : 'kubectl.yaml'
    }

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
        Pack(pack_data)

    @staticmethod
    def validate_pack_data(pack_data):
        # TODO
        pass

    @staticmethod
    def load_local_pack_data(pack_name):
        return yaml.load(open(os.path.join(PackfileParser.pack_data_root, PackfileParser.pack_map[pack_name])))
