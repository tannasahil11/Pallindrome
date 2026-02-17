"""
Tests the palindrome module
"""
import pytest
from palindrome import is_plalindrome

#Step 1
def test_is_plaindrome_with_int():
    """Raises ValueError if the user enters an int"""
    with pytest.raises(ValueError):
        is_plalindrome(1881)

def test_is_plaindrome_with_float():
    """Raises ValueError if the user enters an float"""
    with pytest.raises(ValueError):
        is_plalindrome(13.31)

#Step 2
def test_is_palindrome_with_empty_string():
    """Returns False when an empty string is entered"""
    assert is_plalindrome("") is False

#Step 3
def test_is_palindrome_with_one_character():
    """Returns True for all the single string characters"""
    assert is_plalindrome("a") is True

#Step 4
def test_is_palindrome_with_bb():
    """Returns True for all the palindromes with even length"""
    assert is_plalindrome("bb") is True

#Step 5
def test_is_palindrome_with_abc():
    """Returns False for non-palindrome words"""
    assert is_plalindrome("abc") is False

#Step 6
def test_is_palindrome_with_laval():
    """Returns True for all the palindromes with odd length"""
    assert is_plalindrome("laval") is True

#Step 7
def test_is_palindrome_with_toronto():
    """Returns False for non-palindrome words"""
    assert is_plalindrome("toronto") is False

#Step 8
def test_is_plalindrome_with_sentence():
    """Returns True for all the palindromes with different letter case"""
    assert is_plalindrome("Able was I ere I saw Elba") is True
