# imports
import pytest  # used for our unit tests

# function to test
def remove_chars(word, n):
    # Remove first n characters from a string
    print('Original string:', word)
    x = word[n:]
    return x

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test normal case with a string and a positive integer
@pytest.mark.parametrize("word, n, expected", [("Hello, World!", 5, ', World!'), ("Python", 3, 'hon')])
def test_remove_chars_normal(word, n, expected):
    assert remove_chars(word, n) == expected

# Test edge case with an empty string
@pytest.mark.parametrize("word, n, expected", [("", 5, ''), ("", 0, '')])
def test_remove_chars_empty_string(word, n, expected):
    assert remove_chars(word, n) == expected

# Test edge case with `n` equal to zero
@pytest.mark.parametrize("word, n, expected", [("Hello, World!", 0, 'Hello, World!'), ("Python", 0, 'Python')])
def test_remove_chars_n_zero(word, n, expected):
    assert remove_chars(word, n) == expected

# Test edge case with `n` equal to the length of the string
@pytest.mark.parametrize("word, n, expected", [("Hello, World!", 13, ''), ("Python", 6, '')])
def test_remove_chars_n_length(word, n, expected):
    assert remove_chars(word, n) == expected

# Test edge case with `n` greater than the length of the string
@pytest.mark.parametrize("word, n, expected", [("Hello, World!", 15, ''), ("Python", 10, '')])
def test_remove_chars_n_greater_length(word, n, expected):
    assert remove_chars(word, n) == expected

# Test case with a string that contains special characters or non-ASCII characters
@pytest.mark.parametrize("word, n, expected", [("こんにちは, World!", 5, ', World!'), ("@#$%^&*()", 5, '&*()')])
def test_remove_chars_special_chars(word, n, expected):
    assert remove_chars(word, n) == expected

# Test case with a string that contains spaces
@pytest.mark.parametrize("word, n, expected", [("Hello World", 5, ' World'), ("  ", 1, ' ')])
def test_remove_chars_spaces(word, n, expected):
    assert remove_chars(word, n) == expected

# Test case with a string that contains numbers
@pytest.mark.parametrize("word, n, expected", [("1234567890", 5, '67890'), ("Python3", 6, '3')])
def test_remove_chars_numbers(word, n, expected):
    assert remove_chars(word, n) == expected