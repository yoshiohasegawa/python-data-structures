# Third party imports
import pytest
# pydatastructs imports
from pydatastructs.linkedlist import LinkedList

# Setup
# initialize _linkedlist in pytest fixture to be used in individual method tests
@pytest.fixture
def linkedlist():
    _linkedlist = LinkedList()
    return _linkedlist

# Executions
# append() adds a new instantiation of the Node class to the end of the linked list
# append() accepts any data type
def test_append(linkedlist: LinkedList):
    assert linkedlist.head == None
    assert linkedlist.tail == None

    linkedlist.append(1)
    assert linkedlist.head.value == 1
    assert linkedlist.tail.value == 1

    count = 2
    while count <= 6:
        linkedlist.append(count)
        count += 1

    count = 1
    temp_node = linkedlist.head
    while count <= 6:
        assert temp_node.value == count
        if count < 6:
            assert temp_node.next.value == count + 1
        temp_node = temp_node.next
        count += 1
    
    expected = 'I\'m the tail!'
    linkedlist.append(expected)
    assert linkedlist.tail.value == expected

# remove_head() removes and returns the head node from the linked list
# remove_head() shifts the head property pointer to the next node in the linked list
# remove_head() returns None if the linked list is empty
def test_remove_head(linkedlist: LinkedList):
    assert linkedlist.remove_head() == None

    linkedlist.append(1)
    node = linkedlist.remove_head()
    assert node.value == 1
    assert node.next == None
    assert linkedlist.head == None
    assert linkedlist.tail == None

# find_node() finds and returns the first node that has the value provided
# find_node() returns None if no node contains the value provided
def test_find_node(linkedlist: LinkedList):
    linkedlist.append(1)
    assert linkedlist.find_node(2) == None

    linkedlist.append('2')
    linkedlist.append({'3': 3})
    linkedlist.append([4])
    linkedlist.append(5.5)

    node = linkedlist.find_node('2')
    assert node.value == '2'
    node = linkedlist.find_node({'3': 3})
    assert node.value == {'3': 3}
    node = linkedlist.find_node([4])
    assert node.value == [4]
    node = linkedlist.find_node(5.5)
    assert node.value == 5.5