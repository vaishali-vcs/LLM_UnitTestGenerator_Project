# imports
import pytest  # used for our unit tests

# function to test
def power(a,b):
  # a function to calculate power of a number raised to other. 
  if b == 1:
    return a
  else:
    return a*power(a,b-1)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),  # Positive integer powers
    (10, 4, 10000),  # Positive integer powers
    (2, 0, 1),  # Power of 0
    (100, 0, 1),  # Power of 0
    (2, 1, 2),  # Power of 1
    (100, 1, 100),  # Power of 1
    (0, 2, 0),  # Base of 0
    (0, 5, 0),  # Base of 0
    (0, 0, 1),  # Edge case: 0 to the power of 0
])
def test_power(a, b, expected):
    assert power(a, b) == expected