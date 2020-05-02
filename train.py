
import argparse
import random


def read_pack(pack):
    lines = [l.rstrip() for l in open(pack).readlines()]
    samples = []
    description, solution = None, []
    for line in lines:
        if len(line) == 0:
            samples.append((description, solution))
            description, solution = None, []
        elif description is None:
            description = line
        else:
            solution.append(line)
    return samples


def read_packs(packs):
    samples = []
    for pack in packs:
        samples.extend(read_pack(pack))
    return samples


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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--packs', nargs='+')

    args = parser.parse_args()

    packs_paths = args.packs

    train_pack(args.packs)

