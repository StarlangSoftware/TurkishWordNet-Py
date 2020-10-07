from WordNet.Relation import Relation
from WordNet.SemanticRelationType import SemanticRelationType


class SemanticRelation(Relation):
    __relationType: SemanticRelationType
    __toIndex: int

    semanticDependency = ["ANTONYM", "HYPERNYM", "INSTANCE_HYPERNYM", "HYPONYM", "INSTANCE_HYPONYM", "MEMBER_HOLONYM",
                          "SUBSTANCE_HOLONYM", "PART_HOLONYM", "MEMBER_MERONYM", "SUBSTANCE_MERONYM", "PART_MERONYM",
                          "ATTRIBUTE", "DERIVATION_RELATED", "DOMAIN_TOPIC", "MEMBER_TOPIC", "DOMAIN_REGION",
                          "MEMBER_REGION", "DOMAIN_USAGE", "MEMBER_USAGE", "ENTAILMENT", "CAUSE", "ALSO_SEE",
                          "VERB_GROUP", "SIMILAR_TO", "PARTICIPLE_OF_VERB"]

    semanticDependencyTags = [SemanticRelationType.ANTONYM, SemanticRelationType.HYPERNYM,
                              SemanticRelationType.INSTANCE_HYPERNYM, SemanticRelationType.HYPONYM,
                              SemanticRelationType.INSTANCE_HYPONYM,
                              SemanticRelationType.MEMBER_HOLONYM, SemanticRelationType.SUBSTANCE_HOLONYM,
                              SemanticRelationType.PART_HOLONYM, SemanticRelationType.MEMBER_MERONYM,
                              SemanticRelationType.SUBSTANCE_MERONYM, SemanticRelationType.PART_MERONYM,
                              SemanticRelationType.ATTRIBUTE,
                              SemanticRelationType.DERIVATION_RELATED, SemanticRelationType.DOMAIN_TOPIC,
                              SemanticRelationType.MEMBER_TOPIC, SemanticRelationType.DOMAIN_REGION,
                              SemanticRelationType.MEMBER_REGION,
                              SemanticRelationType.DOMAIN_USAGE, SemanticRelationType.MEMBER_USAGE,
                              SemanticRelationType.ENTAILMENT, SemanticRelationType.CAUSE,
                              SemanticRelationType.ALSO_SEE,
                              SemanticRelationType.VERB_GROUP, SemanticRelationType.SIMILAR_TO,
                              SemanticRelationType.PARTICIPLE_OF_VERB]

    @staticmethod
    def getSemanticTag(tag: str) -> SemanticRelationType:
        """
        Accessor to retrieve semantic relation type given a specific semantic dependency tag.

        PARAMETERS
        ----------
        tag : str
            String semantic dependency tag

        RETURNS
        -------
        SemanticRelationType
            Semantic relation type
        """
        for i in range(len(SemanticRelation.semanticDependencyTags)):
            if tag == SemanticRelation.semanticDependency[i]:
                return SemanticRelation.semanticDependencyTags[i]
        return None

    @staticmethod
    def reverse(semanticRelationType: SemanticRelationType) -> SemanticRelationType:
        """
        Returns the reverse of a specific semantic relation type.

        PARAMETERS
        ----------
        semanticRelationType : SemanticRelationType
            semantic relation type to be reversed

        RETURNS
        -------
        SemanticRelationType
            Reversed version of the semantic relation type
        """
        if semanticRelationType == SemanticRelationType.HYPERNYM:
            return SemanticRelationType.HYPONYM
        elif semanticRelationType == SemanticRelationType.HYPONYM:
            return SemanticRelationType.HYPERNYM
        elif semanticRelationType == SemanticRelationType.ANTONYM:
            return SemanticRelationType.ANTONYM
        elif semanticRelationType == SemanticRelationType.INSTANCE_HYPERNYM:
            return SemanticRelationType.INSTANCE_HYPONYM
        elif semanticRelationType == SemanticRelationType.INSTANCE_HYPONYM:
            return SemanticRelationType.INSTANCE_HYPERNYM
        elif semanticRelationType == SemanticRelationType.MEMBER_HOLONYM:
            return SemanticRelationType.MEMBER_MERONYM
        elif semanticRelationType == SemanticRelationType.MEMBER_MERONYM:
            return SemanticRelationType.MEMBER_HOLONYM
        elif semanticRelationType == SemanticRelationType.PART_MERONYM:
            return SemanticRelationType.PART_HOLONYM
        elif semanticRelationType == SemanticRelationType.PART_HOLONYM:
            return SemanticRelationType.PART_MERONYM
        elif semanticRelationType == SemanticRelationType.SUBSTANCE_MERONYM:
            return SemanticRelationType.SUBSTANCE_HOLONYM
        elif semanticRelationType == SemanticRelationType.SUBSTANCE_HOLONYM:
            return SemanticRelationType.SUBSTANCE_MERONYM
        elif semanticRelationType == SemanticRelationType.DOMAIN_TOPIC:
            return SemanticRelationType.MEMBER_TOPIC
        elif semanticRelationType == SemanticRelationType.MEMBER_TOPIC:
            return SemanticRelationType.DOMAIN_TOPIC
        elif semanticRelationType == SemanticRelationType.DOMAIN_REGION:
            return SemanticRelationType.MEMBER_REGION
        elif semanticRelationType == SemanticRelationType.MEMBER_REGION:
            return SemanticRelationType.DOMAIN_REGION
        elif semanticRelationType == SemanticRelationType.DOMAIN_USAGE:
            return SemanticRelationType.MEMBER_USAGE
        elif semanticRelationType == SemanticRelationType.MEMBER_USAGE:
            return SemanticRelationType.DOMAIN_USAGE
        elif semanticRelationType == SemanticRelationType.DERIVATION_RELATED:
            return SemanticRelationType.DERIVATION_RELATED
        return None

    def __init__(self, name: str, relationType, toIndex=None):
        """
        Constructor that initializes relation type, relation name, and the index.

        PARAMETERS
        ----------
        name : str
            name of the relation
        relationType
            semantic dependency tag
        toIndex : int
            index of the relation
        """
        super().__init__(name)
        if toIndex is not None:
            self.__toIndex = toIndex
        else:
            self.__toIndex = 0
        if isinstance(relationType, str):
            self.__relationType = SemanticRelation.getSemanticTag(relationType)
        elif isinstance(relationType, SemanticRelationType):
            self.__relationType = relationType

    def __eq__(self, other):
        """
        An overridden equals method to compare two SemanticRelations.

        PARAMETERS
        ----------
        other : SemanticRelation
            The reference object with which to compare

        RETURNS
        -------
        bool
            True if this object is the same as the obj argument; False otherwise.
        """
        return self.name == other.name and self.__relationType == other.__relationType and \
               self.__toIndex == other.__toIndex

    def toIndex(self) -> int:
        """
        Returns the index value.

        RETURNS
        -------
        int
            index value.
        """
        return self.__toIndex

    def getRelationType(self) -> SemanticRelationType:
        """
        Accessor for the semantic relation type.

        RETURNS
        -------
        SemanticRelationType
            semantic relation type
        """
        return self.__relationType

    def setRelationType(self, relationType: SemanticRelationType):
        """
        Mutator for the semantic relation type.

        PARAMETERS
        ----------
        relationType : SemanticRelationType
            semantic relation type.
        """
        self.__relationType = relationType

    def getTypeAsString(self) -> str:
        """
        Accessor method to retrieve the semantic relation type as a String.

        RETURNS
        -------
        str
            String semantic relation type
        """
        if self.__relationType is not None:
            return self.__relationType.name
        else:
            return None

    def __str__(self) -> str:
        """
        Overridden __str__ method to print semantic relation types and names.

        RETURNS
        -------
        str
            Semantic relation types and names
        """
        return self.getTypeAsString() + "->" + self.name
