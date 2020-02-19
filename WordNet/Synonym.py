from WordNet.Literal import Literal


class Synonym:

    __literals: list

    def __init__(self):
        """
        A constructor that creates a new list of literals.
        """
        self.__literals = []

    def addLiteral(self, literal: Literal):
        """
        Appends the specified Literal to the end of literals list.

        PARAMETERS
        ----------
        literal : Literal
            Element to be appended to the list
        """
        self.__literals.append(literal)

    def moveFirst(self, literal: Literal):
        """
        Moves the specified literal to the first of literals list.

        PARAMETERS
        ----------
        literal : Literal
            Element to be moved to the first element of the list
        """
        if self.contains(literal):
            self.__literals.remove(literal)
            self.__literals.insert(0, literal)

    def getLiteral(self, indexOrName) -> Literal:
        """
        Returns the element at the specified position in literals list.

        PARAMETERS
        ----------
        indexOrName : int
            index of the element to return

        RETURNS
        -------
        Literal
            The element at the specified position in the list
        """
        if isinstance(indexOrName, int):
            return self.__literals[indexOrName]
        elif isinstance(indexOrName, str):
            for literal in self.__literals:
                if literal.getName() == indexOrName:
                    return literal
        return None

    def literalSize(self) -> int:
        """
        Returns size of literals list.

        RETURNS
        -------
        int
            The size of the list
        """
        return len(self.__literals)

    def contains(self, literal: Literal) -> bool:
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
        return literal in self.__literals

    def containsLiteral(self, literalName: str) -> bool:
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
        for literal in self.__literals:
            if literal.getName() == literalName:
                return True
        return False

    def removeLiteral(self, toBeRemoved: Literal):
        """
        Removes the first occurrence of the specified element from literals list,
        if it is present. If the list does not contain the element, it stays unchanged.

        PARAMETERS
        ----------
        toBeRemoved : Literal
            Element to be removed from the list, if present
        """
        self.__literals.remove(toBeRemoved)

    def saveAsXml(self, outFile):
        """
        Method to write Synonyms to the specified file in the XML format.

        PARAMETERS
        ----------
        outFile
            File to write XML files
        """
        outFile.write("<SYNONYM>")
        for literal in self.__literals:
            literal.saveAsXml(outFile)
        outFile.write("</SYNONYM>")

    def __str__(self) -> str:
        """
        Overridden toString method to print literals.

        RETURNS
        -------
        str
            Concatenated literals
        """
        result = ""
        for literal in self.__literals:
            result = result + literal.getName() + " "
        return result
