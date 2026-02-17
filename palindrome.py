"""
Validates strings as palindromes.
"""
from collections import deque
def is_plalindrome(word):
    """Checks if the entered word reads the same backwards."""
    if not isinstance(word, str):
        raise ValueError("Input not a string")
    if len(word) == 0:
        return False
    dq = deque(word)
    while len(dq) > 1:
        if dq.pop().casefold() != dq.popleft().casefold():
            return False
    return True
