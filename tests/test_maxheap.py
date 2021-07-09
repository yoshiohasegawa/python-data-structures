# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.maxheap import MaxHeap

# Setup
# initialize _maxheap in pytest fixture to be used in individual method tests
@pytest.fixture
def maxheap():
    _maxheap = MaxHeap()
    return _maxheap

# Executions
# insert() adds
def test_insert(maxheap: MaxHeap):
    values = [1, 2, 3, 4, 5, 6, 7]

    for val in values:
        maxheap.insert(val)
    # tree: 
    #            1
    # tree: 
    #            2
    #         /   
    #       1
    # tree: 
    #            3
    #         /    \
    #       1       2
    # tree: 
    #            4
    #         /    \
    #       3       2
    #     / 
    #   1 
    # tree: 
    #            5
    #         /    \
    #       4       2
    #     /  \
    #   1     3
    # tree: 
    #            6
    #        /      \
    #      4         5
    #   /    \     /
    #  1      3   2
    # tree: 
    #            7
    #        /      \
    #      4         6
    #   /    \     /   \
    #  1      3   2     5
    
    assert maxheap.get() == [7, 4, 6, 1, 3, 2, 5]