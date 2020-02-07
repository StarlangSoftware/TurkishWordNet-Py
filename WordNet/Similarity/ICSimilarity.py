from WordNet.Similarity.Similarity import Similarity
from WordNet.SynSet import SynSet
from WordNet.WordNet import WordNet


class ICSimilarity(Similarity):

    informationContents: dict

    def __init__(self, wordNet: WordNet, informationContents: dict):
        super().__init__(wordNet)
        self.informationContents = informationContents

    def computeSimilarity(self, synSet1: SynSet, synSet2: SynSet) -> float:
        pass
