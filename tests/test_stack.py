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