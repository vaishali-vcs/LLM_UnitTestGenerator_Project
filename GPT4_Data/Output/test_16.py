# imports
import pytest  # used for our unit tests

# function to test
def find_square(num):
    # function to find square of a number
    result = num * num
    return result

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Testing with positive integers, negative integers, zero, and floating point numbers
@pytest.mark.parametrize("num, expected_result", [(2, 4), (10, 100), (-2, 4), (-10, 100), (0, 0), (1.5, 2.25), (-2.5, 6.25)])
def test_find_square_valid_inputs(num, expected_result):
    assert find_square(num) == expected_result

# Testing with large numbers
def test_find_square_large_number():
    assert find_square(1000000) == 1000000000000

# Testing edge case - maximum limit
def test_find_square_maximum_limit():
    assert find_square(1.8e308) == float('inf')  # Python represents infinity as float('inf')

# Testing with invalid inputs
@pytest.mark.parametrize("num", ['a', None])
def test_find_square_invalid_inputs(num):
    with pytest.raises(TypeError):
        find_square(num)