#*****************************************************************************
# Programmer: Yoshio Hasegawa
# Class Name: MaxHeap
# Parent Class: Heap
#
# Revision     Date                        Release Comment
# --------  ----------  ------------------------------------------------------
#   1.0     07/08/2021   Initial Release
#
# File Description
# ----------------------------------------------------------------------------
# This is a class for the Max Heap data structure. It is a complete binary
# tree, where all parent node's values are greater than or equal to their
# child node's values. This data structure is represented by an array and,
# each node is represented by the value of an element in the array.
#
# Useful formulas:
# For a given node at index i...
# The parent node index = (i - 1) // 2
# The left child node index = (2 * 1) + 1
# The right child node index = (2 * 1) + 2
#
# Class Methods
# ----------------------------------------------------------------------------
#    Name                                       Description
# ----------                  ------------------------------------------------
# __init__                    Constructor
# insert                      Adds a node in the appropriate place
#*****************************************************************************
# Importing parent class List
from .heap import Heap
# Imported Packages:
from typing import TypeVar

T = TypeVar('T')

class MaxHeap(Heap):
    """
    A complete binary tree data structure represented as an array. Every parent
    node's value is greater than or equal to their child node's values.
    """

    def __init__(self):
        """
        A complete binary tree data structure represented as an array. Every parent
        node's value is greater than or equal to their child node's values.
        """
        Heap.__init__(self)
    
    def insert(self, value: T) -> None:
        """
        This method adds a child node to this max heap in the appropriate place.

        Args:
            value (T): The value to be added to this max heap.
        """
        if self._array == []:
            self._array.append(value)
        else:
            parent_idx = (len(self._array) - 1) // 2
            curr_idx = len(self._array)
            self._array.append(value)

            # While the value to be inserted is greater than it's parent,
            # keep swapping the parent and child from the bottom up until
            # the max heap is balance or, until swapped with the root node.
            while value > self._array[parent_idx] and parent_idx >= 0:
                temp_value = self._array[parent_idx]
                self._array[parent_idx] = value
                self._array[curr_idx] = temp_value
                curr_idx = parent_idx
                parent_idx = (parent_idx - 1) // 2



                
