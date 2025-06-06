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
    
    def get_item(self, index: int) -> Any:
        """
        Return the item at position <index> in this list.

        Precondition: index >= 0.

        Raises:
        (IndexError) if the <index> is out of bounds.

        Returns:
        (Any) The data value stored at the given index in the list.


        DocTest:

        >>> l = LinkedList()
        >>> l.add(2)
        >>> l.add(1)
        >>> l.get_item(0)
        1
        >>> l.get_item(1)
        2
        """
        
        curr = self.head 
        i = 0
        while curr is not None:
            if i == index:  #stopping condition
                return curr.data
            curr = curr.next
            i += 1
        raise IndexError("out of range") #raises error to prevent range issues

    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.

        Note that adding to the end of the list is okay.

        Raises:
            (IndexError) if index > len(self) or index < 0.

        Args:
            index (int): The index where the item will be inserted.
            item (Any): The data/contents of the item to be inserted.

        DocTest:
        >>> l = LinkedList()
        >>> l.insert(0, "first")  
        >>> l.get_item(0)
        'first'
        >>> l.size()
        1
        >>> l.insert(0, "first2")  
        >>> l.get_item(0)
        'first2'
        >>> l.get_item(1)
        'first'
        """
        
        if index < 0 or index > self.size():
            raise IndexError("out of range")
            
        new_node = Node(item, self.head)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
            
        curr = self.head
        i = 0
        while curr is not None and i < index - 1:
            curr = curr.next
            i += 1
            
        if curr is None: 
            raise IndexError("out of range")
            
        new_node.next = curr.next
        curr.next = new_node


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
