# imports
import pytest  # used for our unit tests

# function to test
def cubesum(num):
    """
    Returns the sum of cube of each digit of a given number
    """
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input,expected", [
    (123, 36),  # testing with positive integer
    (999, 2187),  # testing with positive integer
    (1, 1),  # testing with single digit number
    (9, 729),  # testing with single digit number
    (0, 0),  # testing with zero
])
def test_cubesum(input, expected):
    assert cubesum(input) == expected

@pytest.mark.parametrize("input", [
    -123,  # testing with negative number
    12.3,  # testing with non-integer number
    '123',  # testing with non-numeric input
    [1, 2, 3],  # testing with non-numeric input
])
def test_cubesum_invalid_input(input):
    with pytest.raises(Exception):
        cubesum(input)