from WordNet.Literal import Literal


class Synonym:

    __literals: list

    """
    A constructor that creates a new list of literals.
    """
    def __init__(self):
        self.__literals = []

    """
    Appends the specified Literal to the end of literals list.

    PARAMETERS
    ----------
    literal : Literal
        Element to be appended to the list
    """
    def addLiteral(self, literal: Literal):
        self.__literals.append(literal)

    """
    Moves the specified literal to the first of literals list.

    PARAMETERS
    ----------
    literal : Literal
        Element to be moved to the first element of the list
    """
    def moveFirst(self, literal: Literal):
        if self.contains(literal):
            self.__literals.remove(literal)
            self.__literals.insert(0, literal)

    """
    Returns the element at the specified position in literals list.

    PARAMETERS
    ----------
    index : int
        index of the element to return
        
    RETURNS
    -------
    Literal
        The element at the specified position in the list
    """
    def getLiteral(self, indexOrName) -> Literal:
        if isinstance(indexOrName, int):
            return self.__literals[indexOrName]
        elif isinstance(indexOrName, str):
            for literal in self.__literals:
                if literal.getName() == indexOrName:
                    return literal
        return None

    """
    Returns size of literals list.

    RETURNS
    -------
    int
        The size of the list
    """
    def literalSize(self) -> int:
        return len(self.__literals)

    """
    Returns true if literals list contains the specified literal.

    PARAMETERS
    ----------
    literal : Literal
        Element whose presence in the list is to be tested
        
    RETURNS
    -------
    bool
        True if the list contains the specified element
    """
    def contains(self, literal: Literal) -> bool:
        return literal in self.__literals

    """
    Returns True if literals list contains the specified String literal.

    PARAMETERS
    ----------
    literalName : str
        element whose presence in the list is to be tested
        
    RETURNS
    -------
        True if the list contains the specified element
    """
    def containsLiteral(self, literalName: str) -> bool:
        for literal in self.__literals:
            if literal.getName() == literalName:
                return True
        return False

    """
    Removes the first occurrence of the specified element from literals list,
    if it is present. If the list does not contain the element, it stays unchanged.

    PARAMETERS
    ----------
    toBeRemoved : Literal
        Element to be removed from the list, if present
    """
    def removeLiteral(self, toBeRemoved: Literal):
        self.__literals.remove(toBeRemoved)

    """
    Method to write Synonyms to the specified file in the XML format.

    PARAMETERS
    ----------
    outFile 
        File to write XML files
    """
    def saveAsXml(self, outFile):
        outFile.write("<SYNONYM>")
        for literal in self.__literals:
            literal.saveAsXml(outFile)
        outFile.write("</SYNONYM>")

    """
    Overridden toString method to print literals.

    RETURNS
    -------
    str
        Concatenated literals
    """
    def __str__(self) -> str:
        result = ""
        for literal in self.__literals:
            result = result + literal.getName() + " "
        return result
