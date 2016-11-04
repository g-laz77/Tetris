import essen

class Test_essen:
    def test_calcLevel(self):
        ans = essen.calcLevel(200)
        assert ans == 1

    def test_calcfreq(self):
        ans = essen.calcFallFreq(400)
        assert ans == 0.4

    def test_OnBoard(self):
        ans = essen.onBoard(12, 33)
        assert not ans
