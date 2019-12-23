from WordNet.InterlingualRelation import InterlingualRelation
from WordNet.Relation import Relation
from WordNet.SemanticRelation import SemanticRelation
from WordNet.SemanticRelationType import SemanticRelationType


class Literal:

    name: str
    sense: int
    synSetId: str
    origin: str = None
    relations: list

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
    def __init__(self, name: str, sense: int, synSetId: str):
        self.name = name
        self.sense = sense
        self.synSetId = synSetId
        self.relations = []

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
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.sense == other.sense

    """
    Accessor method to return SynSet ID.

    RETURNS
    -------
    str
        String of SynSet ID
    """
    def getSynSetId(self) -> str:
        return self.synSetId

    """
    Accessor method to return name of the literal.

    RETURNS
    -------
    str
        Name of the literal
    """
    def getName(self) -> str:
        return self.name

    """
    Accessor method to return the index of sense of the literal.

    RETURNS
    -------
    int
        Index of sense of the literal
    """
    def getSense(self) -> int:
        return self.sense

    """
    Accessor method to return the origin of the literal.
    
    RETURNS
    -------
    str
        Origin of the literal
    """
    def getOrigin(self) -> str:
        return self.origin

    """
    Mutator method to set the origin with specified origin.

    PARAMETERS
    ----------
    origin : str 
        Origin of the literal to set
    """
    def setOrigin(self, origin: str):
        self.origin = origin

    """
    Mutator method to set the sense index of the literal.

    PARAMETERS
    ----------
    sense : int
        Sense index of the literal to set
    """
    def setSense(self, sense: int):
        self.sense = sense

    """
    Appends the specified Relation to the end of relations list.

    PARAMETERS
    ----------
    relation : Relation
        Element to be appended to the list
    """
    def addRelation(self, relation: Relation):
        self.relations.append(relation)

    """
    Removes the first occurrence of the specified element from relations list,
    if it is present. If the list does not contain the element, it stays unchanged.

    PARAMETERS
    ----------
    relation : Relation
        Element to be removed from the list, if present
    """
    def removeRelation(self, relation: Relation):
        self.relations.remove(relation)

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
    def containsRelation(self, relation: Relation) -> bool:
        return relation in self.relations

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
    def containsRelationType(self, semanticRelationType: SemanticRelationType) -> bool:
        for relation in self.relations:
            if isinstance(relation, SemanticRelation) and relation.getRelationType() == semanticRelationType:
                return True
        return False

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
    def getRelation(self, index: int) -> Relation:
        return self.relations[index]

    """
    Returns size of relations list.

    RETURNS
    -------
    int
        The size of the list
    """
    def relationSize(self) -> int:
        return len(self.relations)

    """
    Mutator method to set name of a literal.

    PARAMETERS
    ----------
    name : str
        Name of the literal to set
    """
    def setName(self, name: str):
        self.name = name

    """
    Mutator method to set SynSet ID of a literal.

    PARAMETERS
    ----------
    synSetId : str
        SynSet ID of the literal to set
    """
    def setSynSetId(self, synSetId: str):
        self.synSetId = synSetId

    """
    Method to write Literals to the specified file in the XML format.

    PARAMETERS
    ----------
    outfile : file
        File to write XML files
    """
    def saveAsXml(self, outfile):
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

    """
    Overridden __str__ method to print names and sense of literals.

    RETURNS
    -------
    str
        Concatenated names and senses of literals
    """
    def __str__(self) -> str:
        return self.name + " " + str(self.sense)
