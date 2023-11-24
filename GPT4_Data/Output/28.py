# imports
import pytest  # used for our unit tests

# function to test
def get_middle_three_chars(str1):
    # Create a string made of the middle three characters
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)
    return res

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("input_str,expected_output", [
    ("python", "tho"),  # Scenario 1
    ("hello", "ell"),  # Scenario 1
    ("cat", "cat"),  # Scenario 2
    ("dog", "dog"),  # Scenario 2
    ("abcd", "bc"),  # Scenario 3
    ("123456", "345"),  # Scenario 3
    ("a", "a"),  # Scenario 4
    ("", ""),  # Scenario 4
    ("12345", "234"),  # Scenario 5
    ("!@#$%^", "@#$"),  # Scenario 5
    ("I love Python", "ve "),  # Scenario 6
    ("The quick brown fox", "k b"),  # Scenario 6
    ("你好世界", "好世"),  # Scenario 7
    ("♠♥♦♣", "♥♦"),  # Scenario 7
    ("hello\nworld", "o\nw"),  # Edge Case 1
    ("abc\tdef", "c\t"),  # Edge Case 1
    ("a"*1000000 + "bcd" + "e"*1000000, "bcd"),  # Edge Case 2
    (" "*1000000 + "xyz" + " "*1000000, "xyz"),  # Edge Case 2
    ("\x00\x01\x02", "\x00\x01\x02"),  # Edge Case 3
    ("abc\x00def", "c\x00d")  # Edge Case 3
])
def test_get_middle_three_chars(input_str, expected_output):
    assert get_middle_three_chars(input_str) == expected_output

# Edge Case 4 and 5 are not included in the test cases as they are expected to raise a TypeError,
# which is outside the scope of the current function's responsibility.