"""
A deque is an ordered collection of items similar to the queue. It has two ends,
a front and a rear, and the items remain positioned in the collection. Items can
be added or removed in either side of the data structure. As such, it is a hybrid
linear structure that provides all the capabilities of stacks and queues in a
single data structure.

Abstract implementation:
    > Deque() - create a new, empty deque
    > add_front() - adds a new item to the front of the deque
    > add_read() - adds a new item to the rear of the deque
    > remove_front() - removes the item at the front of the deque
    > remove_read() - rermoves the item at the the rear of the deque
    > is_empty() - checks if the deque is empty and returns a boolean
    > size() - returns an integer corresponding to the deque length
"""

from typing import Any, List, Iterable


class Deque(object):
    def __init__(self, sequence: Iterable) -> None:
        self.sequence = sequence
        self._items: List[Any] = [self.add_rear(s) for s in sequence]

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return self._items == []

    def add_front(self, item: Any) -> None:
        self._items.append(item)

    def add_rear(self, item: Any) -> None:
        self._items.insert(0, item)

    def remove_front(self) -> Any:
        return self._items.pop()

    def remove_rear(self) -> Any:
        return self._items.pop(0)

    def size(self) -> int:
        return len(self._items)


"""
Solve the palindrome problem using a deque data structure. Given a string of length n,
the idea is to iterate (n // 2 + 1) times and check if the removed values from both
front and rear are the same.
"""


def is_palindrome(word: str) -> bool:
    word_deque = Deque(word)

    while (len(word_deque)) > 1:
        first = word_deque.remove_rear()
        last = word_deque.remove_front()
        if first != last:
            return False

    return True


is_palindrome("lasdfjgsd")  # => False
is_palindrome("radar")  # => True
