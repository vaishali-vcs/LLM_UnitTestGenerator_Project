# imports
import pytest  # used for our unit tests

# function to test
def prodDigit(num):
    """
    Returns the product of digits of given number
    """
    temp = num
    prod = 1
    while temp > 0:
        digit = temp % 10
        prod *= digit
        temp //= 10
    return prod

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test positive integers with multiple digits
@pytest.mark.parametrize("num, expected", [(123, 6), (456, 120)])
def test_positive_multi_digit(num, expected):
    assert prodDigit(num) == expected

# Test positive integers with a single digit
@pytest.mark.parametrize("num, expected", [(7, 7), (0, 1)])
def test_positive_single_digit(num, expected):
    assert prodDigit(num) == expected

# Test positive integers with one or more zeros in them
@pytest.mark.parametrize("num, expected", [(101, 0), (2003, 0)])
def test_positive_with_zeros(num, expected):
    assert prodDigit(num) == expected

# Test numbers with trailing zeros
@pytest.mark.parametrize("num, expected", [(100, 0), (7000, 0)])
def test_trailing_zeros(num, expected):
    assert prodDigit(num) == expected

# Test the number zero itself
@pytest.mark.parametrize("num, expected", [(0, 1)])
def test_zero(num, expected):
    assert prodDigit(num) == expected

# Test very large numbers
@pytest.mark.parametrize("num, expected", [(12345678901234567890, 0)])
def test_large_numbers(num, expected):
    assert prodDigit(num) == expected