"""
A queue is an ordered collection of items where the addition of new items
happens at one end (called the "rear") and the removal of existing items
occurs at the other end (called the "front").

Abstract implementation:
    > Queue() - creates an empty queue
    > enqueue(item) - add a new item to the read of the queue
    > dequeue() - removes the front item from the queue
    > is_empty() - checks whether the queue is empty and returns a bool
    > size() - return the number of items in the queue as an integer
"""

from typing import Any, Iterable
from collections import deque


class Queue:
    def __init__(self) -> None:
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self._items == []

    def enqueue(self, item: Any) -> None:
        self._items.insert(0, item)

    def dequeue(self) -> Any:
        return self._items().pop()

    def size(self) -> int:
        return len(self._items)


"""
Simulating a game of Hot Potato.
"""


def hot_potato(names: Iterable[str], num: int) -> str:
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while len(queue) > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())

        # Remove child at the rear of the queue
        queue.dequeue()

    return queue.dequeue()


num = 9
children = ("Bill", "David", "Susan", "Jane", "Kent", "Brad")
hot_potato(children, num)   # => 'David'
