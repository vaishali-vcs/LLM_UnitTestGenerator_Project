# imports
import pytest  # used for our unit tests

# function to test
def reverseNumbers(num):
    # Reverse a given integer number
    reverse_number = 0
    while num > 0:
        reminder = num % 10
        reverse_number = (reverse_number * 10) + reminder
        num = num // 10
    return reverse_number

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input,expected", [
    (123, 321),  # Test with positive integer
    (7, 7),  # Test with single digit
    (100, 1),  # Test with trailing zeros
    (12345678901234567890, 9876543210987654321),  # Test with large number
])
def test_reverseNumbers(input, expected):
    assert reverseNumbers(input) == expected

@pytest.mark.parametrize("input", [
    -123,  # Test with negative integer
    123.45,  # Test with float
    "123",  # Test with string
    None,  # Test with None
    True,  # Test with boolean
])
def test_reverseNumbers_errors(input):
    with pytest.raises(TypeError):
        reverseNumbers(input)