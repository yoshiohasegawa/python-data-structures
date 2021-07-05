# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.tree import Tree

# Setup
# initialize _tree in pytest fixture to be used in individual method tests
@pytest.fixture
def tree():
    _tree = Tree(value=1)
    return _tree

# Executions
# add() adds a new instantiation of the Tree class
# to the collection in the children property
def test_add(tree: Tree):
    count = 2
    temp_node = tree
    while count <= 7:
        temp_node.add(count)
        temp_node = temp_node.children[0]
        count += 1
    
    count = 1
    temp_node = tree
    while count <= 6:
        assert temp_node.value == count
        temp_node = temp_node.children[0]
        count += 1
    
# contains() returns a boolean verifying if a value is found within a sub-tree
def test_contains(tree: Tree):
    assert tree.contains(1) == True

    count = 2
    temp_node = tree
    while count <= 7:
        temp_node.add(count)
        temp_node = temp_node.children[0]
        count += 1
    
    count = 1
    while count <= 7:
        assert tree.contains(count) == True
        count += 1