# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.stack import Stack

# Setup
# initialize _stack in pytest fixture to be used in individual method tests
@pytest.fixture
def stack():
    _stack = Stack(collection=[1, '2', {'3': 3}])
    return _stack

# Executions
# Constructor accepts argument of type list
def test_init():
    stack = Stack(collection=['I', 'am', 'a', 'list!'])
    assert stack.get() == ['I', 'am', 'a', 'list!']

    with pytest.raises(TypeError):
        stack = Stack(collection='I am not a list...')

# get() returns the entire stack
def test_get(stack: Stack):
    assert stack.get() == [1, '2', {'3': 3}]

# length() returns the number of items in the stack
def test_length(stack: Stack):
    assert stack.length() == 3

    stack.push(4.4)
    assert stack.length() == 4

# is_empty() returns a boolean verifying if the stack is empty
def test_is_empty(stack: Stack):
    assert stack.is_empty() == False

    for idx in range(stack.length()):
        stack.pop()
    assert stack.is_empty() == True

# push() adds an item to the top of the stack
# push() accepts any data type
def test_push(stack: Stack):
    stack.push(4)
    assert stack.get() == [1, '2', {'3': 3}, 4]

    stack.push('5')
    assert stack.get() == [1, '2', {'3': 3}, 4, '5']

    stack.push([6])
    assert stack.get() == [1, '2', {'3': 3}, 4, '5', [6]]

    stack.push(7.7)
    assert stack.get() == [1, '2', {'3': 3}, 4, '5', [6], 7.7]

    stack.push(None)
    assert stack.get() == [1, '2', {'3': 3}, 4, '5', [6], 7.7, None]

# pop() removes an item from the top of the stack
# pop() returns the removed item
# pop() will raise an IndexError if there are no items in the stack
def test_pop(stack: Stack):
    item = stack.pop()
    assert item == {'3': 3}
    assert stack.get() == [1, '2']

    for idx in range(stack.length()):
        stack.pop()

    with pytest.raises(IndexError):
        stack.pop()

# merge_sort() raises TypeError if provided an incorrect data type
# merge_sort() raises ValueError if provided an incorrect value
def test_merge_sort():
    stack = Stack([2, 3, 1])

    with pytest.raises(TypeError):
        stack.merge_sort(order=0)

    with pytest.raises(ValueError):
        stack.merge_sort(order='small to big')

# merge_sort() sorts the stack in ascending order by default, and if specified.
def test_merge_sort_asc():
    stack = Stack([6, 4, 8, 10, 3, 5, 1, 7, 9, 2])
    stack.merge_sort()
    assert stack.get() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    stack2 = Stack([2, 1, 3])
    stack2.merge_sort(order='asc')
    assert stack2.get() == [1, 2, 3]

# merge_sort() sorts the stack in descending order if specified.
def test_merge_sort_desc():
    stack = Stack([6, 4, 8, 10, 3, 5, 1, 7, 9, 2])
    stack.merge_sort(order='desc')
    assert stack.get() == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]