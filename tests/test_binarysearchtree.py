# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.binarysearchtree import BinarySearchTree

# Setup
# initialize _binarysearchtree in pytest fixture to be used in individual method tests
@pytest.fixture
def binarysearchtree():
    _binarysearchtree = BinarySearchTree(value=10)
    return _binarysearchtree

# Executions
# insert() adds a new instantiation of the BinarySearchTree class
# to the Binary Search Tree in the appropriate place.
def test_insert(binarysearchtree: BinarySearchTree):
    values = [5, 15, 1, 11, 6, 16]

    for val in values:
        binarysearchtree.insert(val)
    
    assert binarysearchtree.value == 10
    assert binarysearchtree.left.value == 5
    assert binarysearchtree.right.value == 15

    left = binarysearchtree.left
    right = binarysearchtree.right
    assert left.left.value == 1
    assert left.right.value == 6
    assert right.left.value == 11
    assert right.right.value == 16

# contains() returns a boolean verifying if a value is found within a Binary Search Tree
def test_contains(binarysearchtree: BinarySearchTree):
    assert binarysearchtree.contains(10) == True

    values = [5, 15, 1, 11, 6, 16]

    for val in values:
        binarysearchtree.insert(val)
    
    for val in values:
        assert binarysearchtree.contains(val) == True