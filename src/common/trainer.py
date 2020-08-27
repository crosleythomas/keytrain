from src.common.packs import Deck

class Trainer(object):

    def __init__(self, packs):
        self.packs = packs

    def train(self):
        pass

    def train_sample(sample):
        print(sample[0])
        for solution in sample[1]:
            ans = input('')
            if not ans == solution:
                print(u'\u274C')
                for soln in sample[1]:
                    print(soln)
                print()
                return
        print(u'\u2705' + '\n')

    def train_pack(packs):
        samples = read_packs(packs)
        random.shuffle(samples)

        for sample in samples:
            train_sample(sample)

