from abc import abstractmethod

from WordNet.Similarity.Similarity import Similarity
from WordNet.WordNet import WordNet


class ICSimilarity(Similarity):

    informationContents: dict

    def __init__(self, wordNet: WordNet, informationContents: dict):
        super().__init__(wordNet)
        self.informationContents = informationContents
