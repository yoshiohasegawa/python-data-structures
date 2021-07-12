# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.minheap import MinHeap

# Setup
# initialize _minheap in pytest fixture to be used in individual method tests
@pytest.fixture
def minheap():
    _minheap = MinHeap()
    return _minheap

# Executions
# insert() adds a a value to the min heap in the appropriate place.
def test_insert(minheap: MinHeap):
    values = [7, 6, 5, 4, 3, 2, 1]

    for val in values:
        minheap.insert(val)
    # tree: 
    #            7
    # tree: 
    #            6
    #         /   
    #       7
    # tree: 
    #            5
    #         /    \
    #       7       6
    # tree: 
    #            4
    #         /    \
    #       5       6
    #     / 
    #   7 
    # tree: 
    #            3
    #         /    \
    #       4       6
    #     /  \
    #   7     5
    # tree: 
    #            2
    #        /      \
    #      4         3
    #   /    \     /
    #  7      5   6
    # tree: 
    #            1
    #        /      \
    #      4         2
    #   /    \     /   \
    #  7      5   6     3

    assert minheap.get() == [1, 4, 2, 7, 5, 6, 3]