# imports
import pytest  # used for our unit tests
from io import StringIO
import sys

# function to test
def setCommonElements(set1, set2):
    """ Check if two sets have any elements in common. If yes, display the common elements """
    if set1.isdisjoint(set2):
        print("Two sets have no items in common")
    else:
        print("Two sets have items in common")
        print(set1.intersection(set2))

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("set1, set2, expected_output", [
    # Scenario 1: The two sets have no elements in common.
    ({1, 2, 3}, {4, 5, 6}, "Two sets have no items in common\n"),
    ({'apple', 'banana', 'cherry'}, {'dog', 'elephant', 'fox'}, "Two sets have no items in common\n"),
    ({True, False}, {None}, "Two sets have no items in common\n"),

    # Scenario 2: The two sets have some elements in common.
    ({1, 2, 3}, {2, 3, 4}, "Two sets have items in common\n{2, 3}\n"),
    ({'apple', 'banana', 'cherry'}, {'banana', 'cherry', 'dog'}, "Two sets have items in common\n{'banana', 'cherry'}\n"),
    ({True, False}, {False, None}, "Two sets have items in common\n{False}\n"),

    # Scenario 3: One or both sets are empty.
    ({}, {1, 2, 3}, "Two sets have no items in common\n"),
    ({1, 2, 3}, {}, "Two sets have no items in common\n"),
    ({}, {}, "Two sets have no items in common\n"),

    # Scenario 4: The two sets are identical.
    ({1, 2, 3}, {1, 2, 3}, "Two sets have items in common\n{1, 2, 3}\n"),
    ({'apple', 'banana', 'cherry'}, {'apple', 'banana', 'cherry'}, "Two sets have items in common\n{'apple', 'banana', 'cherry'}\n"),
    ({True, False}, {True, False}, "Two sets have items in common\n{False, True}\n"),
])
def test_setCommonElements(set1, set2, expected_output):
    # Redirect stdout to a buffer
    sys.stdout = StringIO()
    # Call the function, which will print to the buffer instead of stdout
    setCommonElements(set1, set2)
    # Get the current value of the buffer and reset stdout
    got_output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    # Check the output against the expected output
    assert got_output == expected_output