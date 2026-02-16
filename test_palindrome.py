"""
Tests the palindrome module
"""
import pytest
from palindrome import is_plalindrome

#Step 1
def test_is_plaindrome_with_int():
    with pytest.raises(ValueError):
        is_plalindrome(1881)

def test_is_plaindrome_with_float():
    with pytest.raises(ValueError):
        is_plalindrome(13.31)

#Step 2
def test_is_palindrome_with_empty_string():
    assert is_plalindrome("") == False

#Step 3
def test_is_palindrome_with_one_character():
    assert is_plalindrome("a") == True

#Step 4
def test_is_palindrome_with_bb():
    assert is_plalindrome("bb") == True

#Step 5
def test_is_palindrome_with_abc():
    assert is_plalindrome("abc") == False

#Step 6
def test_is_palindrome_with_laval():
    assert is_plalindrome("laval") == True

#Step 7
def test_is_palindrome_with_toronto():
    assert is_plalindrome("toronto") == False

#Step 8 
def test_is_plalindrome_with_sentence():
    assert is_plalindrome("Able was I ere I saw Elba") == True