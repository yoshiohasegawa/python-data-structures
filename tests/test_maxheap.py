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
# Constructor accepts argument of type list
def test_init():
    maxheap = MaxHeap(collection=[])
    assert maxheap.get() == []

    maxheap = MaxHeap(collection=[1, 2, 3, 4, 5])
    assert maxheap.get() == [5, 4, 2, 1, 3]

    with pytest.raises(TypeError):
        maxheap = MaxHeap(collection='I am not a list...')

# insert() adds a a value to the max heap in the appropriate place.
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

# remove_max() removes and returns the max value from the max heap.
# remove_max() re-builds the heap so that the max heap properties hold.
# remove_max() returns None if the max heap is empty.
def test_remove_max(maxheap: MaxHeap):
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    for val in values:
        maxheap.insert(val)
    assert maxheap.get() == [15, 10, 14, 7, 9, 11, 13, 1, 4, 3, 8, 2, 6, 5, 12]

    max_value = maxheap.remove_max()
    assert max_value == 15
    assert maxheap.get() == [14, 10, 13, 7, 9, 11, 12, 1, 4, 3, 8, 2, 6, 5]

    max_value = maxheap.remove_max()
    assert max_value == 14
    assert maxheap.get() == [13, 10, 12, 7, 9, 11, 5, 1, 4, 3, 8, 2, 6]

    max_value = maxheap.remove_max()
    assert max_value == 13
    assert maxheap.get() == [12, 10, 11, 7, 9, 6, 5, 1, 4, 3, 8, 2]

    max_value = maxheap.remove_max()
    assert max_value == 12
    assert maxheap.get() == [11, 10, 6, 7, 9, 2, 5, 1, 4, 3, 8]

    max_value = maxheap.remove_max()
    assert max_value == 11
    assert maxheap.get() == [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]

    max_value = maxheap.remove_max()
    assert max_value == 10
    assert maxheap.get() == [9, 8, 6, 7, 3, 2, 5, 1, 4]

    max_value = maxheap.remove_max()
    assert max_value == 9
    assert maxheap.get() == [8, 7, 6, 4, 3, 2, 5, 1]

    max_value = maxheap.remove_max()
    assert max_value == 8
    assert maxheap.get() == [7, 4, 6, 1, 3, 2, 5]

    max_value = maxheap.remove_max()
    assert max_value == 7
    assert maxheap.get() == [6, 4, 5, 1, 3, 2]

    max_value = maxheap.remove_max()
    assert max_value == 6
    assert maxheap.get() == [5, 4, 2, 1, 3]

    max_value = maxheap.remove_max()
    assert max_value == 5
    assert maxheap.get() == [4, 3, 2, 1]

    max_value = maxheap.remove_max()
    assert max_value == 4
    assert maxheap.get() == [3, 1, 2]

    max_value = maxheap.remove_max()
    assert max_value == 3
    assert maxheap.get() == [2, 1]

    max_value = maxheap.remove_max()
    assert max_value == 2
    assert maxheap.get() == [1]

    max_value = maxheap.remove_max()
    assert max_value == 1
    assert maxheap.get() == []

    max_value = maxheap.remove_max()
    assert max_value == None
    assert maxheap.get() == []