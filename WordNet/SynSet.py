from __future__ import annotations
from Dictionary.Pos import Pos

from WordNet.InterlingualDependencyType import InterlingualDependencyType
from WordNet.InterlingualRelation import InterlingualRelation
from WordNet.Literal import Literal
from WordNet.Relation import Relation
from WordNet.SemanticRelation import SemanticRelation
from WordNet.SemanticRelationType import SemanticRelationType
from WordNet.Synonym import Synonym


class SynSet:

    __id: str
    __pos: Pos
    __definition: list
    __example: str
    __synonym: Synonym
    __relations: list
    __note: str
    __wikiPage: str
    __bcs: int

    def __init__(self, _id: str):
        """
        Constructor initialize SynSet ID, synonym and relations list.

        PARAMETERS
        ----------
        _id : str
            SynSet ID
        """
        self.__id = _id
        self.__synonym = Synonym()
        self.__relations = []
        self.__definition = []
        self.__pos = None
        self.__example = None
        self.__wikiPage = None

    def __eq__(self, other) -> bool:
        """
        An overridden equals method to compare two SynSets.

        PARAMETERS
        ----------
        other
            The reference object with which to compare

        RETURNS
        -------
        bool
            True if this object's ID is the same as the obj argument's ID; False otherwise.
        """
        return self.__id == other.__id

    def __hash__(self):
        """
        Returns a hash code for the ID.

        RETURNS
        -------
        int
            A hash code for the ID
        """
        return hash(self.__id)

    def getId(self) -> str:
        """
        Accessor for the SynSet ID.

        RETURNS
        -------
        str
            SynSet ID
        """
        return self.__id

    def setId(self, _id: str):
        """
        Mutator method for the SynSet ID.

        PARAMETERS
        ----------
        _id : str
            SynSet ID to be set
        """
        self.__id = _id
        for i in range(self.__synonym.literalSize()):
            self.__synonym.getLiteral(i).setSynSetId(_id)

    def setDefinition(self, definition: str):
        """
        Mutator method for the definition.

        PARAMETERS
        ----------
        definition : str
            String definition
        """
        if definition is not None:
            self.__definition = definition.split("|")

    def removeDefinition(self, definition: str):
        """
        Removes the specified definition from long definition.

        PARAMETERS
        ----------
        definition : str
            definition to be removed
        """
        longDefinition = self.getLongDefinition()
        if longDefinition.startswith(definition + "|"):
            self.setDefinition(longDefinition.replace(definition + "|", ""))
        elif longDefinition.endswith("|" + definition):
            self.setDefinition(longDefinition.replace("|" + definition, ""))
        elif ("|" + definition + "|") in longDefinition:
            self.setDefinition(longDefinition.replace("|" + definition, ""))

    def getDefinition(self, index=None) -> str:
        """
        Accessor for the definition.

        RETURNS
        -------
        str
            Definition
        """
        if len(self.__definition) > 0:
            if index is None:
                index = 0
            if 0 <= index < len(self.__definition):
                return self.__definition[index]
            else:
                return None
        else:
            return None

    def representative(self) -> str:
        """
        Returns the first literal's name.

        RETURNS
        -------
        str
            The first literal's name.
        """
        return self.getSynonym().getLiteral(0).getName()

    def getLongDefinition(self) -> str:
        """
        Returns all the definitions in the list.

        RETURNS
        -------
        str
            All the definitions
        """
        if len(self.__definition) > 0:
            longDefinition = self.__definition[0]
            for i in range(1, len(self.__definition)):
                longDefinition = longDefinition + "|" + self.__definition[i]
            return longDefinition
        else:
            return None

    def sortDefinitions(self):
        """
        Sorts definitions list according to their lengths.
        """
        if len(self.__definition) > 0:
            for i in range(len(self.__definition)):
                for j in range(i + 1, len(self.__definition)):
                    if len(self.__definition[i]) < len(self.__definition[j]):
                        tmp = self.__definition[i]
                        self.__definition[i] = self.__definition[j]
                        self.__definition[j] = tmp

    def numberOfDefinitions(self) -> int:
        """
        Returns number of definitions in the list.

        RETURNS
        -------
        int
            Number of definitions in the list.
        """
        return len(self.__definition)

    def setExample(self, example: str):
        """
        Mutator for the example.

        PARAMETERS
        ----------
        example : str
            String that will be used to set
        """
        self.__example = example

    def getExample(self) -> str:
        """
        Accessor for the example.

        RETURNS
        -------
        str
            String example
        """
        return self.__example

    def setBcs(self, bcs: int):
        """
        Mutator for the bcs value which enables the connection with the BalkaNet.

        PARAMETERS
        ----------
        bcs : int
            bcs value
        """
        if 1 <= bcs <= 3:
            self.__bcs = bcs

    def getBcs(self) -> int:
        """
        Accessor for the bcs value

        RETURNS
        -------
        int
            Bcs value
        """
        return self.__bcs

    def setPos(self, pos: Pos):
        """
        Mutator for the part of speech tags.

        PARAMETERS
        ----------
        pos : Pos
            part of speech tag
        """
        self.__pos = pos

    def getPos(self) -> Pos:
        """
        Accessor for the part of speech tag.

        RETURNS
        -------
        Pos
            Part of speech tag
        """
        return self.__pos

    def setNote(self, note: str):
        """
        Mutator for the available notes.

        PARAMETERS
        ----------
        note : str
            String note to be set
        """
        self.__note = note

    def getNote(self) -> str:
        """
        Accessor for the available notes.

        RETURNS
        -------
        str
            String note
        """
        return self.__note

    def setWikiPage(self, wikiPage: str):
        """
        Mutator for the wiki page.

        PARAMETERS
        ----------
        wikiPage : str
            String Wiki page to be set
        """
        self.__wikiPage = wikiPage

    def getWikiPage(self) -> str:
        """
        Accessor for the wiki pages.

        RETURNS
        -------
        str
            String wiki page
        """
        return self.__wikiPage

    def addRelation(self, relation: Relation):
        """
        Appends the specified Relation to the end of relations list.

        PARAMETERS
        ----------
        relation : Relation
            Element to be appended to the list
        """
        self.__relations.append(relation)

    def removeRelation(self, relationOrName):
        """
        Removes the first occurrence of the specified element from relations list according to relation name,
        if it is present. If the list does not contain the element, it stays unchanged.

        PARAMETERS
        ----------
        relationOrName
            Element to be removed from the list, if present
            element to be removed from the list, if present
        """
        if isinstance(relationOrName, Relation):
            self.__relations.remove(relationOrName)
        elif isinstance(relationOrName, str):
            for i in range(len(self.__relations)):
                if self.__relations[i].getName() == relationOrName:
                    self.__relations.pop(i)
                    break

    def getRelation(self, index: int) -> Relation:
        """
        Returns the element at the specified position in relations list.

        PARAMETERS
        ----------
        index : int
            index of the element to return

        RETURNS
        -------
        Relation
            The element at the specified position in the list
        """
        return self.__relations[index]

    def getInterlingual(self) -> list:
        """
        Returns interlingual relations with the synonym interlingual dependencies.

        RETURNS
        -------
        list
            A list of SynSets that has interlingual relations in it
        """
        result = []
        for i in range(len(self.__relations)):
            if isinstance(self.__relations[i], InterlingualRelation):
                relation = self.__relations[i]
                if relation.getType() == InterlingualDependencyType.SYNONYM:
                    result.append(relation.getName())
        return result

    def relationSize(self) -> int:
        """
        Returns the size of the relations list.

        RETURNS
        -------
        int
            The size of the relations list
        """
        return len(self.__relations)

    def addLiteral(self, literal: Literal):
        """
        Adds a specified literal to the synonym.

        PARAMETERS
        ----------
        literal : Literal
            literal to be added
        """
        self.__synonym.addLiteral(literal)

    def getSynonym(self) -> Synonym:
        """
        Accessor for the synonym.

        RETURNS
        -------
        Synonym
            synonym
        """
        return self.__synonym

    def containsSameLiteral(self, synSet: SynSet) -> bool:
        """
        Compares literals of synonym and the specified SynSet, returns true if their have same literals.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet to compare

        RETURNS
        -------
        bool
            True if SynSets have same literals, False otherwise
        """
        for i in range(self.__synonym.literalSize()):
            literal1 = self.__synonym.getLiteral(i).getName()
            for j in range(synSet.getSynonym().literalSize()):
                literal2 = synSet.getSynonym().getLiteral(j).getName()
                if literal1 == literal2:
                    return True
        return False

    def containsRelation(self, relation: Relation) -> bool:
        """
        Returns True if relations list contains the specified relation.

        PARAMETERS
        ----------
        relation : Relation
            Element whose presence in the list is to be tested

        RETURNS
        -------
        bool
            True if the list contains the specified element
        """
        return relation in self.__relations

    def containsRelationType(self, semanticRelationType: SemanticRelationType) -> bool:
        """
        Returns True if specified semantic relation type presents in the relations list.

        PARAMETERS
        ----------
        semanticRelationType : SemanticRelationType
            Element whose presence in the list is to be tested

        RETURNS
        -------
        bool
            True if specified semantic relation type presents in the relations list
        """
        for relation in self.__relations:
            if isinstance(relation, SemanticRelation) and relation.getRelationType() == semanticRelationType:
                return True
        return False

    def mergeSynSet(self, synSet: SynSet):
        """
        Merges synonym and a specified SynSet with their definitions, relations, part of speech tags and examples.

        PARAMETERS
        ----------
        synSet : SynSet
            SynSet to be merged
        """
        for i in range(synSet.getSynonym().literalSize()):
            if not self.__synonym.contains(synSet.getSynonym().getLiteral(i)):
                self.__synonym.addLiteral(synSet.getSynonym().getLiteral(i))
        if len(self.__definition) == 0 and synSet.getDefinition() is not None:
            self.setDefinition(synSet.getDefinition())
        elif len(self.__definition) > 0 and synSet.getDefinition() is not None \
                and self.getLongDefinition() != synSet.getLongDefinition():
            self.setDefinition(self.getLongDefinition() + "|" + synSet.getLongDefinition())
        if synSet.relationSize() != 0:
            for i in range(0, synSet.relationSize()):
                if not self.containsRelation(synSet.getRelation(i)) and synSet.getRelation(i).getName() != id:
                    self.addRelation(synSet.getRelation(i))
        if self.__pos is None and synSet.getPos() is not None:
            self.setPos(synSet.getPos())
        if self.__example is None and synSet.getExample() is not None:
            self.__example = synSet.getExample()

    def __str__(self) -> str:
        """
        Overridden toString method to print the first definition or representative.

        RETURNS
        -------
        str
            Print the first definition or representative.
        """
        if len(self.__definition) > 0:
            return self.__definition[0]
        else:
            return self.representative()

    def saveAsXml(self, outFile):
        """
        Method to write SynSets to the specified file in the XML format.

        PARAMETERS
        ----------
        outFile : file
            File to write XML files
        """
        outFile.write("<SYNSET>")
        outFile.write("<ID>" + self.__id + "</ID>")
        self.__synonym.saveAsXml(outFile)
        if self.__pos is not None:
            if self.__pos == Pos.NOUN:
                outFile.write("<POS>n</POS>")
            elif self.__pos == Pos.ADJECTIVE:
                outFile.write("<POS>a</POS>")
            elif self.__pos == Pos.VERB:
                outFile.write("<POS>v</POS>")
            elif self.__pos == Pos.ADVERB:
                outFile.write("<POS>b</POS>")
            elif self.__pos == Pos.CONJUNCTION:
                outFile.write("<POS>c</POS>")
            elif self.__pos == Pos.PRONOUN:
                outFile.write("<POS>r</POS>")
            elif self.__pos == Pos.INTERJECTION:
                outFile.write("<POS>i</POS>")
            elif self.__pos == Pos.PREPOSITION:
                outFile.write("<POS>p</POS>")
        for relation in self.__relations:
            if isinstance(relation, InterlingualRelation):
                outFile.write("<ILR>" + relation.getName() + "<TYPE>" + relation.getTypeAsString() + "</TYPE></ILR>")
            elif isinstance(relation, SemanticRelation):
                outFile.write("<SR>" + relation.getName() + "<TYPE>" + relation.getTypeAsString() + "</TYPE></SR>")
        if self.__wikiPage is not None:
            outFile.write("<WIKI>" + self.__wikiPage + "</WIKI>")
        if len(self.__definition) > 0:
            outFile.write("<DEF>" + self.getLongDefinition() + "</DEF>")
        if self.__example is not None:
            outFile.write("<EXAMPLE>" + self.__example + "</EXAMPLE>")
        outFile.write("</SYNSET>\n")
