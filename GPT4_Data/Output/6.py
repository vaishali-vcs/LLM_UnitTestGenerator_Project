# imports
import pytest  # used for our unit tests

# function to test
def exp(num, power):
    """
    Returns the exponent of a given number with power
    """
    if power == 0:
        return 1
    if num == 0:
        return 0
    answer = num
    increment = num
    
    for i in range(1, power):
        for j in range(1, num):
            answer += increment
        increment = answer
    return answer

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("num, power, expected", [
    (2, 3, 8),  # positive integers
    (5, 4, 625),
    (0, 5, 0),  # base is zero
    (5, 0, 1),  # exponent is zero
    (0, 0, 1),  # base and exponent are zero
    (1, 5, 1),  # base is one
    (5, 1, 5),  # exponent is one
    (-2, 3, -8),  # negative base, positive exponent
    (-2, 2, 4),
    (2, -3, 0.125),  # positive base, negative exponent
    (10, 6, 1000000),  # large numbers
    (2, 10, 1024)
])
def test_exp(num, power, expected):
    assert exp(num, power) == expected