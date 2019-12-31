import xml.etree.ElementTree
from collections import OrderedDict

from Dictionary.ExceptionalWord import ExceptionalWord
from Dictionary.Pos import Pos
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse

from WordNet.InterlingualRelation import InterlingualRelation
from WordNet.Literal import Literal
from WordNet.SemanticRelation import SemanticRelation
from WordNet.SemanticRelationType import SemanticRelationType
from WordNet.SynSet import SynSet


class WordNet:
    __synSetList: OrderedDict
    __literalList: OrderedDict
    __exceptionList: dict
    __interlingualList: dict

    """
    Constructor that initializes the SynSet list, literal list, reads exception.

    PARAMETERS
    ----------
    fileName : str
        Resource to be read for the WordNet.
    """

    def __init__(self, fileName: str = None, exceptionFileName: str = None):
        if fileName is None:
            fileName = "turkish_wordnet.xml"
        elif exceptionFileName is None:
            exceptionFileName = "english_exception.xml"
            self.readExceptionFile(exceptionFileName)
        self.__interlingualList = {}
        self.__exceptionList = {}
        self.__synSetList = OrderedDict()
        self.__literalList = OrderedDict()
        root = xml.etree.ElementTree.parse(fileName).getroot()
        currentSynSet = None
        for synSetNode in root:
            for partNode in synSetNode:
                if partNode.tag == "ID":
                    currentSynSet = SynSet(partNode.text)
                    self.addSynSet(currentSynSet)
                elif partNode.tag == "DEF":
                    currentSynSet.setDefinition(partNode.text)
                elif partNode.tag == "EXAMPLE":
                    currentSynSet.setExample(partNode.text)
                elif partNode.tag == "BCS":
                    currentSynSet.setBcs(int(partNode.text))
                elif partNode.tag == "POS":
                    if partNode.text == "a":
                        currentSynSet.setPos(Pos.ADJECTIVE)
                    elif partNode.text == "v":
                        currentSynSet.setPos(Pos.VERB)
                    elif partNode.text == "b":
                        currentSynSet.setPos(Pos.ADVERB)
                    elif partNode.text == "n":
                        currentSynSet.setPos(Pos.NOUN)
                    elif partNode.text == "i":
                        currentSynSet.setPos(Pos.INTERJECTION)
                    elif partNode.text == "c":
                        currentSynSet.setPos(Pos.CONJUNCTION)
                    elif partNode.text == "p":
                        currentSynSet.setPos(Pos.PREPOSITION)
                    elif partNode.text == "r":
                        currentSynSet.setPos(Pos.PRONOUN)
                elif partNode.tag == "SR":
                    if len(partNode) > 0 and partNode[0].tag == "TYPE":
                        typeNode = partNode[0]
                        if len(partNode) > 1 and partNode[1].tag == "TO":
                            toNode = partNode[1]
                            currentSynSet.addRelation(SemanticRelation(partNode.text, typeNode.text, int(toNode.text)))
                        else:
                            currentSynSet.addRelation(SemanticRelation(partNode.text, typeNode.text))
                elif partNode.tag == "ILR":
                    if len(partNode) > 0 and partNode[0].tag == "TYPE":
                        typeNode = partNode[0]
                        interlingualId = partNode.text
                        if interlingualId in self.__interlingualList:
                            synSetList = self.__interlingualList[interlingualId]
                        else:
                            synSetList = []
                        synSetList.append(currentSynSet)
                        self.__interlingualList[interlingualId] = synSetList
                        currentSynSet.addRelation(InterlingualRelation(interlingualId, typeNode.text))
                elif partNode.tag == "SYNONYM":
                    for literalNode in partNode:
                        currentLiteral = None
                        for childNode in literalNode:
                            if childNode.tag == "SENSE":
                                currentLiteral = Literal(literalNode.text, int(childNode.text), currentSynSet.getId())
                                currentSynSet.addLiteral(currentLiteral)
                                self.addLiteralToLiteralList(currentLiteral)
                            elif childNode.tag == "SR":
                                typeNode = childNode[0]
                                if len(childNode) > 1 and childNode[1].tag == "TO":
                                    toNode = childNode[1]
                                    currentLiteral.addRelation(
                                        SemanticRelation(childNode.text, typeNode.text, int(toNode.text)))
                                else:
                                    currentLiteral.addRelation(SemanticRelation(childNode.text, typeNode.text))

    """
    Method constructs a DOM parser using the dtd/xml schema parser configuration and using this parser it
    reads exceptions from file and puts to exceptionList HashMap.

    PARAMETERS
    ----------
    exceptionFileName : str
        Exception file to be read
    """

    def readExceptionFile(self, exceptionFileName: str):
        root = xml.etree.ElementTree.parse(exceptionFileName).getroot()
        for wordNode in root:
            wordName = wordNode.attrib["name"]
            rootForm = wordNode.attrib["root"]
            if wordNode.attrib["pos"] == "Adj":
                pos = Pos.ADJECTIVE
            elif wordNode.attrib["pos"] == "Adv":
                pos = Pos.ADVERB
            elif wordNode.attrib["pos"] == "Noun":
                pos = Pos.NOUN
            elif wordNode.attrib["pos"] == "Verb":
                pos = Pos.VERB
            else:
                pos = Pos.NOUN
            self.__exceptionList[wordName] = ExceptionalWord(wordName, rootForm, pos)

    """
    Adds a specified literal to the literal list.

    PARAMETERS
    ----------
    literal : Literal
        literal to be added
    """

    def addLiteralToLiteralList(self, literal: Literal):
        if literal.getName() in self.__literalList:
            literals = self.__literalList[literal.getName()]
        else:
            literals = []
        literals.append(literal)
        self.__literalList[literal.getName()] = literals

    """
    Returns the values of the SynSet list.

    RETURNS
    -------
    list
        Values of the SynSet list
    """

    def synSetList(self) -> list:
        return list(self.__synSetList.values())

    """
    Returns the keys of the literal list.

    RETURNS
    -------
    list
        Keys of the literal list
    """

    def literalList(self) -> list:
        return list(self.__literalList.keys())

    """
    Adds specified SynSet to the SynSet list.

    PARAMETERS
    ----------
    synSet : SynSet
        SynSet to be added
    """

    def addSynSet(self, synSet: SynSet):
        self.__synSetList[synSet.getId()] = synSet

    """
    Removes specified SynSet from the SynSet list.

    PARAMETERS
    ----------
    synSet : SynSet
        SynSet to be removed
    """

    def removeSynSet(self, synSet: SynSet):
        self.__synSetList.pop(synSet.getId())

    """
    Changes ID of a specified SynSet with the specified new ID.

    PARAMETERS
    ----------
    synSet : SynSet
        SynSet whose ID will be updated
    newId : str 
        new ID
    """

    def changeSynSetId(self, synSet: SynSet, newId: str):
        self.__synSetList.pop(synSet.getId())
        synSet.setId(newId)
        self.__synSetList[newId] = synSet

    """
    Returns SynSet with the specified SynSet ID.

    PARAMETERS
    ----------
    synSetId : str
        ID of the SynSet to be returned
        
    RETURNS
    -------
    SynSet
        SynSet with the specified SynSet ID
    """

    def getSynSetWithId(self, synSetId: str) -> SynSet:
        if synSetId in self.__synSetList:
            return self.__synSetList[synSetId]
        else:
            return None

    """
    Returns SynSet with the specified literal and sense index.

    PARAMETERS
    ----------
    literal : Literal
        SynSet literal
    sense : int  
        SynSet's corresponding sense index
        
    RETURNS
    -------
    SynSet
        SynSet with the specified literal and sense index
    """

    def getSynSetWithLiteral(self, literal: str, sense: int) -> SynSet:
        if literal in self.__literalList:
            literals = self.__literalList[literal]
            for current in literals:
                if current.getSense() == sense:
                    return self.getSynSetWithId(current.getSynSetId())
        return None

    """
    Returns the number of SynSets with a specified literal.

    PARAMETERS
    ----------
    literal : Literal
        literal to be searched in SynSets
        
    RETURNS
    -------
    int
        The number of SynSets with a specified literal
    """

    def numberOfSynSetsWithLiteral(self, literal: str) -> int:
        if literal in self.__literalList:
            return len(self.__literalList[literal])
        else:
            return 0

    """
    Returns a list of SynSets with a specified part of speech tag.

    PARAMETERS
    ----------
    pos : Pos
        Part of speech tag to be searched in SynSets
        
    RETURNS
    -------
    list
        A list of SynSets with a specified part of speech tag
    """

    def getSynSetsWithPartOfSpeech(self, pos: Pos) -> list:
        result = []
        for synSet in self.__synSetList.values():
            if synSet.getPos() is not None and synSet.getPos() == pos:
                result.append(synSet)
        return result

    """
    Returns a list of literals with a specified literal String.

    PARAMETERS
    ----------
    literal : Literal
        literal String to be searched in literal list
        
    RETURNS
    -------
    list
        A list of literals with a specified literal String
    """

    def getLiteralsWithName(self, literal: str) -> list:
        if literal in self.__literalList:
            return self.__literalList[literal]
        else:
            return []

    """
    Finds the SynSet with specified literal String and part of speech tag and adds to the given SynSet list.

    PARAMETERS
    ----------
    result : list 
        SynSet list to add the specified SynSet
    literal : str
        literal String to be searched in literal list
    pos : Pos    
        part of speech tag to be searched in SynSets
    """

    def addSynSetsWithLiteralToList(self, result: list, literal: str, pos: Pos):
        for current in self.__literalList[literal]:
            synSet = self.getSynSetWithId(current.getSynSetId)
            if synSet is not None and synSet.getPos() == pos:
                result.append(synSet)

    """
    Finds SynSets with specified literal String and adds to the newly created SynSet list.

    PARAMETERS
    ----------
    literal : Literal
        literal String to be searched in literal list
        
    RETURNS
    -------
    list
        Returns a list of SynSets with specified literal String
    """

    def getSynSetsWithLiteral(self, literal: str) -> list:
        result = []
        if literal in self.__literalList:
            for current in self.__literalList[literal]:
                synSet = self.getSynSetWithId(current.getSynSetId())
                if synSet is not None:
                    result.append(synSet)
        return result

    """
    Finds literals with specified literal String and adds to the newly created literal String list. Ex: cleanest - clean

    PARAMETERS
    ----------
    literal : Literal
        literal String to be searched in literal list
        
    RETURNS
    -------
    list
        Returns a list of literals with specified literal String
    """

    def getLiteralsWithPossibleModifiedLiteral(self, literal: str) -> list:
        result = [literal]
        wordWithoutLastOne = literal[:len(literal) - 1]
        wordWithoutLastTwo = literal[:len(literal) - 2]
        wordWithoutLastThree = literal[:len(literal) - 3]
        if literal in self.__exceptionList and self.__exceptionList[literal].getRoot() in self.__literalList:
            result.append(self.__exceptionList[literal].getRoot())
        if literal.endswith("s") and wordWithoutLastOne in self.__literalList:
            result.append(wordWithoutLastOne)
        if (literal.endswith("es") or literal.endswith("ed") or literal.endswith("er")) \
                and wordWithoutLastTwo in self.__literalList:
            result.append(wordWithoutLastTwo)
        if literal.endswith("ed") and (wordWithoutLastTwo + literal[len(literal) - 3]) in self.__literalList:
            result.append(wordWithoutLastTwo + literal[len(literal) - 3])
        if (literal.endswith("ed") or literal.endswith("er")) and (wordWithoutLastTwo + "e") in self.__literalList:
            result.append(wordWithoutLastTwo + "e")
        if (literal.endswith("ing") or literal.endswith("est")) and wordWithoutLastThree in self.__literalList:
            result.append(wordWithoutLastThree)
        if literal.endswith("ing") and (wordWithoutLastThree + literal[len(literal) - 4]) in self.__literalList:
            result.append(wordWithoutLastThree + literal[len(literal) - 4])
        if (literal.endswith("ing") or literal.endswith("est")) and (wordWithoutLastThree + "e") in self.__literalList:
            result.append(wordWithoutLastThree + "e")
        if literal.endswith("ies") and (wordWithoutLastThree + "y") in self.__literalList:
            result.append(wordWithoutLastThree + "y")
        return result

    """
    Finds SynSets with specified literal String and part of speech tag, then adds to the newly created SynSet list. 
    Ex: cleanest - clean

    PARAMETERS
    ----------
    literal : str
        Literal String to be searched in literal list
    pos : Pos    
        part of speech tag to be searched in SynSets
        
    RETURNS
    -------
    list
        Returns a list of SynSets with specified literal String and part of speech tag
    """

    def getSynSetsWithPossiblyModifiedLiteral(self, literal: str, pos: Pos) -> list:
        result = []
        modifiedLiterals = self.getLiteralsWithPossibleModifiedLiteral(literal)
        for modifiedLiteral in modifiedLiterals:
            if modifiedLiteral in self.__literalList:
                self.addSynSetsWithLiteralToList(result, modifiedLiteral, pos)
        return result

    """
    Adds the reverse relations to the SynSet.

    PARAMETERS
    ----------
    synSet : SynSet          
        SynSet to add the reverse relations
    semanticRelation : SemanticRelation
        relation whose reverse will be added
    """

    def addReverseRelation(self, synSet: SynSet, semanticRelation: SemanticRelation):
        otherSynSet = self.getSynSetWithId(semanticRelation.getName())
        if otherSynSet is not None and SemanticRelation.reverse(semanticRelation.getRelationType()) is not None:
            otherRelation = SemanticRelation(synSet.getId(),
                                             SemanticRelation.reverse(semanticRelation.getRelationType()))
            if not otherSynSet.containsRelation(otherRelation):
                otherSynSet.addRelation(otherRelation)

    """
    Removes the reverse relations from the SynSet.

    PARAMETERS
    ----------
    synSet : SynSet          
        SynSet to remove the reverse relation
    semanticRelation : SemanticRelation
        relation whose reverse will be removed
    """

    def removeReverseRelation(self, synSet: SynSet, semanticRelation: SemanticRelation):
        otherSynSet = self.getSynSetWithId(semanticRelation.getName())
        if otherSynSet is not None and SemanticRelation.reverse(semanticRelation.getRelationType()) is not None:
            otherRelation = SemanticRelation(synSet.getId(),
                                             SemanticRelation.reverse(semanticRelation.getRelationType()))
            if otherSynSet.containsRelation(otherRelation):
                otherSynSet.removeRelation(otherRelation)

    """
    Loops through the SynSet list and adds the possible reverse relations.
    """

    def equalizeSemanticRelations(self):
        for synSet in self.__synSetList.values():
            for i in range(synSet.relationSize()):
                if isinstance(synSet.getRelation(i), SemanticRelation):
                    self.addReverseRelation(synSet, synSet.getRelation(i))

    """
    Creates a list of literals with a specified word, or possible words corresponding to morphological parse.

    PARAMETERS
    ----------
    word : str     
        literal String
    parse : MorphologicalParse    
        morphological parse to get possible words
    metaParse : MetamorphicParse
        metamorphic parse to get possible words
    fsm : FsmMorphologicalAnalyzer      
        finite state machine morphological analyzer to be used at getting possible words

    RETURNS
    -------
    list
        A list of literal
    """

    def constructLiterals(self, word: str, parse: MorphologicalParse, metaParse: MetamorphicParse,
                          fsm: FsmMorphologicalAnalyzer):
        result = []
        if parse.size() > 0:
            if not parse.isPunctuation() and not parse.isCardinal() and not parse.isReal():
                possibleWords = fsm.getPossibleWords(parse, metaParse)
                for possibleWord in possibleWords:
                    result.extend(self.getLiteralsWithName(possibleWord))
            else:
                result.extend(self.getLiteralsWithName(word))
        else:
            result.extend(self.getLiteralsWithName(word))
        return result

    """
    Creates a list of SynSets with a specified word, or possible words corresponding to morphological parse.

    PARAMETERS
    ----------
    word : str     
        literal String  to get SynSets with
    parse : MorphologicalParse    
        morphological parse to get SynSets with proper literals
    metaParse : MetamorphicParse
        metamorphic parse to get possible words
    fsm : FsmMorphologicalAnalyzer      
        finite state machine morphological analyzer to be used at getting possible words

    RETURNS
    -------
    list
        A list of SynSets
    """

    def constructSynSets(self, word: str, parse: MorphologicalParse, metaParse: MetamorphicParse,
                         fsm: FsmMorphologicalAnalyzer) -> list:
        result = []
        if parse.size() > 0:
            if parse.isProperNoun():
                result.append(self.getSynSetWithLiteral("(özel isim)", 1))
            if parse.isTime():
                result.append(self.getSynSetWithLiteral("(zaman)", 1))
            if parse.isDate():
                result.append(self.getSynSetWithLiteral("(tarih)", 1))
            if parse.isHashTag():
                result.append(self.getSynSetWithLiteral("(hashtag)", 1))
            if parse.isEmail():
                result.append(self.getSynSetWithLiteral("(email)", 1))
            if parse.isOrdinal():
                result.append(self.getSynSetWithLiteral("(sayı sıra sıfatı)", 1))
            if parse.isPercent():
                result.append(self.getSynSetWithLiteral("(yüzde)", 1))
            if parse.isFraction():
                result.append(self.getSynSetWithLiteral("(kesir sayı)", 1))
            if parse.isRange():
                result.append(self.getSynSetWithLiteral("(sayı aralığı)", 1))
            if parse.isReal():
                result.append(self.getSynSetWithLiteral("(reel sayı)", 1))
            if not parse.isPunctuation() and not parse.isCardinal() and not parse.isReal():
                possibleWords = fsm.getPossibleWords(parse, metaParse)
                for possibleWord in possibleWords:
                    synSets = self.getSynSetsWithLiteral(possibleWord)
                    if len(synSets) > 0:
                        for synSet in synSets:
                            if synSet.getPos() is not None and (parse.getPos() == "NOUN" or parse.getPos() == "ADVERB"
                                                                or parse.getPos() == "VERB" or parse.getPos() == "ADJ"
                                                                or parse.getPos() == "CONJ"):
                                if synSet.getPos() == Pos.NOUN:
                                    if parse.getPos() == "NOUN" or parse.getRootPos() == "NOUN":
                                        result.append(synSet)
                                elif synSet.getPos() == Pos.ADVERB:
                                    if parse.getPos() == "ADVERB" or parse.getRootPos() == "ADVERB":
                                        result.append(synSet)
                                elif synSet.getPos() == Pos.VERB:
                                    if parse.getPos() == "VERB" or parse.getRootPos() == "VERB":
                                        result.append(synSet)
                                elif synSet.getPos() == Pos.ADJECTIVE:
                                    if parse.getPos() == "ADJ" or parse.getRootPos() == "ADJ":
                                        result.append(synSet)
                                elif synSet.getPos() == Pos.CONJUNCTION:
                                    if parse.getPos() == "CONJ" or parse.getRootPos() == "CONJ":
                                        result.append(synSet)
                                else:
                                    result.append(synSet)
                            else:
                                result.append(synSet)
                if len(result) == 0:
                    for possibleWord in possibleWords:
                        synSets = self.getSynSetsWithLiteral(possibleWord)
                        result.extend(synSets)
            else:
                result.extend(self.getSynSetsWithLiteral(word))
            if parse.isCardinal() and len(result) == 0:
                result.append(self.getSynSetWithLiteral("(tam sayı)", 1))
        else:
            result.extend(self.getSynSetsWithLiteral(word))
        return result

    """
    Returns a list of literals using 3 possible words gathered with the specified morphological parses and metamorphic 
    parses.

    PARAMETERS
    ----------
    morphologicalParse1 : MorphologicalParse
        morphological parse to get possible words
    morphologicalParse2 : MorphologicalParse
        morphological parse to get possible words
    morphologicalParse3 : MorphologicalParse 
        morphological parse to get possible words
    metaParse1 : MetamorphicParse         
        metamorphic parse to get possible words
    metaParse2 : MetamorphicParse          
        metamorphic parse to get possible words
    metaParse3 : MetamorphicParse          
        metamorphic parse to get possible words
    fsm : FsmMorphologicalAnalyzer                
        finite state machine morphological analyzer to be used at getting possible words
    
    RETURNS
    -------
    list
        A list of literals
    """

    def constructIdiomLiterals(self, fsm: FsmMorphologicalAnalyzer, morphologicalParse1: MorphologicalParse,
                               metaParse1: MetamorphicParse, morphologicalParse2: MorphologicalParse,
                               metaParse2: MetamorphicParse, morphologicalParse3: MorphologicalParse = None,
                               metaParse3: MetamorphicParse = None) -> list:
        result = []
        possibleWords1 = fsm.getPossibleWords(morphologicalParse1, metaParse1)
        possibleWords2 = fsm.getPossibleWords(morphologicalParse2, metaParse2)
        if morphologicalParse3 is not None and metaParse3 is not None:
            possibleWords3 = fsm.getPossibleWords(morphologicalParse3, metaParse3)
            for possibleWord1 in possibleWords1:
                for possibleWord2 in possibleWords2:
                    for possibleWord3 in possibleWords3:
                        result.extend(self.getLiteralsWithName(possibleWord1 + " " + possibleWord2 +
                                                               " " + possibleWord3))
        else:
            for possibleWord1 in possibleWords1:
                for possibleWord2 in possibleWords2:
                    result.extend(self.getLiteralsWithName(possibleWord1 + " " + possibleWord2))
        return result

    """
    Returns a list of SynSets using 3 possible words gathered with the specified morphological parses and metamorphic 
    parses.

    PARAMETERS
    ----------
    morphologicalParse1 : MorphologicalParse
        morphological parse to get possible words
    morphologicalParse2 : MorphologicalParse
        morphological parse to get possible words
    morphologicalParse3 : MorphologicalParse 
        morphological parse to get possible words
    metaParse1 : MetamorphicParse         
        metamorphic parse to get possible words
    metaParse2 : MetamorphicParse          
        metamorphic parse to get possible words
    metaParse3 : MetamorphicParse          
        metamorphic parse to get possible words
    fsm : FsmMorphologicalAnalyzer                
        finite state machine morphological analyzer to be used at getting possible words

    RETURNS
    -------
    list
        A list of SynSets
    """

    def constructIdiomSynSets(self, fsm: FsmMorphologicalAnalyzer, morphologicalParse1: MorphologicalParse,
                              metaParse1: MetamorphicParse, morphologicalParse2: MorphologicalParse,
                              metaParse2: MetamorphicParse, morphologicalParse3: MorphologicalParse = None,
                              metaParse3: MetamorphicParse = None) -> list:
        result = []
        possibleWords1 = fsm.getPossibleWords(morphologicalParse1, metaParse1)
        possibleWords2 = fsm.getPossibleWords(morphologicalParse2, metaParse2)
        if morphologicalParse3 is not None and metaParse3 is not None:
            possibleWords3 = fsm.getPossibleWords(morphologicalParse3, metaParse3)
            for possibleWord1 in possibleWords1:
                for possibleWord2 in possibleWords2:
                    for possibleWord3 in possibleWords3:
                        if self.numberOfSynSetsWithLiteral(possibleWord1 + " " + possibleWord2 + " "
                                                           + possibleWord3) > 0:
                            result.extend(self.getSynSetsWithLiteral(possibleWord1 + " " + possibleWord2 +
                                                                     " " + possibleWord3))
        else:
            for possibleWord1 in possibleWords1:
                for possibleWord2 in possibleWords2:
                    if self.numberOfSynSetsWithLiteral(possibleWord1 + " " + possibleWord2) > 0:
                        result.extend(self.getSynSetsWithLiteral(possibleWord1 + " " + possibleWord2))
        return result

    """
    Sorts definitions of SynSets in SynSet list according to their lengths.
    """

    def sortDefinitions(self):
        for synSet in self.__synSetList:
            synSet.sortDefinitions()

    """
    Returns a list of SynSets with the interlingual relations of a specified SynSet ID.

    PARAMETERS
    ----------
    synSetId : str
        SynSet ID to be searched
        
    RETURNS
    -------
    list
        A list of SynSets with the interlingual relations of a specified SynSet ID
    """

    def getInterlingual(self, synSetId: str) -> list:
        if synSetId in self.__interlingualList:
            return self.__interlingualList[synSetId]
        else:
            return []

    def containsSameLiteral(self, synSet1: SynSet, synSet2: SynSet) -> bool:
        for i in range(synSet1.getSynonym().literalSize()):
            literal1 = synSet1.getSynonym().getLiteral(i)
            for j in range(i + 1, synSet2.getSynonym().literalSize()):
                literal2 = synSet2.getSynonym().getLiteral(j)
                if literal1.getName() == literal2.getName() and synSet1.getPos() is not None:
                    return True
        return False

    """
    Prints the SynSets without part of speech tags.
    """
    def noPosCheck(self):
        for synSet in self.synSetList():
            if synSet.getPos() is None:
                print(synSet.getId() + "\t" + synSet.getSynonym().getLiteral(0).getName() + "\t" +
                      synSet.getDefinition() + "\t" + "has no part of speech")

    """
    Prints the SynSets without definitions.
    """
    def noDefinitionCheck(self):
        for synSet in self.synSetList():
            if synSet.getDefinition() is None:
                print("SynSet " + synSet.getId() + " has no definition " + synSet.getSynonym().__str__())

    """
    Print the literals with same senses.
    """
    def sameLiteralSameSenseCheck(self):
        for name in self.__literalList.keys():
            literals = self.__literalList[name]
            for i in range(len(literals)):
                for j in range(i + 1, len(literals)):
                    if literals[i].getSense() == literals[j].getSense():
                        print("Literal " + name + " has same senses.")

    """
    Prints the literals with same SynSets.
    """
    def sameLiteralSameSynSetCheck(self):
        for synSet in self.synSetList():
            if self.containsSameLiteral(synSet, synSet):
                print(synSet.getPos().__str__() + "->" + synSet.getSynonym().__str__() + "->" + synSet.getDefinition())

    """
    Prints SynSets without relation IDs.
    """
    def semanticRelationNoIDCheck(self):
        for synSet in self.synSetList():
            j = 0
            while j < synSet.relationSize():
                relation = synSet.getRelation(j)
                if isinstance(relation, SemanticRelation) and self.getSynSetWithId(relation.getName()) is None:
                    synSet.removeRelation(relation)
                    j = j - 1
                    print("Relation " + relation.getName() + " of Synset " + synSet.getId() + " does not exists "
                          + synSet.getSynonym().__str__())
                j = j + 1

    """
    Prints SynSets with same relations.
    """
    def sameSemanticRelationCheck(self):
        for synSet in self.synSetList():
            j = 0
            while j < synSet.relationSize():
                relation = synSet.getRelation(j)
                same = None
                for k in range(j + 1, synSet.relationSize()):
                    if relation.getName() == synSet.getRelation(k).getName():
                        print(relation.getName() + "--" + synSet.getRelation(k).getName()
                              + " are same relation for synset " + synSet.getId())
                        same = synSet.getRelation(k)
                if same is not None:
                    synSet.removeRelation(same)
                else:
                    j = j + 1

    """
    Performs check processes.
    """
    def check(self):
        self.noPosCheck()
        self.noDefinitionCheck()
        self.sameSemanticRelationCheck()
        self.semanticRelationNoIDCheck()
        self.sameLiteralSameSynSetCheck()
        self.sameLiteralSameSenseCheck()

    """
    Method to write SynSets to the specified file in the XML format.

    PARAMETERS
    ----------
    fileName : str
        file name to write XML files
    """

    def saveAsXml(self, fileName: str):
        outFile = open(fileName, "w")
        outFile.write("<SYNSETS>\n")
        for synSet in self.__synSetList.values():
            synSet.saveAsXml(outFile)
        outFile.write("</SYNSETS>\n")
        outFile.close()

    """
    Returns the size of the SynSet list.

    RETURNS
    -------
    int
        The size of the SynSet list
    """

    def size(self) -> int:
        return len(self.__synSetList)

    """
    Conduct common operations between similarity metrics.

    PARAMETERS
    ----------
    pathToRootOfSynSet1 : list
        First list of Strings
    pathToRootOfSynSet2 : list
        Second list of Strings
        
    RETURNS
    -------
    int
        Path length
    """

    def findPathLength(self, pathToRootOfSynSet1: list, pathToRootOfSynSet2: list) -> int:
        for i in range(len(pathToRootOfSynSet1)):
            foundIndex = pathToRootOfSynSet2.index(pathToRootOfSynSet1[i])
            if foundIndex != -1:
                return i + foundIndex - 1
        return -1

    """
    Returns depth and ID of the LCS.

    PARAMETERS
    ----------
    pathToRootOfSynSet1 : list
        First list of Strings
    pathToRootOfSynSet2 : list
        Second list of Strings

    RETURNS
    -------
    tuple
        Depth and ID of the LCS
    """

    def findLCS(self, pathToRootOfSynSet1: list, pathToRootOfSynSet2: list) -> tuple:
        for i in range(len(pathToRootOfSynSet1)):
            LCSid = pathToRootOfSynSet1[i]
            if LCSid in pathToRootOfSynSet2:
                return LCSid, len(pathToRootOfSynSet1) - i + 1
        return None

    """
    Returns the depth of path.

    PARAMETERS
    ----------
    pathToRootOfSynSet1 : list
        First list of Strings
    pathToRootOfSynSet2 : list
        Second list of Strings

    RETURNS
    -------
    int
        LCS depth
    """

    def findLCSDepth(self, pathToRootOfSynSet1: list, pathToRootOfSynSet2: list) -> int:
        temp = self.findLCS(pathToRootOfSynSet1, pathToRootOfSynSet2)
        if temp is not None:
            return temp[1]
        else:
            return -1

    """
    Returns the ID of LCS of path.

    PARAMETERS
    ----------
    pathToRootOfSynSet1 : list
        First list of Strings
    pathToRootOfSynSet2 : list
        Second list of Strings

    RETURNS
    -------
    str
        LCS ID
    """

    def findLCSid(self, pathToRootOfSynSet1: list, pathToRootOfSynSet2: list) -> str:
        temp = self.findLCS(pathToRootOfSynSet1, pathToRootOfSynSet2)
        if temp is not None:
            return temp[0]
        else:
            return None

    """
    Finds the parent of a node. It does not move until the root, instead it goes one level up.

    PARAMETERS
    ----------
    root : SynSet
        SynSet whose parent will be find
        
    RETURNS
    -------
    SynSet
        Parent SynSet
    """

    def percolateUp(self, root: SynSet) -> SynSet:
        for i in range(root.relationSize()):
            r = root.getRelation(i)
            if isinstance(r, SemanticRelation):
                if r.getRelationType() == SemanticRelationType.HYPERNYM \
                        or r.getRelationType() == SemanticRelationType.INSTANCE_HYPERNYM:
                    root = self.getSynSetWithId(r.getName())
                    return root
        return None

    """
    Finds the path to the root node of a SynSets.

    PARAMETERS
    ----------
    synSet : SynSet
        SynSet whose root path will be found
        
    RETURNS
    -------
    list
        List of String corresponding to nodes in the path
    """

    def findPathToRoot(self, synSet: SynSet) -> list:
        pathToRoot = []
        while synSet is not None:
            if synSet.getId() in pathToRoot:
                break
            pathToRoot.append(synSet.getId())
            synSet = self.percolateUp(synSet)
        return pathToRoot
