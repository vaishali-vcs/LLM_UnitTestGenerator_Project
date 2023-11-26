# imports
import pytest  # used for our unit tests

# function to test
def is_palindrome(s):
    return s == s[::-1]

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test for scenario 1: Empty strings
@pytest.mark.parametrize("test_input,expected", [("", True)])
def test_empty_string(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for scenario 2: Single-character strings
@pytest.mark.parametrize("test_input,expected", [("a", True)])
def test_single_character_string(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for scenario 3: Multi-character palindromes
@pytest.mark.parametrize("test_input,expected", [("aa", True), ("aba", True)])
def test_multi_character_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for scenario 4: Multi-character non-palindromes
@pytest.mark.parametrize("test_input,expected", [("ab", False), ("abc", False)])
def test_multi_character_non_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for scenario 5: Palindromes with spaces, punctuation, and mixed case
@pytest.mark.parametrize("test_input,expected", [("Able was I ere I saw Elba", False), ("A man, a plan, a canal, Panama", False)])
def test_palindrome_with_spaces_punctuation_and_mixed_case(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for scenario 6: Non-palindromes with spaces, punctuation, and mixed case
@pytest.mark.parametrize("test_input,expected", [("Hello, world", False), ("Python is fun", False)])
def test_non_palindrome_with_spaces_punctuation_and_mixed_case(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for edge case 1: Strings with non-alphanumeric characters
@pytest.mark.parametrize("test_input,expected", [("@#$%^^%$#@", True), ("12321...", False)])
def test_string_with_non_alphanumeric_characters(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for edge case 2: Strings with Unicode characters
@pytest.mark.parametrize("test_input,expected", [("あいういあ", True), ("あいうえお", False)])
def test_string_with_unicode_characters(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for edge case 3: Strings with mixed alphanumeric and non-alphanumeric characters
@pytest.mark.parametrize("test_input,expected", [("a..a", True), ("a..b", False)])
def test_string_with_mixed_alphanumeric_and_non_alphanumeric_characters(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for edge case 4: Strings with special whitespace characters
@pytest.mark.parametrize("test_input,expected", [("a\na", True), ("a\tb", False)])
def test_string_with_special_whitespace_characters(test_input, expected):
    assert is_palindrome(test_input) == expected

# Test for edge case 5: Case sensitivity and normalization
@pytest.mark.parametrize("test_input,expected", [("Aa", False), ("Nǐ hǎo, hǎo Nǐ", False)])
def test_case_sensitivity_and_normalization(test_input, expected):
    assert is_palindrome(test_input) == expected