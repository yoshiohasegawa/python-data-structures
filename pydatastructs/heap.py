#*****************************************************************************
# Programmer: Yoshio Hasegawa
# Class Name: Heap
#
# Revision     Date                        Release Comment
# --------  ----------  ------------------------------------------------------
#   1.0     07/09/2021   Initial Release
#
# File Description
# ----------------------------------------------------------------------------
# This is a parent class inherited by the Max Heap and Min Heap data 
# structures. It contains the _array property used by both MaxHeap and MinHeap,
# which is a list representing the heaps. It also contains some shared methods
# used to get or set/alter the data structure.
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
# get                         Returns the array
#*****************************************************************************
# Imported Packages:
from typing import TypeVar

T = TypeVar('T')

class Heap:
    """
    A class containing a _array property which contains a list. This class
    also contains methods used to get or set/alter the list. The contained
    methods are specific to a heap data structure. Once this class is
    instantiated, and empty list is assign to the _array property.
    """

    def __init__(self):
        """
        A class containing a _array property which contains a list. This class
        also contains methods used to get or set/alter the list. The contained
        methods are specific to a heap data structure. Once this class is
        instantiated, and empty list is assign to the _array property.
        """
        self._array: list = []
    
    def get(self) -> list:
        """
        This method is used to return the array representing the heap.

        Returns:
            list: array containing all data represented in the heap.
        """
        return self._array