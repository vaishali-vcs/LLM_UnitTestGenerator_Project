# imports
import pytest  # used for our unit tests

# function to test
def createMixString(s1, s2):
    """
    Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
    then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars
    go at the end of the result."""
    # get string length
    s1_length = len(s1)
    s2_length = len(s2)

    # get length of a bigger string
    length = s1_length if s1_length > s2_length else s2_length
    result = ""

    # reverse s2
    s2 = s2[::-1]

    # iterate string
    # s1 ascending and s2 descending
    for i in range(length):
        if i < s1_length:
            result = result + s1[i]
        if i < s2_length:
            result = result + s2[i]

    return result

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("s1, s2, expected", [
    ("abcd", "1234", "a4b3c2d1"),  # Both strings are of equal length
    ("abcdef", "123", "a3b2c1def"),  # s1 is longer than s2
    ("abc", "123456", "a6b5c4321"),  # s2 is longer than s1
    ("", "1234", "4321"),  # s1 is empty
    ("abcd", "", "abcd"),  # s2 is empty
    ("", "", ""),  # Both strings are empty
    ("a b c", "1 2 3", "a3 b2 c 1"),  # Strings contain spaces
    ("!@#", "$%^", "!^@%#$"),  # Strings contain special characters
    ("αβγ", "123", "α3β2γ1"),  # Strings contain non-alphanumeric characters
    ("AbC", "1a3", "A3b1Ca"),  # Strings contain mixed case characters
    ("こんにちは", "世界", "こ5ん4に3ち2は1"),  # Strings contain Unicode characters
    ("Hello\nWorld", "Python\tRules", "Hs\nEo\tlRlWuodl"),  # Strings contain escape sequences
    ("aaaaaa", "bbbbbb", "a6a5a4a3a2a1"),  # Strings contain only one type of character
    ("Hello\0World", "Python\0Rules", "Hs\0Eo\0lRlWuodl"),  # Strings contain non-printable characters
])
def test_createMixString(s1, s2, expected):
    assert createMixString(s1, s2) == expected