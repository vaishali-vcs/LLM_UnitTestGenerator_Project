# imports
import pytest  # used for our unit tests

# function to test
def find_digits_chars_symbols(sample_str):
    # Count all letters, digits, and special symbols from a given string
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    return char_count, digit_count, symbol_count

# unit tests
@pytest.mark.parametrize("input_str, expected_output", [
    ("HelloWorld", (10, 0, 0)),  # only letters
    ("1234567890", (0, 10, 0)),  # only digits
    ("!@#$%^&*()", (0, 0, 10)),  # only special symbols
    ("HelloWorld123!@#", (10, 3, 3)),  # mix of letters, digits, and special symbols
    ("", (0, 0, 0)),  # empty string
    ("Hello World", (10, 0, 1)),  # string with whitespace
    ("こんにちは世界", (0, 0, 8)),  # non-ASCII characters
    ("Hello\\nWorld", (10, 0, 2)),  # string with escape sequences
    ("HelloWorld", (10, 0, 0)),  # mix of uppercase and lowercase letters
    ("aaaaaaa", (7, 0, 0)),  # repeated characters
    ("a", (1, 0, 0)),  # single character
    ("\x07", (0, 0, 1)),  # control characters
    ("😀", (0, 0, 1)),  # Unicode characters
    ("a" * 1000000, (1000000, 0, 0)),  # extremely long string
    ("Hello\x00World", (10, 0, 1)),  # string with null characters
    ("\"", (0, 0, 1)),  # special meaning in Python
    ("Hello, 世界", (5, 0, 3)),  # different scripts
    ("l", (1, 0, 0)),  # visually similar but different Unicode codes
])
def test_find_digits_chars_symbols(input_str, expected_output):
    assert find_digits_chars_symbols(input_str) == expected_output