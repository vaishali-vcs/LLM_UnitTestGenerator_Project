# imports
import pytest  # used for our unit tests
import math

# function to test
def area_cylinder(radius,height):
    # Function to compute area of cylinder
    circle_area = math.pi * radius * radius
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test with positive inputs
@pytest.mark.parametrize("radius, height, expected", [
    (5, 10, 314.1592653589793),  # Expected: 2*π*5^2 + 2*π*5*10
    (3.14, 2.71, 78.95683520871486),  # Expected: 2*π*3.14^2 + 2*π*3.14*2.71
])
def test_positive_inputs(radius, height, expected):
    assert math.isclose(area_cylinder(radius, height), expected, rel_tol=1e-9)

# Test with zero inputs
@pytest.mark.parametrize("radius, height, expected", [
    (0, 10, 0),  # Expected: 2*π*0^2 + 2*π*0*10
    (5, 0, 50*math.pi),  # Expected: 2*π*5^2 + 2*π*5*0
])
def test_zero_inputs(radius, height, expected):
    assert math.isclose(area_cylinder(radius, height), expected, rel_tol=1e-9)

# Test with negative inputs
@pytest.mark.parametrize("radius, height", [
    (-5, 10),
    (5, -10),
])
def test_negative_inputs(radius, height):
    with pytest.raises(ValueError):  # Expect a ValueError because radius and height can't be negative
        area_cylinder(radius, height)

# Test with large inputs
@pytest.mark.parametrize("radius, height, expected", [
    (1e6, 1e6, 6.283185307179586e12),  # Expected: 2*π*(1e6)^2 + 2*π*(1e6)*(1e6)
])
def test_large_inputs(radius, height, expected):
    assert math.isclose(area_cylinder(radius, height), expected, rel_tol=1e-9)

# Test with small inputs
@pytest.mark.parametrize("radius, height, expected", [
    (1e-6, 1e-6, 6.283185307179586e-6),  # Expected: 2*π*(1e-6)^2 + 2*π*(1e-6)*(1e-6)
])
def test_small_inputs(radius, height, expected):
    assert math.isclose(area_cylinder(radius, height), expected, rel_tol=1e-9)

# Test with non-numeric inputs
@pytest.mark.parametrize("radius, height", [
    ('five', 10),
    (5, 'ten'),
])
def test_non_numeric_inputs(radius, height):
    with pytest.raises(TypeError):  # Expect a TypeError because radius and height must be numbers
        area_cylinder(radius, height)

# Test with no inputs
def test_no_inputs():
    with pytest.raises(TypeError):  # Expect a TypeError because the function requires two arguments
        area_cylinder()