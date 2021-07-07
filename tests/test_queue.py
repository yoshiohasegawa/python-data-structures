# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.queue import Queue

# Setup
# initialize _queue in pytest fixture to be used in individual method tests
@pytest.fixture
def queue():
    _queue = Queue(collection=[1, '2', {'3': 3}])
    return _queue

# Executions
# Constructor accepts argument of type list
def test_init():
    queue = Queue(collection=['I', 'am', 'a', 'list!'])
    assert queue.get() == ['I', 'am', 'a', 'list!']

    with pytest.raises(TypeError):
        queue = Queue(collection='I am not a list...')

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

# merge_sort() raises TypeError if provided an incorrect data type
# merge_sort() raises ValueError if provided an incorrect value
def test_merge_sort():
    queue = Queue([2, 3, 1])

    with pytest.raises(TypeError):
        queue.merge_sort(order=0)

    with pytest.raises(ValueError):
        queue.merge_sort(order='small to big')

# merge_sort() sorts the queue in ascending order by default, and if specified.
def test_merge_sort_asc():
    queue = Queue([6, 4, 8, 10, 3, 5, 1, 7, 9, 2])
    queue.merge_sort()
    assert queue.get() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    queue2 = Queue([2, 1, 3])
    queue2.merge_sort(order='asc')
    assert queue2.get() == [1, 2, 3]

# merge_sort() sorts the queue in descending order if specified.
def test_merge_sort_desc():
    queue = Queue([6, 4, 8, 10, 3, 5, 1, 7, 9, 2])
    queue.merge_sort(order='desc')
    assert queue.get() == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]