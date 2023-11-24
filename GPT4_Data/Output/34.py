# imports
import pytest  # used for our unit tests

# function to test
def remove_value(sample_list, val):
    #Remove all occurrences of a specific item from a list.
    return [i for i in sample_list if i != val]

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("sample_list,val,expected", [
    # Scenario 1: Regular use case with a list containing multiple instances of the value to be removed
    ([1, 2, 3, 2, 4, 2, 5], 2, [1, 3, 4, 5]),
    (['a', 'b', 'a', 'c', 'a', 'd'], 'a', ['b', 'c', 'd']),
    # Scenario 2: List contains no instances of the value to be removed
    ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
    (['apple', 'banana', 'cherry'], 'orange', ['apple', 'banana', 'cherry']),
    # Scenario 3: List contains only instances of the value to be removed
    ([2, 2, 2, 2, 2], 2, []),
    (['a', 'a', 'a', 'a'], 'a', []),
    # Scenario 4: List is empty
    ([], 1, []),
    ([], 'a', []),
    # Scenario 5: List contains different data types
    ([1, '1', 1.0, '1.0'], 1, ['1', '1.0']),
    ([True, 'True', 1, '1'], True, ['True', '1']),
    # Scenario 6: Edge case with None value
    ([1, 2, 3, None, 4, 5], None, [1, 2, 3, 4, 5]),
    ([None, None, None], None, []),
    # Scenario 7: List contains nested lists
    ([1, 2, [3, 4], 5], [3, 4], [1, 2, 5]),
    (['a', 'b', ['c', 'd'], 'e'], ['c', 'd'], ['a', 'b', 'e']),
    # Edge cases
    ([[1, 2], [3, 4], [1, 2]], [1, 2], [[3, 4]]),
    ([{'a': 1}, {'b': 2}, {'a': 1}], {'a': 1}, [{'b': 2}]),
    ([True, False, True, False], 1, [False, False]),
    ([True, False, True, False], 0, [True, True]),
    ([1+2j, 2+3j, 1+2j], 1+2j, [2+3j]),
    ([1+2j, 2+3j, 1+2j], 2+3j, [1+2j, 1+2j])
])
def test_remove_value(sample_list, val, expected):
    assert remove_value(sample_list, val) == expected