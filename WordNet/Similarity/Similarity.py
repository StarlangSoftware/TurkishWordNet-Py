from abc import abstractmethod

from WordNet.SynSet import SynSet
from WordNet.WordNet import WordNet


class Similarity:

    wordNet: WordNet

    @abstractmethod
    def computeSimilarity(self, synSet1: SynSet, synSet2: SynSet) -> float:
        pass

    def __init__(self, wordNet: WordNet):
        self.wordNet = wordNet
