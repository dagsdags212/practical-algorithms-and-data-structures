"""
Stacks are ordered collections of items where the additionof new items and the removal
of existing items always take place at the same end. The end is commonly referred to
as the "top", and the opposite and is known as the "base".

Abstract implementation:
    > Stack() - creates a new, empty stack
    > push(item) - adds the given item to the top of the stack and returns nothing
    > pop() - removes and returns the top item from the stack
    > peek() - retuns the top item from the stack, but does not remove it
    > is_empty() - returns a boolean representing whether the stack is empty
    > stize() - returns the number of items on the stack as an integer
"""
from typing import List, Any


class Stack:
    def __init__(self):
        self._items: List[Any] = []

    def is_empty(self) -> bool:
        return not bool(self._items)

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        return self._items.pop()

    def peek(self) -> Any:
        return self._items[-1]

    def size(self) -> int:
        return len(self._items)

"""
A practical application of using stacks is checking wether parantheses
within a string are balaned, meaning each opening parenthesis has a corresponding
closing paranthesis. LSPs use this feature to check for code errors.
"""
def is_balanced(parentheses: str, opening: str = '(') -> bool:
    stack = Stack()
    for paren in parentheses:
        if paren == opening:
            stack.push(paren)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return stack.size() == 0

is_balanced('((()))') # => True
is_balanced('(()')    # => False
is_balanced('())')    # => False


"""
We can extend the `is_balanced` function to detect all symbols that must
occur in pairs such as '()', '{}', and '[]'.
"""
def is_balanced(symbols: str) -> bool:
    pairings = {
        '(': ')', '{': '}', '[': ']',   # brackets
        '\'': '\'', '\"': '\"'          # parantheses
    }
    stack = Stack()
    for s in symbols:
        if s in pairings:
            stack.push(s)
            continue
        try:
            opening_symbol = stack.pop()
        except IndexError:
            return False
        if s != pairings[opening_symbol]:
            # A mistmatch has occured
            return False
    return stack.size() == 0

is_balanced('{{([][])}()}') # => True
is_balanced('{[])')         # => False
is_balanced('((()))')       # => True
is_balanced('(()')          # => False
is_balanced('())')          # => False


"""
Another application of the stack is interconverting between number bases
such as binary to decimal and vice versa. Given an integer, we repeatedly
apply floor division to the input using the base as the dividend until the
resulting quotient is zero. The remainder is then pushed into the stack.
"""
def convert_to_binary(decimal: int) -> str:
    remainder_stack = Stack()

    while decimal > 0:
        remainder = decimal % 2
        remainder_stack.push(remainder)
        decimal //= 2

    binary_digits = []
    while not remainder_stack.is_empty():
        binary_digits.append(str(remainder_stack.pop()))

    return ''.join(binary_digits)

convert_to_binary(42)  # => '101010'

"""
The `convert_to_binary` function can be further generalized to other bases.
Below is an implementation of a decimal number than can be converted to any
base encoding.
"""
def convert_to_base(decimal: int, base: int) -> str:
    digits = '0123456789abcdef'
    remainder_stack = Stack()

    while decimal > 0:
        remainder = decimal % base
        remainder_stack.push(remainder)
        decimal //= base

    new_digits = []
    while not remainder_stack.is_empty():
        new_digits.append(digits[remainder_stack.pop()])

    return ''.join(new_digits)

convert_to_base(25, 2)  # => '11001'
convert_to_base(25, 16) # => '19'


"""
Create a 'fully parenthesized' expression to avoid ambiguity when determining the
order of operaion in a mathematical expression. Symbols * and % has precedence
over + and -. Operators of equal precedence are evaluated from left to right.
"""
