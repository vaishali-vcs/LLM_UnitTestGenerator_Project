# imports
import pytest  # used for our unit tests

# function to test
def reverseTuple(tuple1):
    # Reverse the tuple
    tuple1 = tuple1[::-1]
    return tuple1

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("input_tuple, expected_output", [
    # Testing with a tuple of integers
    ((1, 2, 3, 4, 5), (5, 4, 3, 2, 1)),
    ((1, 2, 2, 3, 3, 3), (3, 3, 3, 2, 2, 1)),
    ((-1, 2, -3, 4, -5), (-5, 4, -3, 2, -1)),
    # Testing with a tuple of strings
    (('a', 'b', 'c'), ('c', 'b', 'a')),
    (('hello', 'world'), ('world', 'hello')),
    (('Hello', 'WORLD', 'Python'), ('Python', 'WORLD', 'Hello')),
    # Testing with a tuple of mixed data types
    ((1, 'a', 2, 'b'), ('b', 2, 'a', 1)),
    ((1, 'a', 2.0, 'b'), ('b', 2.0, 'a', 1)),
    # Testing with edge cases
    ((), ()),
    ((1,), (1,)),
    ((1, 1), (1, 1)),
    # Testing with non-tuple inputs
    ('abc', 'cba'),
    ([1, 2, 3], [3, 2, 1]),
    # Testing with tuples of tuples
    (((1, 2), (3, 4)), ((3, 4), (1, 2))),
    # Testing with tuples containing mutable elements
    ((1, [2, 3]), ([2, 3], 1)),
    # Testing with tuples containing None
    ((1, None), (None, 1)),
    ((None, None), (None, None)),
    # Testing with tuples containing boolean values
    ((True, False), (False, True)),
    ((True, True), (True, True)),
])
def test_reverseTuple(input_tuple, expected_output):
    assert reverseTuple(input_tuple) == expected_output