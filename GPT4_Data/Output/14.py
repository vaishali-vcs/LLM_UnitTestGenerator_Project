# imports
import pytest  # used for our unit tests
import math    # used for checking if a number is close to another

# function to test
def area_circle(radius):
    # Function to Compute the Area of a Circle
    pi = 3.14159
    area = pi * radius**2
    return area

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Testing with positive radius values
@pytest.mark.parametrize("radius, expected", [
    (1, 3.14159),
    (2, 12.56636),
    (5, 78.53975)
])
def test_positive_radius(radius, expected):
    assert math.isclose(area_circle(radius), expected, rel_tol=1e-5)

# Testing with zero radius
def test_zero_radius():
    assert area_circle(0) == 0

# Testing with negative radius values
@pytest.mark.parametrize("radius, expected", [
    (-1, 3.14159),
    (-2, 12.56636)
])
def test_negative_radius(radius, expected):
    assert math.isclose(area_circle(radius), expected, rel_tol=1e-5)

# Testing with non-integer radius values
@pytest.mark.parametrize("radius, expected", [
    (1.5, 7.06858),
    (3.2, 32.16991)
])
def test_float_radius(radius, expected):
    assert math.isclose(area_circle(radius), expected, rel_tol=1e-5)

# Testing with non-numeric radius values
@pytest.mark.parametrize("radius", [
    "one",
    [2]
])
def test_non_numeric_radius(radius):
    with pytest.raises(TypeError):
        area_circle(radius)

# Testing with extremely large radius values
def test_large_radius():
    assert area_circle(1e10) < float('inf')

# Testing with extremely small radius values
def test_small_radius():
    assert area_circle(1e-100) >= 0

# Testing with non-finite radius values
@pytest.mark.parametrize("radius", [
    float('inf'),
    float('nan')
])
def test_non_finite_radius(radius):
    with pytest.raises(ValueError):
        area_circle(radius)

# Testing with complex radius values
@pytest.mark.parametrize("radius", [
    1j,
    1+1j
])
def test_complex_radius(radius):
    with pytest.raises(TypeError):
        area_circle(radius)