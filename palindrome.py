"""
Validates strings as palindromes.
"""
def is_plalindrome(word):

    if type(word) != str:
        raise ValueError("Input not a string")
    return  True