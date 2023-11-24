# imports
import pytest  # used for our unit tests

# function to test
def checkPrime(max_num):
    """
    Check whether the given number is prime or not
    """
    for num in range (2, max_num):
        if max_num % num == 0:
            return False
    return True

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input_value, expected_result", [
    (2, True),  # smallest prime number
    (7, True),  # prime number
    (13, True),  # another prime number
    (1, False),  # not considered a prime number
    (4, False),  # not a prime number
    (15, False),  # not a prime number
    (7919, True),  # large prime number
    (104729, True),  # another large prime number
    (10000, False),  # large non-prime number
    (999999, False),  # another large non-prime number
    (0, False),  # edge case: 0 is not a prime number
    (-7, False),  # edge case: negative number
])
def test_checkPrime(input_value, expected_result):
    assert checkPrime(input_value) == expected_result

# additional tests for edge cases that should raise errors
@pytest.mark.parametrize("input_value", [
    2.5,  # non-integer number
    'Hello',  # non-numeric input
    [2],  # non-numeric input
])
def test_checkPrime_error(input_value):
    with pytest.raises(TypeError):
        checkPrime(input_value)

def test_checkPrime_no_input():
    with pytest.raises(TypeError):
        checkPrime()  # no input