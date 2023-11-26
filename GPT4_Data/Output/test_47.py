# imports
import pytest  # used for our unit tests

# function to test
def checkTriangle(x, y, z):
    """
    Determine if a triangle is equilateral, isosceles, or scalene.
    An equilateral triangle has all three sides the same length.   
    An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
    A scalene triangle has all sides of different lengths.
    """
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or z == x:
        return "isosceles triangle"
    else:
        return "Scalene triangle"

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("x, y, z, expected", [
    (1, 1, 1, "Equilateral triangle"),  # Testing with equilateral triangles
    (3.5, 3.5, 3.5, "Equilateral triangle"),  # Testing with floating point numbers
    (2, 2, 3, "isosceles triangle"),  # Testing with isosceles triangles
    (3, 4, 3, "isosceles triangle"),  # Testing with isosceles triangles, not the first two parameters
    (5.5, 6.5, 5.5, "isosceles triangle"),  # Testing with floating point numbers
    (2, 3, 4, "Scalene triangle"),  # Testing with scalene triangles
    (3.1, 4.2, 5.3, "Scalene triangle"),  # Testing with floating point numbers
    (1e100, 1e100, 1e100, "Equilateral triangle"),  # Testing with extremely large numbers
    (1e-100, 1e-100, 1e-100, "Equilateral triangle"),  # Testing with extremely small numbers
    (1, 2, 3, "Scalene triangle"),  # Testing with non-triangle inputs
])
def test_checkTriangle(x, y, z, expected):
    assert checkTriangle(x, y, z) == expected