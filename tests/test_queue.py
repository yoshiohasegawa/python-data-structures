# Third party imports
import pytest
# pydatastructs imports
from pydatastructs import Queue

# Setup
# initialize _queue in pytest fixture to be used in individual method tests
@pytest.fixture
def queue():
    _queue = Queue([1, '2', {'3': 3}])
    return _queue

# Executions
# get() returns the entire queue
def test_get(queue: Queue):
    assert queue.get() == [1, '2', {'3': 3}]

# length() returns the number of items in the queue
def test_length(queue: Queue):
    assert queue.length() == 3

    queue.enqueue(0)
    assert queue.length() == 4

# is_empty() returns a boolean verifying if the queue is empty
def test_is_empty(queue: Queue):
    assert queue.is_empty() == False

    for idx in range(queue.length()):
        queue.dequeue()
    assert queue.is_empty() == True

# enqueue() adds an item to the end (left) of the queue
# enqueue() accepts any data type
def test_enqueue(queue: Queue):
    queue.enqueue(0)
    assert queue.get() == [0, 1, '2', {'3': 3}]

    queue.enqueue('-1')
    assert queue.get() == ['-1', 0, 1, '2', {'3': 3}]

    queue.enqueue([-2])
    assert queue.get() == [[-2], '-1', 0, 1, '2', {'3': 3}]

    queue.enqueue(-3.3)
    assert queue.get() == [-3.3, [-2], '-1', 0, 1, '2', {'3': 3}]

    queue.enqueue(None)
    assert queue.get() == [None, -3.3, [-2], '-1', 0, 1, '2', {'3': 3}]

# dequeue() removes an item from the front (right) of the queue
# dequeue() returns the removed item
# dequeue() will raise an IndexError if there are no items in the queue
def test_dequeue(queue: Queue):
    item = queue.dequeue()
    assert item == {'3': 3}
    assert queue.get() == [1, '2']

    for idx in range(queue.length()):
        queue.dequeue()

    with pytest.raises(IndexError):
        queue.dequeue()