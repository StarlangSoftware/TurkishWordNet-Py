from WordNet.Similarity.Similarity import Similarity
from WordNet.SynSet import SynSet
from WordNet.WordNet import WordNet


class WuPalmer(Similarity):

    def __init__(self, wordNet: WordNet):
        super().__init__(wordNet)

    def computeSimilarity(self, synSet1: SynSet, synSet2: SynSet) -> float:
        pathToRootOfSynSet1 = self.wordNet.findPathToRoot(synSet1)
        pathToRootOfSynSet2 = self.wordNet.findPathToRoot(synSet2)
        LCSDepth = self.wordNet.findLCSDepth(pathToRootOfSynSet1, pathToRootOfSynSet2)
        return 2 * LCSDepth / (len(pathToRootOfSynSet1) + len(pathToRootOfSynSet2))
