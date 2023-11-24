# imports
import pytest  # used for our unit tests

# function to test
def exponent(base, exp):
    # Write a function that returns an int value of base raises to the power of exp.
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    return result

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("base, exp, expected", [
    (2, 3, 8),  # Positive integer base and exponent
    (1, 100, 1),  # Base is 1
    (100, 0, 1),  # Exponent is 0
    (0, 5, 0),  # Base is 0
    (-2, 3, -8),  # Negative base and positive exponent
    (-3, 2, 9),  # Negative base and positive exponent
    (2.5, 3, 15.625),  # Floating point base and integer exponent
])
def test_exponent(base, exp, expected):
    assert exponent(base, exp) == expected

@pytest.mark.parametrize("base, exp", [
    (2, -3),  # Positive base and negative exponent
    (-2, -3),  # Negative base and negative exponent
    (0, 0),  # Base and exponent are both 0
    (2, 1.5),  # Integer base and floating point exponent
    (2, 10000),  # Exponent is a large number
    ('a', 2),  # Base or exponent is not a number
    (2, 'a'),  # Base or exponent is not a number
    (None, 2),  # Base or exponent is None
    (2, None),  # Base or exponent is None
    (True, 2),  # Base or exponent is a boolean
    (2, False),  # Base or exponent is a boolean
    (-2, 1/2),  # Base is a negative number and exponent is a fraction
])
def test_exponent_edge_cases(base, exp):
    with pytest.raises(Exception):
        exponent(base, exp)