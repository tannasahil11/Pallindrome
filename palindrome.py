"""
Validates strings as palindromes.
"""
def is_plalindrome(word):
    if type(word) != str:
        raise ValueError("Input not a string")
    if len(word) == 0:
        return False
    a = 0
    b = len(word) - 1
    while(a<b):
        if word[a].casefold() != word[b].casefold():
            return False
        a += 1
        b -= 1
    return True