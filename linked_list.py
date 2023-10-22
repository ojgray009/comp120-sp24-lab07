"""
Module: linked_list

Implementation of a linked list.
"""

from typing import Any, Optional
from random import randrange, shuffle, seed

class Node:
    """ Class representing a single entry in a linked list.

    >>> n = Node(7, None)
    >>> n.data
    7
    >>> n.next
    None
    >>> m = Node(13, n)
    >>> m.data
    13
    >>> m.next.data
    7
    """
    data: Any
    next: Optional['Node']

    def __init__(self, data: Any, next: Optional['Node']) -> None:
        self.data = data
        self.next = next

class LinkedList:
    """
    Class representing a linked list, which implements the UnorderedList ADT.

    >>> l = LinkedList()
    >>> print(l)
    []
    >>> l.add(5)
    >>> l.add(-8.3)
    >>> print(l)
    [-8.3, 5]
    >>> l.size()
    2
    >>> l.search(-8.3)
    True
    >>> l.search(7)
    False
    >>> l2 = LinkedList()
    >>> l2.add(5)
    >>> l == l2
    False
    """

    head: Optional[Node]

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        if self.is_empty(): # empty list
            return '[]'

        current = self.head
        s = '['

        while current is not None:
            s += (str(current.data) + ', ')
            current = current.next

        # strip off the extraneous ', ' at the end
        s = s[:-2] + ']'
        return s


    def is_empty(self) -> bool:
        return self.head == None

    def add(self, data: Any) -> None:
        """ Adds new node containing data to front of list. """
        new_node = Node(data, self.head)
        self.head = new_node

    def size(self) -> int:
        """ Returns length of list. """
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, value: Any) -> bool:
        """ Returns True if <value> is located anywhere in this list. """
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next

        return False

    def __eq__(self, other) -> bool:
        """ Returns True if <other> has the same contents as this list. """

        current_self = self.head
        current_other = other.head

        while current_self is not None and current_other is not None:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next

        return current_self == current_other


def create_random_linked_list(size: int, seed_val: int = 42) -> LinkedList:
    """ Creates a linked list containing <size> random integers between
    -100000 and +100000.

    Args:
        size (int): The size of the linked list to generate
        seed (int): The seed to use for the random number generator (helpful
        for testing).

    Returns:
        (LinkedList): The linked list with random numbers
    """

    seed(seed_val)

    # create list of nodes with random vals
    nodes = [Node(randrange(-100000, 100001), None) for _ in range(size)]

    # shuffle them up so they aren't in memory order
    shuffle(nodes)

    # link each one to the next in the list
    for i in range(size-1):
        nodes[i].next = nodes[i+1]

    # create the linked list, setting the head to our first node
    new_list = LinkedList()
    new_list.head = nodes[0]

    return new_list
