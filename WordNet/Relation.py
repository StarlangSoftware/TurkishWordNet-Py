class Relation:

    name: str

    """
    A constructor that sets the name of the relation.
    
    PARAMETERS
    ----------
    name : str
        String relation name
    """
    def __init__(self, name: str):
        self.name = name

    """
    An overridden equals method to compare two relations.

    PARAMETERS
    ----------
    other : Relation
        The reference object with which to compare
        
    RETURNS
    -------
    bool
        True if this object is the same as the obj argument; False otherwise.
    """
    def __eq__(self, other) -> bool:
        return self.name == other.name

    """
    Accessor method for the relation name.
    
    RETURNS
    ------
    str
        String relation name
    """
    def getName(self) -> str:
        return self.name

    """
    Mutator for the relation name.

    PARAMETERS
    ----------
    name : str
        String relation name
    """
    def setName(self, name: str):
        self.name = name
