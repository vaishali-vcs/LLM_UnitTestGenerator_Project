# imports
import pytest  # used for our unit tests
import math  # used for special floating point values

# function to test
def addNumbers(x, y):
    # function that accepts two numbers as arguments and returns the sum
    sum = x + y
    return sum

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("x, y, expected", [
    # Testing with positive integers
    (3, 2, 5),
    (100, 200, 300),
    # Testing with negative integers
    (-3, -2, -5),
    (-100, 200, 100),
    # Testing with zero
    (0, 0, 0),
    (0, 5, 5),
    (-5, 0, -5),
    # Testing with floating point numbers
    (1.5, 2.5, 4.0),
    (-1.5, 0.5, -1.0),
    # Testing with large numbers
    (1e6, 2e6, 3e6),
    (-1e6, 1e6, 0),
    # Edge cases
    (float('inf'), 1, float('inf')),
    (float('-inf'), -1, float('-inf')),
    (float('inf'), float('-inf'), float('nan')),
    (float('nan'), 1, float('nan')),
    # Testing with boolean inputs
    (True, False, 1),
    (True, 1, 2),
    (False, 0, 0),
    # Testing with complex numbers
    ((1+2j), (2+3j), (3+5j)),
    ((1+2j), (-1-2j), 0)
])
def test_addNumbers(x, y, expected):
    # pytest.approx is used to compare floating point numbers for equality
    assert addNumbers(x, y) == pytest.approx(expected)

# Testing with non-numeric and None inputs, which should raise TypeError
@pytest.mark.parametrize("x, y", [
    ('3', 2),
    ([1, 2], 3),
    (None, 1),
    (None, None)
])
def test_addNumbers_type_error(x, y):
    with pytest.raises(TypeError):
        addNumbers(x, y)