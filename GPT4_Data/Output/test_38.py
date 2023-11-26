# imports
import pytest  # used for our unit tests

# function to test
def checkSameItems(tuple1):
    # Check if all items in the tuple are the same
    return all(i == tuple1[0] for i in tuple1)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("input_tuple, expected_result", [
    # Testing with tuples that contain all identical elements
    (('a', 'a', 'a'), True),
    ((1, 1, 1, 1), True),
    ((True, True, True), True),

    # Testing with tuples that contain different elements
    (('a', 'b', 'c'), False),
    ((1, 2, 3, 4), False),
    ((True, False, True), False),

    # Testing with tuples that contain only one element
    (('a',), True),
    ((1,), True),
    ((False,), True),

    # Testing with empty tuples
    ((), True),

    # Testing with tuples that contain elements of different types
    ((1, '1'), False),
    ((True, 'True'), False),
    ((1, 1.0), True),

    # Testing with nested tuples
    (((1, 1), (1, 1)), True),
    (((1, 2), (1, 2)), True),
    (((1, 2), (2, 1)), False),

    # Testing with tuples that contain None
    ((None, None, None), True),
    ((None, 'None'), False),
    ((None, 1), False),

    # Testing with tuples that contain Boolean and integer values
    ((1, True, True), True),
    ((0, False, False), True),
    ((1, True, 2), False),

    # Testing with tuples that contain mutable elements
    (([1, 2], [1, 2]), True),
    (([1, 2], [2, 1]), False),
    (({1: 'a'}, {1: 'a'}), True),

    # Testing with tuples that contain infinite or NaN values
    ((float('inf'), float('inf')), True),
    ((float('nan'), float('nan')), False),
])
def test_checkSameItems(input_tuple, expected_result):
    assert checkSameItems(input_tuple) == expected_result