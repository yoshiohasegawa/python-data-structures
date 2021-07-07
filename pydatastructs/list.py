#*****************************************************************************
# Programmer: Yoshio Hasegawa
# Class Name: List
#
# Revision     Date                        Release Comment
# --------  ----------  ------------------------------------------------------
#   1.0     07/07/2021   Initial Release
#
# File Description
# ----------------------------------------------------------------------------
# This is a parent class inherited by the Stack and Queue data structures. It
# contains the _data property used by both Stack and Queue, which is a list.
# It also contains some shared methods used to alter the data structure.
#
# Class Methods
# ----------------------------------------------------------------------------
#    Name                                       Description
# ----------                  ------------------------------------------------
# __init__                    Constructor
#*****************************************************************************
# Imported Packages:

class List:
    """
    A class containing a _data property which contains a list. This class
    also contains methods used to alter the list.
    If no argument is given, the constructor creates a new empty list.
    """

    def __init__(self, collection: list=[]):
        """
        A class containing a _data property which contains a list. This class
        also contains methods used to alter the list.
        If no argument is given, the constructor creates a new empty list.

        Args:
            collection (list, optional): A list to initialize the _data with. Defaults to [].

        Raises:
            TypeError: Raised when provided a non-list data type as an argument.
        """
        if isinstance(collection, list):
            self._data = collection
        else:
            raise TypeError('Argument \'collection\' must be of type list.')
    
    