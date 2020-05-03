import pytest
import os

from src.train import *


class TestTrain:
    def test_read_pack(self, tmpdir):
        print(tmpdir)
        d = tmpdir.mkdir("packs")
        f = d.join("pack1.txt")
        f.write("""question1
answer1.1
answer1.2

question2
answer2

""")
        filename = os.path.join(f.dirname, f.basename)
        samples = read_pack(filename)
        print('Samples: ' % samples)
        assert isinstance(samples, list)
        assert samples == [("question1", ["answer1.1", "answer1.2"]), ("question2", ["answer2"])]
