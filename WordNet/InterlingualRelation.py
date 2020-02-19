from WordNet.InterlingualDependencyType import InterlingualDependencyType
from WordNet.Relation import Relation


class InterlingualRelation(Relation):
    __dependencyType: InterlingualDependencyType

    ilrDependency = ["Hypernym", "Near_antonym", "Holo_member", "Holo_part", "Holo_portion",
                     "Usage_domain", "Category_domain", "Be_in_state", "Subevent", "Verb_group",
                     "Similar_to", "Also_see", "Causes", "SYNONYM"]

    interlingualDependencyTags = [InterlingualDependencyType.HYPERNYM,
                                  InterlingualDependencyType.NEAR_ANTONYM, InterlingualDependencyType.HOLO_MEMBER,
                                  InterlingualDependencyType.HOLO_PART,
                                  InterlingualDependencyType.HOLO_PORTION, InterlingualDependencyType.USAGE_DOMAIN,
                                  InterlingualDependencyType.CATEGORY_DOMAIN,
                                  InterlingualDependencyType.BE_IN_STATE, InterlingualDependencyType.SUBEVENT,
                                  InterlingualDependencyType.VERB_GROUP,
                                  InterlingualDependencyType.SIMILAR_TO, InterlingualDependencyType.ALSO_SEE,
                                  InterlingualDependencyType.CAUSES,
                                  InterlingualDependencyType.SYNONYM]

    @staticmethod
    def getInterlingualDependencyTag(tag: str) -> InterlingualDependencyType:
        """
        Compares specified str tag with the tags in InterlingualDependencyType array, ignoring case
        considerations.

        PARAMETERS
        ----------
        tag : str
            String to compare

        RETURNS
        -------
        InterlingualDependencyType
            Interlingual dependency type according to specified tag
        """
        for i in range(len(InterlingualRelation.ilrDependency)):
            if tag == InterlingualRelation.ilrDependency[i]:
                return InterlingualRelation.interlingualDependencyTags[i]
        return None

    def __init__(self, name: str, dependencyType: str):
        """
        InterlingualRelation method sets its relation with the specified String name, then gets the
        InterlingualDependencyType according to specified String dependencyType.

        PARAMETERS
        ----------
        name : str
            relation name
        dependencyType : str
            interlingual dependency type
        """
        super().__init__(name)
        self.__dependencyType = InterlingualRelation.getInterlingualDependencyTag(dependencyType)

    def getType(self) -> InterlingualDependencyType:
        """
        Accessor method to get the private InterlingualDependencyType.

        RETURNS
        -------
        InterlingualDependencyType
            Interlingual dependency type
        """
        return self.__dependencyType

    def getTypeAsString(self) -> str:
        """
        Method to retrieve interlingual dependency type as str.

        RETURNS
        -------
        str
            String interlingual dependency type
        """
        return self.__dependencyType.name

    def __str__(self) -> str:
        """
        __str__ method to print interlingual dependency type.

        RETURNS
        -------
        str
            String of relation name
        """
        return self.getTypeAsString() + "->" + self.name
