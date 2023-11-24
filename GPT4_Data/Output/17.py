# imports
import pytest  # used for our unit tests

# function to test
def findRotations(str):
    # function to find the minimum number of rotations required to get the same string.
    tmp = str + str
    n = len(str)
 
    for i in range(1, n + 1):
        # substring from i index of 
        # original string size.
        substring = tmp[i: i+n]
 
        # if substring matches with 
        # original string then we will 
        # come out of the loop.
        if (str == substring):
            return i
    return n

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize(
    "input_str, expected_result",
    [
        # Scenario 1: The input string is empty
        ("", 0),
        # Scenario 2: The input string contains only one unique character
        ("aaaaa", 1),
        # Scenario 3: The input string contains all unique characters
        ("abcdef", 6),
        # Scenario 4: The input string contains repeated characters
        ("abcabc", 3),
        # Scenario 5: The input string contains special characters
        ("ab#c#ab#c", 4),
        # Scenario 6: The input string contains numbers
        ("12341234", 4),
        # Scenario 7: The input string is a palindrome
        ("radar", 5),
        # Scenario 8: The input string contains spaces
        ("abc abc", 4),
        # Edge Case 1: The input string contains non-printable characters
        ("\n\n", 1),
        ("\t\t\t", 1),
        # Edge Case 2: The input string contains unicode characters
        ("åå", 1),
        ("漢字漢字", 2),
        # Edge Case 3: The input string is extremely large
        ("a"*10**6, 1),
        ("ab"*10**6, 2),
        # Edge Case 4: The input string contains a mix of uppercase and lowercase letters
        ("AbcAbc", 3),
        ("ABCabcABCabc", 6),
        # Edge Case 5: The input string contains punctuation marks
        ("abc,abc,", 4),
        ("abc!abc!", 4),
    ]
)
def test_findRotations(input_str, expected_result):
    # Assert that the function findRotations returns the expected result for each test case
    assert findRotations(input_str) == expected_result