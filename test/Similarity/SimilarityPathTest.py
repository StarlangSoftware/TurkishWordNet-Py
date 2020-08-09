import unittest

from WordNet.Similarity.SimilarityPath import SimilarityPath
from WordNet.WordNet import WordNet


class SimilarityPathTest(unittest.TestCase):

    def test_ComputeSimilarity(self):
        turkish = WordNet("../../turkish_wordnet.xml")
        similarityPath = SimilarityPath(turkish)
        self.assertAlmostEqual(32.0, similarityPath.computeSimilarity(turkish.getSynSetWithId("TUR10-0656390"), turkish.getSynSetWithId("TUR10-0600460")), 4)
        self.assertAlmostEqual(6.0, similarityPath.computeSimilarity(turkish.getSynSetWithId("TUR10-0066050"), turkish.getSynSetWithId("TUR10-1198750")), 4)
        self.assertAlmostEqual(6.0, similarityPath.computeSimilarity(turkish.getSynSetWithId("TUR10-0012910"), turkish.getSynSetWithId("TUR10-0172740")), 4)
        self.assertAlmostEqual(15.0, similarityPath.computeSimilarity(turkish.getSynSetWithId("TUR10-0412120"), turkish.getSynSetWithId("TUR10-0755370")), 4)
        self.assertAlmostEqual(13.0, similarityPath.computeSimilarity(turkish.getSynSetWithId("TUR10-0195110"), turkish.getSynSetWithId("TUR10-0822980")), 4)


if __name__ == '__main__':
    unittest.main()
