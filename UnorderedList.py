"""
A list is a collection of nodes that hold a reference to the next node of the
data stucture. When each node holds a reference to the next node in the list,
it is called a singly linked list. When each node holds a reference to both the
next and previous nodes in the list, it is called a double linked list.

Abstract implementation:
    > List() - creates a new, empty list
    > add() - adds a new item to the list
    > remove(item) - removes the item from the list
    > search(item) - searches for the item in the list
    > is_empty() - checks if the list is empty and returns a boolean
    > size() - returns the number of items in the list
    > append(item) - adds anew item to the end of the list.
    > index(item) - returns the position of the item in the list
    > insert(pos, item) - adds a new item to the list at a given position
    > pop() - removes and returns the last item in the list
    > pop(pos) - removes and returns the item at a given position
"""

from typing import Any, Optional


class Node(object):
    """Represents a single item in a list."""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class UnorderedList(object):
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def view(self) -> None:
        ls = '['
        current = self.head
        while current is not None:
            if current.next:
                ls += f'{current.value}, '
            else:
                ls += f'{current.value}'
            current = current.next
        ls += ']'
        print(ls)

    def add(self, item: Any) -> None:
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self) -> int:
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item: Any) -> bool:
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def remove(self, item: Any) -> None:
        current = self.head
        previous = None
        while True:
            if current.value == item:
                break
            previous, current = current, current.next

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def index(self, item: Any) -> Optional[int]:
        current = self.head
        idx = 0
        while current is not None:
            if current.value == item:
                return idx
            current = current.next
            idx += 1

    def pop(self) -> Any:
        current = self.head
        previous = None
        while current.next is not None:
            previous, current = current, current.next
        previous.next = None
        return current.value

    def insert(self, pos: int, item: Any) -> None:
        assert pos < self.size(), "Cannot insert past the last element of the list"
        curr_pos = 0
        current = self.head
        previous = None
        while curr_pos != pos:
            previous, current = current, current.next
            curr_pos += 1
        new_node = Node(item)
        new_node.next = current
        previous.next = new_node


def test_unordered_list():
    ol = UnorderedList()
    ol.add(1)
    ol.add(2)
    ol.add(3)
    assert ol.size() == 3
    last = ol.pop()
    assert last == 1
    ol.insert(1, 10)
    inserted_idx = ol.index(10)
    assert inserted_idx == 1
    assert ol.search(72) == False
    ol.view()


test_unordered_list()
