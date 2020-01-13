class IdMapping:

    __map: dict

    """
    Constructor to load ID mappings from given file to a map.

    PARAMETERS
    ----------
    fileName : str
        String file name input that will be read
    """
    def __init__(self, fileName=None):
        self.__map = {}
        if fileName is not None:
            infile = open(fileName, "r", encoding="utf8")
            lines = infile.readlines()
            for line in lines:
                items = line.split("->")
                self.__map[items[0]] = items[1]

    """
    Returns a Set view of the keys contained in this map.

    RETURNS
    -------
    set
        A set view of the keys contained in this map
    """
    def keySet(self) -> set:
        return set(self.__map.keys())

    """
    Returns the value to which the specified key is mapped, or None if this map contains no mapping for the key.

    PARAMETERS
    ----------
    id : str
        String id of a key
        
    RETURNS
    -------
    str
        Value of the specified key
    """
    def map(self, id: str) -> str:
        if id not in self.__map:
            return None
        mappedId = self.__map[id]
        while mappedId in self.__map:
            mappedId = self.__map[mappedId]
        return mappedId

    """
    Returns the value to which the specified key is mapped.

    PARAMETERS
    ----------
    id : str
        String id of a key
        
    RETURNS
    -------
    str
        Value of the specified key
    """
    def singleMap(self, id: str) -> str:
        return self.__map[id]

    """
    Associates the specified value with the specified key in this map.

    PARAMETERS
    ----------
    key : str  
        key with which the specified value is to be associated
    value : str
        value to be associated with the specified key
    """
    def add(self, key: str, value: str):
        self.__map[key] = value

    """
    Removes the mapping for the specified key from this map if present.

    PARAMETERS
    ----------
    key : str
        key whose mapping is to be removed from the map
    """
    def remove(self, key: str):
        self.__map.pop(key)

    """
    Saves map to the specified file.

    PARAMETERS
    ----------
    fileName : str
        String file to write map
    """
    def save(self, fileName: str):
        outfile = open(fileName, "w", encoding="utf8")
        for key in self.__map:
            outfile.write(key + "->" + self.__map[key] + "\n")
        outfile.close()
