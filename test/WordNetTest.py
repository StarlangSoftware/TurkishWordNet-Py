import unittest

from Dictionary.Pos import Pos

from WordNet.WordNet import WordNet
from WordNet.literal import Literal
from WordNet.SemanticRelationType import SemanticRelationType


class WordNetTest(unittest.TestCase):
    
    turkish: WordNet

    def setUp(self) -> None:
        self.turkish = WordNet()

    def test_SynSetList(self):
        literalCount = 0
        for synSet in self.turkish.synSetList():
            literalCount += synSet.getSynonym().literalSize()
        self.assertEquals(110236, literalCount)

    def test_WikiPage(self):
        wikiPageCount = 0
        for synSet in self.turkish.synSetList():
            if synSet.getWikiPage() is not None:
                wikiPageCount = wikiPageCount + 1
        self.assertEquals(10987, wikiPageCount)

    def test_LiteralList(self):
        self.assertEquals(82255, len(self.turkish.literalList()))

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
        self.assertEquals(1, self.turkish.numberOfSynSetsWithLiteral("yolcu etmek"))
        self.assertEquals(2, self.turkish.numberOfSynSetsWithLiteral("açık pembe"))
        self.assertEquals(3, self.turkish.numberOfSynSetsWithLiteral("bürokrasi"))
        self.assertEquals(4, self.turkish.numberOfSynSetsWithLiteral("bordür"))
        self.assertEquals(5, self.turkish.numberOfSynSetsWithLiteral("duygulanım"))
        self.assertEquals(6, self.turkish.numberOfSynSetsWithLiteral("sarsıntı"))
        self.assertEquals(7, self.turkish.numberOfSynSetsWithLiteral("kuvvetli"))
        self.assertEquals(8, self.turkish.numberOfSynSetsWithLiteral("merkez"))
        self.assertEquals(9, self.turkish.numberOfSynSetsWithLiteral("yüksek"))
        self.assertEquals(10, self.turkish.numberOfSynSetsWithLiteral("biçim"))
        self.assertEquals(11, self.turkish.numberOfSynSetsWithLiteral("yurt"))
        self.assertEquals(12, self.turkish.numberOfSynSetsWithLiteral("iğne"))
        self.assertEquals(13, self.turkish.numberOfSynSetsWithLiteral("kol"))
        self.assertEquals(14, self.turkish.numberOfSynSetsWithLiteral("alem"))
        self.assertEquals(15, self.turkish.numberOfSynSetsWithLiteral("taban"))
        self.assertEquals(16, self.turkish.numberOfSynSetsWithLiteral("yer"))
        self.assertEquals(17, self.turkish.numberOfSynSetsWithLiteral("ağır"))
        self.assertEquals(18, self.turkish.numberOfSynSetsWithLiteral("iş"))
        self.assertEquals(19, self.turkish.numberOfSynSetsWithLiteral("dökmek"))
        self.assertEquals(20, self.turkish.numberOfSynSetsWithLiteral("kaldırmak"))
        self.assertEquals(21, self.turkish.numberOfSynSetsWithLiteral("girmek"))
        self.assertEquals(22, self.turkish.numberOfSynSetsWithLiteral("gitmek"))
        self.assertEquals(23, self.turkish.numberOfSynSetsWithLiteral("vermek"))
        self.assertEquals(24, self.turkish.numberOfSynSetsWithLiteral("olmak"))
        self.assertEquals(25, self.turkish.numberOfSynSetsWithLiteral("bırakmak"))
        self.assertEquals(26, self.turkish.numberOfSynSetsWithLiteral("çıkarmak"))
        self.assertEquals(27, self.turkish.numberOfSynSetsWithLiteral("kesmek"))
        self.assertEquals(28, self.turkish.numberOfSynSetsWithLiteral("açmak"))
        self.assertEquals(33, self.turkish.numberOfSynSetsWithLiteral("düşmek"))
        self.assertEquals(38, self.turkish.numberOfSynSetsWithLiteral("atmak"))
        self.assertEquals(39, self.turkish.numberOfSynSetsWithLiteral("geçmek"))
        self.assertEquals(44, self.turkish.numberOfSynSetsWithLiteral("çekmek"))
        self.assertEquals(50, self.turkish.numberOfSynSetsWithLiteral("tutmak"))
        self.assertEquals(59, self.turkish.numberOfSynSetsWithLiteral("çıkmak"))

    def test_GetSynSetsWithPartOfSpeech(self):
        self.assertEquals(43869, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.NOUN)))
        self.assertEquals(17772, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.VERB)))
        self.assertEquals(12410, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.ADJECTIVE)))
        self.assertEquals(2549, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.ADVERB)))
        self.assertEquals(1552, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.INTERJECTION)))
        self.assertEquals(68, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.PRONOUN)))
        self.assertEquals(61, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.CONJUNCTION)))
        self.assertEquals(30, len(self.turkish.getSynSetsWithPartOfSpeech(Pos.PREPOSITION)))

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
        self.assertEquals(1, len(self.turkish.getInterlingual("ENG31-05674544-n")))
        self.assertEquals(2, len(self.turkish.getInterlingual("ENG31-00220161-r")))
        self.assertEquals(3, len(self.turkish.getInterlingual("ENG31-02294200-v")))
        self.assertEquals(4, len(self.turkish.getInterlingual("ENG31-06205574-n")))
        self.assertEquals(5, len(self.turkish.getInterlingual("ENG31-02687605-v")))
        self.assertEquals(6, len(self.turkish.getInterlingual("ENG31-01099197-n")))
        self.assertEquals(7, len(self.turkish.getInterlingual("ENG31-00587299-n")))
        self.assertEquals(9, len(self.turkish.getInterlingual("ENG31-02214901-v")))
        self.assertEquals(10, len(self.turkish.getInterlingual("ENG31-02733337-v")))
        self.assertEquals(19, len(self.turkish.getInterlingual("ENG31-00149403-v")))

    def test_Size(self):
        self.assertEquals(78311, self.turkish.size())

    def test_FindPathToRoot(self):
        self.assertEquals(1, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0814560"))))
        self.assertEquals(2, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0755370"))))
        self.assertEquals(3, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0516010"))))
        self.assertEquals(4, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0012910"))))
        self.assertEquals(5, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0046370"))))
        self.assertEquals(6, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0186560"))))
        self.assertEquals(7, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0172740"))))
        self.assertEquals(8, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0195110"))))
        self.assertEquals(9, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0285060"))))
        self.assertEquals(10, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0066050"))))
        self.assertEquals(11, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0226380"))))
        self.assertEquals(12, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0490230"))))
        self.assertEquals(13, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-1198750"))))
        self.assertEquals(12, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0412120"))))
        self.assertEquals(13, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-1116690"))))
        self.assertEquals(13, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0621870"))))
        self.assertEquals(14, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0822980"))))
        self.assertEquals(15, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0178450"))))
        self.assertEquals(16, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0600460"))))
        self.assertEquals(17, len(self.turkish.findPathToRoot(self.turkish.getSynSetWithId("TUR10-0656390"))))

    def test_literal(self):
        expected = Literal("kuş", 1, "TUR10-0863380")
        expected_relation_type = SemanticRelationType.DOMAIN_TOPIC

        actual = self.turkish.getSynSetWithLiteral("kuş", 1).getSynonym().getLiteral(0)
        self.assertEqual(expected, actual)
        self.assertEqual("kuş 1", str(expected))
        self.assertEqual(1, len(actual.relations))
        self.assertEqual(expected_relation_type, actual.relations[0].getRelationType())
        self.assertTrue(actual.contains_relation_type(expected_relation_type))


if __name__ == '__main__':
    unittest.main()
