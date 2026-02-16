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