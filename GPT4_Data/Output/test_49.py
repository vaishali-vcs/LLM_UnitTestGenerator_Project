# imports
import pytest  # used for our unit tests
from string import ascii_lowercase as asc_lower
from io import StringIO
import sys

# function to test
def checkPangram(s):
    # check if a sentence contains all the letters in the English alphabet.
    if set(asc_lower) - set(s.lower()) == set([]):
        print("The string is a pangram")
    else:
         print("The string is not a pangram")

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# The function should print "The string is a pangram" when the input string is a pangram
@pytest.mark.parametrize("input_str, expected_output", [
    ("The quick brown fox jumps over the lazy dog", "The string is a pangram\n"),
    ("Pack my box with five dozen liquor jugs", "The string is a pangram\n"),
    ("How vexingly quick daft zebras jump", "The string is a pangram\n"),
    ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "The string is a pangram\n"),
    ("The quick brown fox jumps over the lazy dog!", "The string is a pangram\n"),
    ("The quick brown fox jumps over the lazy dog. The lazy dog is tired.", "The string is a pangram\n"),
    ("Hello world", "The string is not a pangram\n"),
    ("Python is fun", "The string is not a pangram\n"),
    ("I love programming", "The string is not a pangram\n"),
    ("", "The string is not a pangram\n"),
    ("aaaaaaaaaaa", "The string is not a pangram\n"),
    ("     ", "The string is not a pangram\n"),
])

def test_checkPangram(input_str, expected_output):
    # Redirect stdout to a StringIO object
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the function with the test input
    checkPangram(input_str)

    # Get the function's output from stdout
    actual_output = sys.stdout.getvalue()

    # Reset stdout
    sys.stdout = old_stdout

    # Assert that the actual output matches the expected output
    assert actual_output == expected_output