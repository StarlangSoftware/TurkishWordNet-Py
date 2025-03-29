import unittest

from DataStructure.CounterHashMap import CounterHashMap
from Dictionary.Pos import Pos

from WordNet.WordNet import WordNet


class WordNetTest(unittest.TestCase):
    
    turkish: WordNet

    def setUp(self) -> None:
        self.turkish = WordNet()

    def test_SynSetList(self):
        literalCount = 0
        for synSet in self.turkish.synSetList():
            literalCount += synSet.getSynonym().literalSize()
        self.assertEqual(110259, literalCount)

    def test_WikiPage(self):
        wikiPageCount = 0
        for synSet in self.turkish.synSetList():
            if synSet.getWikiPage() is not None:
                wikiPageCount = wikiPageCount + 1
        self.assertEqual(11001, wikiPageCount)

    def test_TotalForeignLiterals(self):
        count = 0
        for synSet in self.turkish.synSetList():
            for i in range(synSet.getSynonym().literalSize()):
                if synSet.getSynonym().getLiteral(i).getOrigin() is not None:
                    count = count + 1
        self.assertEqual(3981, count)

    def test_TotalGroupedLiterals(self):
        count = 0
        for synSet in self.turkish.synSetList():
            for i in range(synSet.getSynonym().literalSize()):
                if synSet.getSynonym().getLiteral(i).getGroupNo() != 0:
                    count = count + 1
        self.assertEqual(5973, count)

    def test_GroupSize(self):
        groups = CounterHashMap()
        for synSet in self.turkish.synSetList():
            literal_groups = synSet.getSynonym().getUniqueLiterals()
            for synonym in literal_groups:
                if synonym.getLiteral(0).getGroupNo() != 0:
                    groups.put(synonym.literalSize())
        self.assertEqual(0, groups.count(1))
        self.assertEqual(2949, groups.count(2))
        self.assertEqual(21, groups.count(3))
        self.assertEqual(3, groups.count(4))

    def test_LiteralList(self):
        self.assertEqual(82276, len(self.turkish.literalList()))

    def test_GetSynSetWithId(self):
        self.assertIsNotNone(self.turkish.getSynSetWithId("TUR10-0000040"))
        self.assertIsNotNone(self.turkish.getSynSetWithId("TUR10-0648550"))
        self.assertIsNotNone(self.turkish.getSynSetWithId("TUR10-1034170"))
        self.assertIsNotNone(self.turkish.getSynSetWithId("TUR10-1047180"))
        self.assertIsNotNone(self.turkish.getSynSetWithId("TUR10-1196250"))

    def test_GetSynSetWithLiteral(self):
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("sıradaki", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("Türkçesi", 2))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("tropikal orman", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("mesut olmak", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("acı badem kurabiyesi", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("açık kapı siyaseti", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("bir baştan bir başa", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("eş zamanlı dil bilimi", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("bir iğne bir iplik olmak", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("yedi kat yerin dibine geçmek", 2))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("kedi gibi dört ayak üzerine düşmek", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("bir kulağından girip öbür kulağından çıkmak", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("anasından emdiği süt burnundan fitil fitil gelmek", 1))
        self.assertIsNotNone(self.turkish.getSynSetWithLiteral("bir ayak üstünde kırk yalanın belini bükmek", 1))

    def test_NumberOfSynSetsWithLiteral(self):
        self.assertEqual(1, self.turkish.numberOfSynSetsWithLiteral("yolcu etmek"))
        self.assertEqual(2, self.turkish.numberOfSynSetsWithLiteral("açık pembe"))
        self.assertEqual(3, self.turkish.numberOfSynSetsWithLiteral("bürokrasi"))
        self.assertEqual(4, self.turkish.numberOfSynSetsWithLiteral("bordür"))
        self.assertEqual(5, self.turkish.numberOfSynSetsWithLiteral("duygulanım"))
        self.assertEqual(6, self.turkish.numberOfSynSetsWithLiteral("sarsıntı"))
        self.assertEqual(7, self.turkish.numberOfSynSetsWithLiteral("kuvvetli"))
        self.assertEqual(8, self.turkish.numberOfSynSetsWithLiteral("merkez"))
        self.assertEqual(9, self.turkish.numberOfSynSetsWithLiteral("yüksek"))
        self.assertEqual(10, self.turkish.numberOfSynSetsWithLiteral("biçim"))
        self.assertEqual(11, self.turkish.numberOfSynSetsWithLiteral("yurt"))
        self.assertEqual(12, self.turkish.numberOfSynSetsWithLiteral("iğne"))
        self.assertEqual(13, self.turkish.numberOfSynSetsWithLiteral("kol"))
        self.assertEqual(14, self.turkish.numberOfSynSetsWithLiteral("alem"))
        self.assertEqual(15, self.turkish.numberOfSynSetsWithLiteral("taban"))
        self.assertEqual(16, self.turkish.numberOfSynSetsWithLiteral("yer"))
        self.assertEqual(17, self.turkish.numberOfSynSetsWithLiteral("ağır"))
        self.assertEqual(18, self.turkish.numberOfSynSetsWithLiteral("iş"))
        self.assertEqual(19, self.turkish.numberOfSynSetsWithLiteral("dökmek"))
        self.assertEqual(20, self.turkish.numberOfSynSetsWithLiteral("kaldırmak"))
        self.assertEqual(21, self.turkish.numberOfSynSetsWithLiteral("girmek"))
        self.assertEqual(22, self.turkish.numberOfSynSetsWithLiteral("gitmek"))
        self.assertEqual(23, self.turkish.numberOfSynSetsWithLiteral("vermek"))
        self.assertEqual(24, self.turkish.numberOfSynSetsWithLiteral("olmak"))
        self.assertEqual(25, self.turkish.numberOfSynSetsWithLiteral("bırakmak"))
        self.assertEqual(26, self.turkish.numberOfSynSetsWithLiteral("çıkarmak"))
        self.assertEqual(27, self.turkish.numberOfSynSetsWithLiteral("kesmek"))
        self.assertEqual(28, self.turkish.numberOfSynSetsWithLiteral("açmak"))
        self.assertEqual(33, self.turkish.numberOfSynSetsWithLiteral("düşmek"))
        self.assertEqual(38, self.turkish.numberOfSynSetsWithLiteral("atmak"))
        self.assertEqual(39, self.turkish.numberOfSynSetsWithLiteral("geçmek"))
        self.assertEqual(44, self.turkish.numberOfSynSetsWithLiteral("çekmek"))
        self.assertEqual(50, self.turkish.numberOfSynSetsWithLiteral("tutmak"))
        self.assertEqual(59, self.turkish.numberOfSynSetsWithLiteral("çıkmak"))

    def test_GetSynSetsWithPartOfSpeech(self):
        self.assertEqual(43882, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.NOUN)))
        self.assertEqual(17773, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.VERB)))
        self.assertEqual(12406, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.ADJECTIVE)))
        self.assertEqual(2549, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.ADVERB)))
        self.assertEqual(1552, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.INTERJECTION)))
        self.assertEqual(74, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.PRONOUN)))
        self.assertEqual(61, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.CONJUNCTION)))
        self.assertEqual(30, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.PREPOSITION)))

    def test_GetLiteralsWithPossibleModifiedLiteral(self):
        english = WordNet("../WordNet/data/english_wordnet_version_31.xml", "../WordNet/data/english_exception.xml")
        self.assertTrue("go" in english.getLiteralsWithPossibleModifiedLiteral("went"))
        self.assertTrue("go" in english.getLiteralsWithPossibleModifiedLiteral("going"))
        self.assertTrue("go" in english.getLiteralsWithPossibleModifiedLiteral("gone"))
        self.assertTrue("be" in english.getLiteralsWithPossibleModifiedLiteral("was"))
        self.assertTrue("be" in english.getLiteralsWithPossibleModifiedLiteral("were"))
        self.assertTrue("be" in english.getLiteralsWithPossibleModifiedLiteral("been"))
        self.assertTrue("have" in english.getLiteralsWithPossibleModifiedLiteral("had"))
        self.assertTrue("play" in english.getLiteralsWithPossibleModifiedLiteral("played"))
        self.assertTrue("play" in english.getLiteralsWithPossibleModifiedLiteral("plays"))
        self.assertTrue("orange" in english.getLiteralsWithPossibleModifiedLiteral("oranges"))
        self.assertTrue("good" in english.getLiteralsWithPossibleModifiedLiteral("better"))
        self.assertTrue("well" in english.getLiteralsWithPossibleModifiedLiteral("better"))
        self.assertTrue("good" in english.getLiteralsWithPossibleModifiedLiteral("best"))
        self.assertTrue("well" in english.getLiteralsWithPossibleModifiedLiteral("best"))
        self.assertTrue("bad" in english.getLiteralsWithPossibleModifiedLiteral("worse"))
        self.assertTrue("bad" in english.getLiteralsWithPossibleModifiedLiteral("worst"))
        self.assertTrue("ugly" in english.getLiteralsWithPossibleModifiedLiteral("uglier"))
        self.assertTrue("ugly" in english.getLiteralsWithPossibleModifiedLiteral("ugliest"))
        self.assertTrue("bus" in english.getLiteralsWithPossibleModifiedLiteral("buses"))
        self.assertTrue("fly" in english.getLiteralsWithPossibleModifiedLiteral("flies"))
        self.assertTrue("leaf" in english.getLiteralsWithPossibleModifiedLiteral("leaves"))

    def test_GetInterlingual(self):
        self.assertEqual(1, len(self.turkish.getInterlingual("ENG31-05674544-n")))
        self.assertEqual(2, len(self.turkish.getInterlingual("ENG31-00220161-r")))
        self.assertEqual(3, len(self.turkish.getInterlingual("ENG31-02294200-v")))
        self.assertEqual(4, len(self.turkish.getInterlingual("ENG31-06205574-n")))
        self.assertEqual(5, len(self.turkish.getInterlingual("ENG31-02687605-v")))
        self.assertEqual(6, len(self.turkish.getInterlingual("ENG31-01099197-n")))
        self.assertEqual(7, len(self.turkish.getInterlingual("ENG31-00587299-n")))
        self.assertEqual(9, len(self.turkish.getInterlingual("ENG31-02214901-v")))
        self.assertEqual(10, len(self.turkish.getInterlingual("ENG31-02733337-v")))
        self.assertEqual(19, len(self.turkish.getInterlingual("ENG31-00149403-v")))

    def test_Size(self):
        self.assertEqual(78327, self.turkish.size())

    def test_FindPathToRoot(self):
        self.assertEqual(1, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0814560"))))
        self.assertEqual(2, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0755370"))))
        self.assertEqual(3, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0516010"))))
        self.assertEqual(4, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0012910"))))
        self.assertEqual(5, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0046370"))))
        self.assertEqual(6, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0186560"))))
        self.assertEqual(7, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0172740"))))
        self.assertEqual(8, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0195110"))))
        self.assertEqual(9, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0285060"))))
        self.assertEqual(10, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0066050"))))
        self.assertEqual(11, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0226380"))))
        self.assertEqual(12, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0490230"))))
        self.assertEqual(13, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-1198750"))))
        self.assertEqual(12, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0412120"))))
        self.assertEqual(13, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-1116690"))))
        self.assertEqual(13, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0621870"))))
        self.assertEqual(14, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0822980"))))
        self.assertEqual(15, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0178450"))))
        self.assertEqual(16, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0600460"))))
        self.assertEqual(17, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0656390"))))


if __name__ == '__main__':
    unittest.main()
