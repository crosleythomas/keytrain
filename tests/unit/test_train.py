import pytest
import os

class TestTrain:
    @pytest.mark.skip
    def test_read_pack(self, tmpdir):
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
        assert samples == [("question1", ["answer1.1", "answer1.2"]), ("question2", ["answer2"])]

    @pytest.mark.skip
    def test_read_packs(self, tmpdir):
        d = tmpdir.mkdir("packs")

        f1 = d.join("pack1.txt")
        f1.write("""question1
answer1.1
answer1.2

question2
answer2

""")
        f1_path = os.path.join(f1.dirname, f1.basename)

        f2 = d.join("pack2.txt")
        f2.write("""question3
answer3.1
answer3.2

question4 
answer4

""")
        f2_path = os.path.join(f2.dirname, f2.basename)

        samples = read_packs([f1_path, f2_path])
        assert samples == [
            ("question1", ["answer1.1", "answer1.2"]),
            ("question2", ["answer2"]),
            ("question3", ["answer3.1", "answer3.2"]),
            ("question4", ["answer4"])
        ]
