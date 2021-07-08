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
    
# contains() returns a boolean verifying if a value is found within a Tree
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

# depth_first_traversal() traverses the tree in a depth first manner
# depth_first_traversal() runs a callback function on each node in order
def test_depth_first_traversal(tree: Tree):
    tree.add(2)
    tree.add(3)
    tree.children[0].add(4)
    tree.children[0].add(5)
    tree.children[1].add(6)
    tree.children[1].add(7)
    # tree: 
    #            1
    #        /      \
    #      2         3
    #   /    \     /   \
    #  4      5   6     7

    result = []
    def add_to_result(node: Tree):
        result.append(node.value)
    
    tree.depth_first_traversal(add_to_result)
    assert result == [1, 2, 4, 5, 3, 6, 7]
