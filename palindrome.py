"""
Validates strings as palindromes.
"""
def is_plalindrome(word):
    #Step 1
    if type(word) != str:
        raise ValueError("Input not a string")
    return  False