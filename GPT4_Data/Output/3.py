# imports
import pytest  # used for our unit tests

# function to test
def factorial(num):
    """
    Returns the factorial of a number
    """
    if num == 1:
        return num
    return num * factorial(num-1)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Testing positive integer inputs
@pytest.mark.parametrize("num, result", [(5, 120), (3, 6)])
def test_positive_integers(num, result):
    assert factorial(num) == result

# Testing input of 1
def test_one():
    assert factorial(1) == 1

# Testing input of 0
def test_zero():
    assert factorial(0) == 1

# Testing negative integer inputs
def test_negative_integers():
    with pytest.raises(ValueError):
        factorial(-5)

# Testing non-integer inputs
def test_non_integer_inputs():
    with pytest.raises(TypeError):
        factorial(2.5)
    with pytest.raises(TypeError):
        factorial('a')

# Testing large integer inputs
def test_large_integers():
    # This test may fail due to recursion limit or memory constraints
    with pytest.raises(RecursionError):
        factorial(1000)