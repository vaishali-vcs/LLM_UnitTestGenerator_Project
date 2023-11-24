# imports
import pytest  # used for our unit tests
import io
import sys

# function to test
def printMultiples(n, m):
    'takes n and m as integers and finds all first m multiples of n'
    for m in (n,m):
        if n % 2 == 0:
            while n < 0:
                print(n)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test with positive integers
@pytest.mark.parametrize("n, m, expected", [
    (5, 3, ""),  # The function currently has no return, so we expect an empty string
    (2, 4, "")
])
def test_positive_integers(n, m, expected):
    # Redirect stdout to a string stream to capture the print output of the function
    sys.stdout = io.StringIO()
    printMultiples(n, m)
    output = sys.stdout.getvalue().strip()
    assert output == expected

# Test with negative n and positive m
@pytest.mark.parametrize("n, m, expected", [
    (-3, 2, ""),
    (-7, 3, "")
])
def test_negative_n_positive_m(n, m, expected):
    sys.stdout = io.StringIO()
    printMultiples(n, m)
    output = sys.stdout.getvalue().strip()
    assert output == expected

# Test with zero n and positive m
@pytest.mark.parametrize("n, m, expected", [
    (0, 3, ""),
    (0, 5, "")
])
def test_zero_n_positive_m(n, m, expected):
    sys.stdout = io.StringIO()
    printMultiples(n, m)
    output = sys.stdout.getvalue().strip()
    assert output == expected

# Test with positive n and zero m
@pytest.mark.parametrize("n, m, expected", [
    (5, 0, ""),
    (2, 0, "")
])
def test_positive_n_zero_m(n, m, expected):
    sys.stdout = io.StringIO()
    printMultiples(n, m)
    output = sys.stdout.getvalue().strip()
    assert output == expected

# Test with large values for n and m
@pytest.mark.parametrize("n, m, expected", [
    (1000000, 1000000, "")
])
def test_large_values(n, m, expected):
    sys.stdout = io.StringIO()
    printMultiples(n, m)
    output = sys.stdout.getvalue().strip()
    assert output == expected

# Test with non-integer inputs
@pytest.mark.parametrize("n, m", [
    (2.5, 3),
    (3, 'four'),
    ('five', 3)
])
def test_non_integer_inputs(n, m):
    with pytest.raises(TypeError):
        printMultiples(n, m)