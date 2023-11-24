# imports
import pytest  # used for our unit tests

# function to test
def checkIsoGram(phrase):
    """The isogram is a string where the occurrence of each letter is exactly one. This code
    checks if a phrase or string is isogram
    """
    char_list = []
    for char in phrase:
        if char.isalpha():
            if char in char_list:
                return False
            char_list.append(char)
    return True

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input_string, expected_result", [
    ("", True),  # Empty string input
    ("a", True),  # Single character input
    ("abc", True),  # Multi-character string with no repeating characters
    ("hello", False),  # Multi-character string with repeating characters
    ("123abc", True),  # String with non-alphabetical characters
    ("abc abc", True),  # String with non-alphabetical characters
    ("Abcabc", False),  # String with case differences
    pytest.param(123, None, marks=pytest.mark.xfail(reason="Non-string input")),  # Non-string input
    ("abc$%&abc", True),  # String with special characters
    ("résumé", False),  # String with accented characters
    ("你好", True),  # String with Unicode characters
    ("abc123abc123", True),  # String with mixed alphanumeric characters
    ("abc\nabc", True),  # String with whitespace characters
    (" abc abc ", True),  # String with whitespace characters
])
def test_checkIsoGram(input_string, expected_result):
    assert checkIsoGram(input_string) == expected_result