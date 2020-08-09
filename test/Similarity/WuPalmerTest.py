import unittest

from WordNet.Similarity.WuPalmer import WuPalmer
from WordNet.WordNet import WordNet


class WuPalmerTest(unittest.TestCase):

    def test_ComputeSimilarity(self):
        turkish = WordNet("../../turkish_wordnet.xml")
        wuPalmer = WuPalmer(turkish)
        self.assertAlmostEqual(0.9697, wuPalmer.computeSimilarity(turkish.getSynSetWithId("TUR10-0656390"), turkish.getSynSetWithId("TUR10-0600460")), 4)
        self.assertAlmostEqual(0.1739, wuPalmer.computeSimilarity(turkish.getSynSetWithId("TUR10-0066050"), turkish.getSynSetWithId("TUR10-1198750")), 4)
        self.assertAlmostEqual(0.3636, wuPalmer.computeSimilarity(turkish.getSynSetWithId("TUR10-0012910"), turkish.getSynSetWithId("TUR10-0172740")), 4)
        self.assertAlmostEqual(0.25, wuPalmer.computeSimilarity(turkish.getSynSetWithId("TUR10-0412120"), turkish.getSynSetWithId("TUR10-0755370")), 4)
        self.assertAlmostEqual(0.3636, wuPalmer.computeSimilarity(turkish.getSynSetWithId("TUR10-0195110"), turkish.getSynSetWithId("TUR10-0822980")), 4)


if __name__ == '__main__':
    unittest.main()
