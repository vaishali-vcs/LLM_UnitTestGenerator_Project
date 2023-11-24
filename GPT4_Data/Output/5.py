# imports
import pytest  # used for our unit tests
from io import StringIO  # used to capture printed output
import sys  # used to redirect standard output

# function to test
def extract_number(number):
    # Write a Program to extract each digit from an integer in the reverse order.
    print("Given number", number)
    while number > 0:
        # get the last digit
        digit = number % 10
        # remove the last digit and repeat the loop
        number = number // 10
        print(digit, end=" ")

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("input_number, expected_output", [
    (1234, "Given number 1234\n4 3 2 1 "),
    (9876543210, "Given number 9876543210\n0 1 2 3 4 5 6 7 8 9 "),
    (0, "Given number 0\n"),
    (5, "Given number 5\n5 "),
    (1000000001, "Given number 1000000001\n1 0 0 0 0 0 0 0 0 1 "),
])
def test_extract_number(input_number, expected_output):
    # Redirect standard output to a string buffer
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the function and capture the output
    extract_number(input_number)
    output = sys.stdout.getvalue()

    # Restore standard output
    sys.stdout = old_stdout

    # Assert that the function's output matches the expected output
    assert output == expected_output