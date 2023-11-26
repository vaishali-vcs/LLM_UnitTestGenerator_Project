# imports
import pytest  # used for our unit tests

# function to test
def concatenateLists(list1, list2):
    # Concatenate two lists index-wise
    list3 = [i + j for i, j in zip(list1, list2)]
    return list3  # modified the function to return the result instead of printing it

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("list1, list2, expected", [
    # Normal case
    (['a', 'b', 'c'], ['d', 'e', 'f'], ['ad', 'be', 'cf']),
    (['1', '2', '3'], ['4', '5', '6'], ['14', '25', '36']),
    # Empty lists
    ([], ['a', 'b', 'c'], []),
    (['a', 'b', 'c'], [], []),
    ([], [], []),
    # Lists of different lengths
    (['a', 'b'], ['1', '2', '3'], ['a1', 'b2']),
    (['a', 'b', 'c', 'd'], ['1', '2'], ['a1', 'b2']),
    # Lists containing special characters
    (['a$', 'b#', 'c@'], ['1', '2', '3'], ['a$1', 'b#2', 'c@3']),
    (['a', 'b', 'c'], ['1$', '2#', '3@'], ['a1$', 'b2#', 'c3@']),
    # Lists containing spaces
    (['a a', 'b b', 'c c'], ['1', '2', '3'], ['a a1', 'b b2', 'c c3']),
    (['a', 'b', 'c'], ['1 1', '2 2', '3 3'], ['a1 1', 'b2 2', 'c3 3'])
])
def test_concatenateLists(list1, list2, expected):
    assert concatenateLists(list1, list2) == expected

# Testing edge cases that should raise exceptions
@pytest.mark.parametrize("list1, list2", [
    # Lists containing non-string elements
    ([1, 2, 3], ['a', 'b', 'c']),
    (['a', 'b', 'c'], [1, 2, 3]),
    # Lists containing None
    (['a', 'b', None], ['1', '2', '3']),
    (['a', 'b', 'c'], ['1', None, '3']),
    ([None, None, None], ['1', '2', '3']),
    # Lists containing boolean values
    (['a', True, 'c'], ['1', '2', '3']),
    (['a', 'b', 'c'], ['1', False, '3']),
    # Lists containing other lists
    (['a', ['b', 'b'], 'c'], ['1', '2', '3']),
    (['a', 'b', 'c'], ['1', ['2', '2'], '3'])
])
def test_concatenateLists_exceptions(list1, list2):
    with pytest.raises(TypeError):
        concatenateLists(list1, list2)