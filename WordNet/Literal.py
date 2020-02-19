from WordNet.InterlingualRelation import InterlingualRelation
from WordNet.Relation import Relation
from WordNet.SemanticRelation import SemanticRelation
from WordNet.SemanticRelationType import SemanticRelationType


class Literal:

    name: str
    sense: int
    synSetId: str
    origin: str
    relations: list

    def __init__(self, name: str, sense: int, synSetId: str):
        """
        A constructor that initializes name, sense, SynSet ID and the relations.

        PARAMETERS
        ----------
        name : str
            name of a literal
        sense : int
            index of sense
        synSetId : str
            ID of the SynSet
        """
        self.name = name
        self.sense = sense
        self.synSetId = synSetId
        self.relations = []
        self.origin = None

    def __eq__(self, other) -> bool:
        """
        Overridden equals method returns true if the specified object literal equals to the current literal's name.

        PARAMETERS
        ----------
        other : Literal
            Object literal to compare

        RETURNS
        -------
        bool
            True if the specified object literal equals to the current literal's name
        """
        return self.name == other.name and self.sense == other.sense

    def getSynSetId(self) -> str:
        """
        Accessor method to return SynSet ID.

        RETURNS
        -------
        str
            String of SynSet ID
        """
        return self.synSetId

    def getName(self) -> str:
        """
        Accessor method to return name of the literal.

        RETURNS
        -------
        str
            Name of the literal
        """
        return self.name

    def getSense(self) -> int:
        """
        Accessor method to return the index of sense of the literal.

        RETURNS
        -------
        int
            Index of sense of the literal
        """
        return self.sense

    def getOrigin(self) -> str:
        """
        Accessor method to return the origin of the literal.

        RETURNS
        -------
        str
            Origin of the literal
        """
        return self.origin

    def setOrigin(self, origin: str):
        """
        Mutator method to set the origin with specified origin.

        PARAMETERS
        ----------
        origin : str
            Origin of the literal to set
        """
        self.origin = origin

    def setSense(self, sense: int):
        """
        Mutator method to set the sense index of the literal.

        PARAMETERS
        ----------
        sense : int
            Sense index of the literal to set
        """
        self.sense = sense

    def addRelation(self, relation: Relation):
        """
        Appends the specified Relation to the end of relations list.

        PARAMETERS
        ----------
        relation : Relation
            Element to be appended to the list
        """
        self.relations.append(relation)

    def removeRelation(self, relation: Relation):
        """
        Removes the first occurrence of the specified element from relations list,
        if it is present. If the list does not contain the element, it stays unchanged.

        PARAMETERS
        ----------
        relation : Relation
            Element to be removed from the list, if present
        """
        self.relations.remove(relation)

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
        return relation in self.relations

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
        for relation in self.relations:
            if isinstance(relation, SemanticRelation) and relation.getRelationType() == semanticRelationType:
                return True
        return False

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
        return self.relations[index]

    def relationSize(self) -> int:
        """
        Returns size of relations list.

        RETURNS
        -------
        int
            The size of the list
        """
        return len(self.relations)

    def setName(self, name: str):
        """
        Mutator method to set name of a literal.

        PARAMETERS
        ----------
        name : str
            Name of the literal to set
        """
        self.name = name

    def setSynSetId(self, synSetId: str):
        """
        Mutator method to set SynSet ID of a literal.

        PARAMETERS
        ----------
        synSetId : str
            SynSet ID of the literal to set
        """
        self.synSetId = synSetId

    def saveAsXml(self, outfile):
        """
        Method to write Literals to the specified file in the XML format.

        PARAMETERS
        ----------
        outfile : file
            File to write XML files
        """
        if self.name == "&":
            outfile.write("<LITERAL>&amp;<SENSE>" + str(self.sense) + "</SENSE>")
        else:
            outfile.write("<LITERAL>" + self.name + "<SENSE>" + str(self.sense) + "</SENSE>")
        if self.origin is not None:
            outfile.write("<ORIGIN>" + self.origin + "</ORIGIN>")
        for r in self.relations:
            if isinstance(r, InterlingualRelation):
                outfile.write("<ILR>" + r.getName() + "<TYPE>" + r.getTypeAsString() + "</TYPE></ILR>")
            elif isinstance(r, SemanticRelation):
                if r.toIndex() == 0:
                    outfile.write("<SR>" + r.getName() + "<TYPE>" + r.getTypeAsString() + "</TYPE></SR>")
                else:
                    outfile.write("<SR>" + r.getName() + "<TYPE>" + r.getTypeAsString() + "</TYPE>" + "<TO>"
                                  + str(r.toIndex()) + "</TO>" + "</SR>")
        outfile.write("</LITERAL>")

    def __str__(self) -> str:
        """
        Overridden __str__ method to print names and sense of literals.

        RETURNS
        -------
        str
            Concatenated names and senses of literals
        """
        return self.name + " " + str(self.sense)
