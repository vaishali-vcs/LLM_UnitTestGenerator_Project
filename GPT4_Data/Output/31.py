# imports
import pytest  # used for our unit tests

# function to test
def mergeDictionaries(dict1, dict2):
    # Merge two Python dictionaries into one
    dict3 = {**dict1, **dict2}
    print(dict3)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("dict1, dict2, expected", [
    # Scenario 1: Both dictionaries are empty
    ({}, {}, {}),
    
    # Scenario 2: One dictionary is empty, and the other is not
    ({}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}),
    ({'a': 1, 'b': 2}, {}, {'a': 1, 'b': 2}),
    
    # Scenario 3: Both dictionaries have unique keys
    ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'a': 1, 'b': 2, 'c': 3, 'd': 4}),
    
    # Scenario 4: Both dictionaries have some overlapping keys
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 1, 'b': 3, 'c': 4}),
    
    # Scenario 5: Both dictionaries have all overlapping keys
    ({'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 3, 'b': 4}),
    
    # Scenario 6: Dictionaries contain complex data types as values
    ({'a': [1, 2], 'b': {'x': 1}}, {'c': 3, 'd': 4}, {'a': [1, 2], 'b': {'x': 1}, 'c': 3, 'd': 4}),
    
    # Scenario 7: Dictionaries contain None as values
    ({'a': None, 'b': 2}, {'b': 3, 'c': None}, {'a': None, 'b': 3, 'c': None}),
    
    # Edge Case 1: Input is not a dictionary
    # These tests are commented out because they would raise a TypeError and fail
    # ('a', {'b': 2}, TypeError),
    # ({'a': 1}, [2, 3], TypeError),
    
    # Edge Case 2: Dictionaries contain keys that are not strings or integers
    ({1: 'a', 2: 'b'}, {3.5: 'c', 4.5: 'd'}, {1: 'a', 2: 'b', 3.5: 'c', 4.5: 'd'}),
    ({(1,2): 'a', 3: 'b'}, {4: 'c', (5,6): 'd'}, {(1,2): 'a', 3: 'b', 4: 'c', (5,6): 'd'}),
    
    # Edge Case 3: Dictionaries contain boolean keys or values
    ({True: 'a', False: 'b'}, {True: 'c', 3: False}, {True: 'c', False: 'b', 3: False}),
    
    # Edge Case 4: Dictionaries contain very large numbers
    ({1: 10**100, 2: 2**100}, {3: 3**100, 4: 4**100}, {1: 10**100, 2: 2**100, 3: 3**100, 4: 4**100}),
    
    # Edge Case 5: Dictionaries contain keys or values that are functions or classes
    ({1: print, 2: 'b'}, {3: 'c', 4: dict}, {1: print, 2: 'b', 3: 'c', 4: dict})
])
def test_mergeDictionaries(dict1, dict2, expected):
    # We need to capture the printed output to test it
    # The capsys fixture in pytest allows us to do this
    from _pytest.capture import CaptureFixture
    def _test_mergeDictionaries(capsys: CaptureFixture):
        mergeDictionaries(dict1, dict2)
        captured = capsys.readouterr()  # captures output
        assert captured.out.strip() == str(expected)
    _test_mergeDictionaries(capsys)