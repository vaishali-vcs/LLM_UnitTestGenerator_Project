# imports
import pytest  # used for our unit tests
import random  # used in the function to test

# function to test
def pickRandomChar(name):
    #Pick a random character from a given String
    char = random.choice(name)
    print("random char is ", char)
    return char  # added return statement to make function testable

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("name", [
    "Hello",  # non-empty string
    "Python",  # non-empty string
    "Hello@World",  # string with special characters
    "Python$3.8",  # string with special characters
    "Hello World",  # string with spaces
    "Python 3.8",  # string with spaces
    "Hello1World",  # string with numbers
    "Python38",  # string with numbers
    "H",  # single character string
    "P",  # single character string
    "HelloHello",  # string with repeating characters
    "PythonPython",  # string with repeating characters
    "Héllo",  # string with unicode characters
    "Pythön",  # string with unicode characters
    "Hello\nWorld",  # string with escape sequences
    "Python\t3.8",  # string with escape sequences
    "H" * 1000000,  # very long string
    "Python" * 1000000,  # very long string
    "\x00Hello\x00World\x00",  # string with non-printable characters
    "\x01Python\x01",  # string with non-printable characters
    " ",  # string with only spaces
    "  ",  # string with only spaces
    "@#$%^&*()",  # string with only special characters
    "!@#",  # string with only special characters
    "Hello World 123!@#",  # string with mixed types of characters
    "Python 3.8 *(&)",  # string with mixed types of characters
])
def test_pickRandomChar(name):
    # Test that the function returns a character from the string
    assert pickRandomChar(name) in name

# Test that the function raises an exception for an empty string
def test_pickRandomChar_empty():
    with pytest.raises(IndexError):
        pickRandomChar("")

# Test that the function raises an exception for a non-string input
def test_pickRandomChar_non_string():
    with pytest.raises(TypeError):
        pickRandomChar(123)
    with pytest.raises(TypeError):
        pickRandomChar([1, 2, 3])
    with pytest.raises(TypeError):
        pickRandomChar((1, 2, 3))