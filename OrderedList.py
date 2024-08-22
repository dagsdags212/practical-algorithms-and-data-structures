from typing import Any
from UnorderedList import Node, UnorderedList


class OrderedList(UnorderedList):
    def add(self, item: Any) -> None:
        current = self.head
        previous = None
        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        new_node = Node(item)
        if previous is None:
            new_node.next, self.head = self.head, new_node
        else:
            new_node.next, previous.next = current, new_node

    def search(self, item: Any) -> bool:
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            if current.value > item:
                return False
            current = current.next
        return False
