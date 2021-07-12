<h1 align="center">Python Data Structures</h1>
<h4 align="center">For all of your data structure needs</h4>

# Table of Contents
1. [About](#about)
2. [Getting Started](#getting-started)
3. [Data Structures](#data-structures)
    * [Stack](#stack)
    * [Queue](#queue)
    * [Tree](#tree)
    * [Binary Search Tree](#binary-search-tree)
    * [Linked List](#linked-list)
    * [Max Heap](#max-heap)
    * [Min Heap](#min-heap)
4. [Contact](#contact)

# About
A Python package that contains common data structures. Data structures within this package also contain associated search and sorting algorithms. The intention of this package is mostly a learning endeavor but, it may also be used for various build purposes. I hope you find it easy to understand and interact with. If you have any questions or comments, please feel free to [reach out](#contact).

# Getting Started
Further information regarding this package can be found on the Python Package Index: [pydatastructs](https://pypi.org/project/pydatastructs/).

## Installation
To get started, install the package:
```console
pip install pydatastructs
```

Then, import it into your project:
```python
from pydatastructs import (
    Stack,
    Queue,
    Tree,
    BinarySearchTree,
    LinkedList,
    MaxHeap,
    MinHeap
    )
```

# Data Structures

## Stack
A list or array based data structure with last-in-first-out (LIFO) properties.

### Methods
- get()
- length()
- is_empty()
- push()
- pop()
- merge_sort()

### Usage
```python
from pydatastructs import Stack

my_stack = Stack(collection=[5, 3, 1, 4, 2])
length = my_stack.length()

if length < 6:
    my_stack.push(0)

my_stack.merge_sort() # [0, 1, 2, 3, 4, 5]
```

## Queue
A list or array based data structure with first-in-first-out (FIFO) properties.

### Methods
- get()
- length()
- is_empty()
- enqueue()
- dequeue()
- merge_sort()

### Usage
```python
from pydatastructs import Queue

my_queue = Queue(collection=[5, 3, 1, 4, 2])
queue_is_empty = my_queue.is_empty

if not queue_is_empty:
    print(my_queue.dequeue())

my_queue.merge_sort() # [1, 3, 4, 5]
```

## Tree
A node based data structure where each node contains a value property and a children property. The children property is a collection of child nodes. Finally, each node itself is a tree or sub-tree.

### Methods
- add()
- contains()
- depth_first_traversal()
- breadth_first_traversal()

### Usage
```python
from pydatastructs import Tree

my_tree = Tree(value=1)
my_tree.add(2)
my_tree.add(3)
my_tree.children[0].add(4)
my_tree.children[0].add(5)
my_tree.children[1].add(6)
my_tree.children[1].add(7)

result = []
def add_to_result(node: Tree):
    result.append(node.value)

my_tree.depth_first_traversal(add_to_result)
print(result) # [1, 2, 4, 5, 3, 6, 7]
              # my_tree: 
              #            1
              #        /      \
              #      2         3
              #   /    \     /   \
              #  4      5   6     7
```

## Binary Search Tree
A node based data structure where each node contains a value property and, a left and right property. The left and right properties point to potential child nodes. The left node's value will always be less than the parent node's value. The right node's value will always be greater than the parent node's value. Finally, each node itself is a tree or sub-tree.

### Methods
- insert()
- contains()
- depth_first_traversal()
- breadth_first_traversal()

### Usage
```python
from pydatastructs import BinarySearchTree

my_binarysearchtree = BinarySearchTree(value=10)
values = [6, 14, 4, 12, 8, 16]

for val in values:
    my_binarysearchtree.insert(val)

result = []
def add_to_result(node: BinarySearchTree):
    result.append(node.value)

my_binarysearchtree.breadth_first_traversal(add_to_result)
print(result) # [10, 6, 14, 4, 8, 12, 16]
              # my_binarysearchtree: 
              #            10
              #        /      \
              #      6         14
              #   /    \     /   \
              #  4      8   12     16
```

## Linked List
A node based data structure containing a head and tail property. The head points to the root node and, the tail points to the last node in the linked list. Each node has a value property and a next property, which points to the next node in the linked list.

### Methods
- append()
- remove_head()
- find_node()

### Usage
```python
from pydatastructs import LinkedList

my_linkedlist = LinkedList(value=1)
values = [2, 3, 4, 5]

for val in values:
    my_linkedlist.append(val)

node = my_linkedlist.find_node(3)

print(node.next.value) # 4
```

## Max Heap
A complete binary tree data structure represented as an array where, every parent node's value is greater than or equal to their child node's values.

### Methods
- get()
- insert()
- remove_max()

### Usage
```python
from pydatastructs import MaxHeap

my_maxheap = MaxHeap()
values = [1, 2, 3, 4, 5, 6, 7]

for val in values:
    my_maxheap.insert(val)

my_maxheap.get() # [7, 4, 6, 1, 3, 2, 5]
                 # my_maxheap: 
                 #            7
                 #        /      \
                 #      4         6
                 #   /    \     /   \
                 #  1      3   2     5
```

## Min Heap
A complete binary tree data structure represented as an array where, every parent node's value is less than or equal to their child node's values.

### Methods
- get()
- insert()
- remove_min()

### Usage
```python
from pydatastructs import MinHeap

my_minheap = MinHeap()
values = [7, 6, 5, 4, 3, 2, 1]

for val in values:
    my_minheap.insert(val)

my_minheap.get() # [1, 4, 2, 7, 5, 6, 3]
                 # my_minheap: 
                 #            1
                 #        /      \
                 #      4         2
                 #   /    \     /   \
                 #  7      5   6     3
```

# Contact
For support, feedback or, to report a bug, you may contact the maintainer:
- Yoshio Hasegawa: [GitHub](https://github.com/yoshiohasegawa), [LinkedIn](https://www.linkedin.com/in/yoshiohasegawa/)

## License
Distributed under the MIT License.