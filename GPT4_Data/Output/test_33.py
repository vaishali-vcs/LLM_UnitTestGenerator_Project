# imports
import pytest  # used for our unit tests

# function to test
def turnItemtoSquare(numbers):
    # Turn every item of a list into its square
    res = []
    for i in numbers:
        # calculate square and add to the result list
        res.append(i * i)
    return res  # Modified to return the result instead of printing it

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize(
    "input,expected_output", 
    [
        # Testing with positive integers
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
        # Testing with negative integers
        ([-1, -2, -3, -4, -5], [1, 4, 9, 16, 25]),
        # Testing with zero
        ([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25]),
        # Testing with floating point numbers
        ([1.1, 2.2, 3.3, 4.4, 5.5], [1.21, 4.84, 10.89, 19.36, 30.25]),
        # Testing with empty list
        ([], []),
        # Testing with single-item list
        ([1], [1]),
        # Testing with large numbers
        ([1000000000, 2000000000, 3000000000], [1000000000000000000, 4000000000000000000, 9000000000000000000]),
    ]
)
def test_turnItemtoSquare(input, expected_output):
    # Assert that the function's output is as expected
    assert turnItemtoSquare(input) == expected_output