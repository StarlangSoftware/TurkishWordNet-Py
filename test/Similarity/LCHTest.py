import unittest

from WordNet.Similarity.LCH import LCH
from WordNet.WordNet import WordNet


class LCHTest(unittest.TestCase):

    def test_ComputeSimilarity(self):
        turkish = WordNet("../../turkish_wordnet.xml")
        lch = LCH(turkish)
        self.assertAlmostEqual(2.8332, lch.computeSimilarity(turkish.getSynSetWithId("TUR10-0656390"), turkish.getSynSetWithId("TUR10-0600460")), 4)
        self.assertAlmostEqual(0.7673, lch.computeSimilarity(turkish.getSynSetWithId("TUR10-0412120"), turkish.getSynSetWithId("TUR10-0755370")), 4)
        self.assertAlmostEqual(0.6242, lch.computeSimilarity(turkish.getSynSetWithId("TUR10-0195110"), turkish.getSynSetWithId("TUR10-0822980")), 4)


if __name__ == '__main__':
    unittest.main()
