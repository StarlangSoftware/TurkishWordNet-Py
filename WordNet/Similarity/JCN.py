from WordNet.Similarity.ICSimilarity import ICSimilarity
from WordNet.SynSet import SynSet
from WordNet.WordNet import WordNet


class JCN(ICSimilarity):

    def __init__(self, wordNet: WordNet, informationContents: dict):
        super().__init__(wordNet, informationContents)

    def computeSimilarity(self, synSet1: SynSet, synSet2: SynSet) -> float:
        pathToRootOfSynSet1 = self.wordNet.findPathToRoot(synSet1)
        pathToRootOfSynSet2 = self.wordNet.findPathToRoot(synSet2)
        LCSid = self.wordNet.findLCSid(pathToRootOfSynSet1, pathToRootOfSynSet2)
        return 1 / (self.informationContents[synSet1.getId()] + self.informationContents[synSet2.getId()] -
                    2 * self.informationContents[LCSid])
