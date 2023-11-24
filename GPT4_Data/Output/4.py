# imports
import pytest  # used for our unit tests

# function to test
def first_last_same(numberList):
    # Check if the first and last number of a list is the same
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("numberList, expected", [
    # Scenario 1: The list contains positive integers
    ([1, 2, 3, 4, 5, 1], True),
    ([5, 4, 3, 2, 1], False),
    # Scenario 2: The list contains negative integers
    ([-1, -2, -3, -4, -1], True),
    ([-5, -4, -3, -2, -1], False),
    # Scenario 3: The list contains floating point numbers
    ([1.1, 2.2, 3.3, 1.1], True),
    ([1.1, 2.2, 3.3, 4.4], False),
    # Scenario 4: The list contains a mix of integers and floating point numbers
    ([1, 2.2, 3, 1], True),
    ([1.1, 2, 3.3, 4], False),
    # Scenario 5: The list contains only one element
    ([1], True),
    # Scenario 6: The list is empty
    ([], pytest.raises(IndexError)),
    # Scenario 7: The list contains non-numeric elements
    (['a', 'b', 'c', 'a'], True),
    ([1, 'b', 3, 1], True),
    # Edge cases
    ([True, False, True], True),
    ([True, True, False], False),
    ([None, 1, 2, None], True),
    ([None, 1, 2, 3], False),
    ([1+1j, 2+2j, 1+1j], True),
    ([1+1j, 2+2j, 3+3j], False),
    ([[1, 2], [3, 4], [1, 2]], True),
    ([[1, 2], [3, 4], [5, 6]], False),
    ([{'a': 1}, {'b': 2}, {'a': 1}], True),
    ([('a', 1), ('b', 2), ('c', 3)], False),
    ([1e100, 2, 3, 1e100], True),
    ([1e-100, 2, 3, 4], False)
])
def test_first_last_same(numberList, expected):
    if isinstance(expected, type) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            first_last_same(numberList)
    else:
        assert first_last_same(numberList) == expected