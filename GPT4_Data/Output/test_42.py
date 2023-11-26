# imports
import pytest  # used for our unit tests
import random
import string

# function to test
def randomString(stringLength):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test the function with positive integer inputs
@pytest.mark.parametrize("input,expected", [(5, 5), (10, 10)])
def test_positive_integer(input, expected):
    assert len(randomString(input)) == expected

# Test the function with zero as input
def test_zero():
    assert randomString(0) == ""

# Test the function with negative integer inputs
def test_negative_integer():
    with pytest.raises(ValueError):
        randomString(-5)

# Test the function with non-integer inputs
@pytest.mark.parametrize("input", ["five", 5.0])
def test_non_integer(input):
    with pytest.raises(TypeError):
        randomString(input)

# Test the function with no input
def test_no_input():
    with pytest.raises(TypeError):
        randomString()

# Test the function with very large positive integer inputs
def test_large_positive_integer():
    with pytest.raises(MemoryError):
        randomString(1000000000)

# Test the function with non-numeric inputs
@pytest.mark.parametrize("input", [[1, 2, 3], {'length': 5}])
def test_non_numeric(input):
    with pytest.raises(TypeError):
        randomString(input)

# Test the function with None as input
def test_none():
    with pytest.raises(TypeError):
        randomString(None)

# Test the function with boolean inputs
@pytest.mark.parametrize("input", [True, False])
def test_boolean(input):
    with pytest.raises(TypeError):
        randomString(input)