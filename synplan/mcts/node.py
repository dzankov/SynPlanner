"""Module containing a class Node in the tree search."""


class Node:
    """Node class represents a node in the tree search."""

    def __init__(
        self, precursors_to_expand: tuple = None, new_precursors: tuple = None
    ) -> None:
        """The function initializes the new Node object.

        :param precursors_to_expand: The tuple of precursors to be expanded. The first precursor
            in the tuple is the current precursor which will be expanded (for which new
            precursors will be generated by applying the predicted reaction rules). When
            the first precursor has been successfully expanded, the second precursor becomes
            the current precursor to be expanded.
        :param new_precursors: The tuple of new precursors generated by applying the reaction
            rule.
        """

        self.precursors_to_expand = precursors_to_expand
        self.new_precursors = new_precursors

        if len(self.precursors_to_expand) == 0:
            self.curr_precursor = tuple()
        else:
            self.curr_precursor = self.precursors_to_expand[0]
            self.next_precursor = self.precursors_to_expand[1:]

    def __len__(self) -> int:
        """Returns the number of precursor in the node to expand."""
        return len(self.precursors_to_expand)

    def __repr__(self) -> str:
        """Returns the SMILES of each precursor in precursor_to_expand and new_precursor."""
        return (
            f"New precursors: {self.new_precursors}\n"
            f"Precursors to expand: {self.precursors_to_expand}\n"
        )

    def is_solved(self) -> bool:
        """If True, it is a terminal node.

        There are no precursors for expansion.
        """

        return len(self.precursors_to_expand) == 0
