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

# remove_min() removes and returns the min value from the min heap.
# remove_min() re-builds the heap so that the min heap properties hold.
# remove_min() returns None if the min heap is empty.
def test_remove_min(minheap: MinHeap):
    values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    for val in values:
        minheap.insert(val)
    assert minheap.get() == [1, 6, 2, 9, 7, 5, 3, 15, 12, 13, 8, 14, 10, 11, 4]

    min_value = minheap.remove_min()
    assert min_value == 1
    assert minheap.get() == [2, 6, 3, 9, 7, 5, 4, 15, 12, 13, 8, 14, 10, 11]

    min_value = minheap.remove_min()
    assert min_value == 2
    assert minheap.get() == [3, 6, 4, 9, 7, 5, 11, 15, 12, 13, 8, 14, 10]

    min_value = minheap.remove_min()
    assert min_value == 3
    assert minheap.get() == [4, 6, 5, 9, 7, 10, 11, 15, 12, 13, 8, 14]

    min_value = minheap.remove_min()
    assert min_value == 4
    assert minheap.get() == [5, 6, 10, 9, 7, 14, 11, 15, 12, 13, 8]

    min_value = minheap.remove_min()
    assert min_value == 5
    assert minheap.get() == [6, 7, 10, 9, 8, 14, 11, 15, 12, 13]

    min_value = minheap.remove_min()
    assert min_value == 6
    assert minheap.get() == [7, 8, 10, 9, 13, 14, 11, 15, 12]

    min_value = minheap.remove_min()
    assert min_value == 7
    assert minheap.get() == [8, 9, 10, 12, 13, 14, 11, 15]

    min_value = minheap.remove_min()
    assert min_value == 8
    assert minheap.get() == [9, 12, 10, 15, 13, 14, 11]

    min_value = minheap.remove_min()
    assert min_value == 9
    assert minheap.get() == [10, 12, 11, 15, 13, 14]

    min_value = minheap.remove_min()
    assert min_value == 10
    assert minheap.get() == [11, 12, 14, 15, 13]

    min_value = minheap.remove_min()
    assert min_value == 11
    assert minheap.get() == [12, 13, 14, 15]

    min_value = minheap.remove_min()
    assert min_value == 12
    assert minheap.get() == [13, 15, 14]

    min_value = minheap.remove_min()
    assert min_value == 13
    assert minheap.get() == [14, 15]

    min_value = minheap.remove_min()
    assert min_value == 14
    assert minheap.get() == [15]

    min_value = minheap.remove_min()
    assert min_value == 15
    assert minheap.get() == []

    min_value = minheap.remove_min()
    assert min_value == None
    assert minheap.get() == []