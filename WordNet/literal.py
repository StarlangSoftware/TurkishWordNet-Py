from typing import Optional, TextIO

from WordNet.InterlingualRelation import InterlingualRelation
from WordNet.Relation import Relation
from WordNet.SemanticRelation import SemanticRelation
from WordNet.SemanticRelationType import SemanticRelationType


class Literal:
    def __init__(self, name: str, sense: int, syn_set_id: str, origin: Optional[str] = None):
        """
        A constructor that initializes name, sense, SynSet ID and the relations.

        PARAMETERS
        ----------
        name : str
            name of a literal
        sense : int
            index of sense
        syn_set_id : str
            ID of the SynSet
        """
        self.name = name
        self.sense: int = sense
        self.syn_set_id: str = syn_set_id
        self.relations: list[Relation] = []
        self.origin = origin

    def add_relation(self, relation: Relation):
        """
        Appends the specified Relation to the end of relations list.

        PARAMETERS
        ----------
        relation : Relation
            Element to be appended to the list
        """
        self.relations.append(relation)

    def remove_relation(self, relation: Relation):
        """
        Removes the first occurrence of the specified element from relations list,
        if it is present. If the list does not contain the element, it stays unchanged.

        PARAMETERS
        ----------
        relation : Relation
            Element to be removed from the list, if present
        """
        self.relations.remove(relation)

    def contains_relation(self, relation: Relation) -> bool:
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

    def contains_relation_type(self, semantic_relation_type: SemanticRelationType) -> bool:
        """
        Returns True if specified semantic relation type presents in the relations list.

        PARAMETERS
        ----------
        semantic_relation_type : SemanticRelationType
            Element whose presence in the list is to be tested

        RETURNS
        -------
        bool
            True if specified semantic relation type presents in the relations list
        """
        for relation in self.relations:
            if isinstance(relation, SemanticRelation) and relation.getRelationType() == semantic_relation_type:
                return True
        return False

    def get_relation(self, index: int) -> Relation:
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
        if index >= len(self.relations) or index < 0:
            return None
        return self.relations[index]

    def save_as_xml(self, outfile: TextIO):
        """
        Method to write Literals to the specified file in the XML format.

        PARAMETERS
        ----------
        outfile : file
            File to write XML files
        """
        if self.name == "&":
            outfile.write(f"<LITERAL>&amp;<SENSE>{self.sense}</SENSE>")
        else:
            outfile.write(f"<LITERAL>{self.name}<SENSE>{self.sense}</SENSE>")
        if self.origin is not None:
            outfile.write(f"<ORIGIN>{self.origin}</ORIGIN>")
        for r in self.relations:
            if isinstance(r, InterlingualRelation):
                outfile.write(f"<ILR>{r.getName()}<TYPE>{r.getTypeAsString()}</TYPE></ILR>")
            elif isinstance(r, SemanticRelation):
                if r.toIndex() == 0:
                    outfile.write(f"<SR>{r.getName()}<TYPE>{r.getTypeAsString()}</TYPE></SR>")
                else:
                    outfile.write(f"<SR>{r.getName()}<TYPE>{r.getTypeAsString()}"
                                  f"</TYPE><TO>{r.toIndex()}</TO></SR>")
        outfile.write("</LITERAL>")

    def __str__(self) -> str:
        """
        Overridden __str__ method to print names and sense of literals.

        RETURNS
        -------
        str
            Concatenated names and senses of literals
        """
        return f"{self.name} {self.sense}"

    def __repr__(self):
        """
        The printable representation of the Literal object.
        """
        origin_repr = f', "{self.origin}"' if self.origin else ""
        return f'Literal("{self.name}", {self.sense}, "{self.syn_set_id}"{origin_repr})'

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
        return isinstance(other, Literal) and self.name == other.name and self.sense == other.sense

