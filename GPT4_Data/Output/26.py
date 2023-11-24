# imports
import pytest  # used for our unit tests
from io import StringIO  # used to capture the print output
import sys  # used to redirect the print output

# function to test
def printOddIndexNumbers(numlist):
    # set a loop to display elements from a given list present at odd index positions
    for i in numlist[1::2]:
        print(i, end=" ")

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "2 4 6 8 10 "),  # positive integers
    ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], "-2 -4 -6 -8 -10 "),  # negative integers
    ([1, -2, 3, -4, 5, -6, 7, -8, 9, -10], "-2 -4 -6 -8 -10 "),  # mix of positive and negative integers
    ([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10], "2.2 4.4 6.6 8.8 10.1 "),  # floating point numbers
    ([1], ""),  # single element
    ([], ""),  # empty list
    (['a', 'b', 'c', 'd', 'e'], "b d "),  # non-numeric elements
    ([1, 2], "2 "),  # only two elements
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], "1 2 3 4 5 "),  # duplicate elements
])
def test_printOddIndexNumbers(input_list, expected_output):
    # redirect stdout to a StringIO object
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # call the function with the current test input
    printOddIndexNumbers(input_list)

    # get the function's print output
    sys.stdout = old_stdout
    function_output = mystdout.getvalue()

    # assert that the function's output matches the expected output
    assert function_output == expected_output