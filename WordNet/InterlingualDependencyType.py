from enum import Enum, auto


class InterlingualDependencyType(Enum):
    HYPERNYM = auto()
    NEAR_ANTONYM = auto()
    HOLO_MEMBER = auto()
    HOLO_PART = auto()
    HOLO_PORTION = auto()
    USAGE_DOMAIN = auto()
    CATEGORY_DOMAIN = auto()
    BE_IN_STATE = auto()
    SUBEVENT = auto()
    VERB_GROUP = auto()
    SIMILAR_TO = auto()
    ALSO_SEE = auto()
    CAUSES = auto()
    SYNONYM = auto()
