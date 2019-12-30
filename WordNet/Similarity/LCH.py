from WordNet.Similarity.Similarity import Similarity
from WordNet.SynSet import SynSet
from WordNet.WordNet import WordNet
import math


class LCH(Similarity):

    def __init__(self, wordNet: WordNet):
        super().__init__(wordNet)

    def computeSimilarity(self, synSet1: SynSet, synSet2: SynSet) -> float:
        pathToRootOfSynSet1 = self.wordNet.findPathToRoot(synSet1)
        pathToRootOfSynSet2 = self.wordNet.findPathToRoot(synSet2)
        pathLength = self.wordNet.findPathLength(pathToRootOfSynSet1, pathToRootOfSynSet2)
        maxDepth = max(len(pathToRootOfSynSet1), len(pathToRootOfSynSet2))
        return -math.log(pathLength / (2 * maxDepth))
