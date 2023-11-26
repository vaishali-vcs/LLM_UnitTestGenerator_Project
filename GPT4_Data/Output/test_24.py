# imports
import pytest  # used for our unit tests
from io import StringIO  # used to capture the output of the function
import sys  # used to redirect the standard output

# function to test
def fibonacci(nrange=2):
    # Display Fibonacci series
    # first two numbers
    num1, num2 = 0, 1

    print("Fibonacci sequence:")
    # run loop 10 times
    for i in range(nrange):
        # print next number of a series
        print(num1, end="  ")
        # add last two numbers to get next number
        res = num1 + num2

        # update values
        num1 = num2
        num2 = res

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input_value, expected_output", [
    (2, "Fibonacci sequence:\n0  1  "),  # Testing with default argument
    (5, "Fibonacci sequence:\n0  1  1  2  3  "),  # Testing with positive integers
    (0, "Fibonacci sequence:\n"),  # Testing with zero
])
def test_fibonacci(input_value, expected_output):
    # Redirect standard output to a buffer
    stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the function with the test input
    fibonacci(input_value)

    # Get the function output from the buffer
    function_output = sys.stdout.getvalue()

    # Reset standard output
    sys.stdout = stdout

    # Assert that the function output matches the expected output
    assert function_output == expected_output

@pytest.mark.parametrize("input_value", [
    -1,  # Testing with negative integers
    'five',  # Testing with non-integer arguments
    5.5,  # Testing with decimal numbers
    float('nan'),  # Testing with special numeric values
    float('inf'),  # Testing with special numeric values
])
def test_fibonacci_edge_cases(input_value):
    # Redirect standard output to a buffer
    stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the function with the test input
    fibonacci(input_value)

    # Get the function output from the buffer
    function_output = sys.stdout.getvalue()

    # Reset standard output
    sys.stdout = stdout

    # Assert that the function output matches the expected output for edge cases
    assert function_output == "Fibonacci sequence:\n"