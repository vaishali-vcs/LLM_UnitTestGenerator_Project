# imports
import pytest  # used for our unit tests

# function to test
def sumOfList(list, size):
    # find sum of all elements in list using recursion
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("list, size, expected", [
    # Normal list of numbers
    ([1, 2, 3, 4, 5], 5, 15),
    ([10, 20, 30, 40, 50], 5, 150),
    # List with negative numbers
    ([-1, -2, -3, -4, -5], 5, -15),
    ([10, -20, 30, -40, 50], 5, 30),
    # List with floating point numbers
    ([1.1, 2.2, 3.3, 4.4, 5.5], 5, 16.5),
    ([10.5, 20.5, 30.5, 40.5, 50.5], 5, 152.5),
    # List with only one element
    ([5], 1, 5),
    ([-10], 1, -10),
    # Empty list
    ([], 0, 0),
    # List with zero
    ([0, 1, 2, 3, 4], 5, 10),
    ([0, 0, 0, 0, 0], 5, 0),
    # List with large numbers
    ([1000000, 2000000, 3000000], 3, 6000000),
    ([-1000000, 2000000, -3000000], 3, -2000000),
    # List with large number of elements
    ([1]*1000, 1000, 1000),
    ([-1]*10000, 10000, -10000)
])
def test_sumOfList(list, size, expected):
    assert sumOfList(list, size) == expected

# Edge cases
@pytest.mark.parametrize("list, size", [
    # List with non-numeric values
    (['a', 'b', 'c'], 3),
    ([1, 2, '3', 4, 5], 5),
    # List with None values
    ([None, None, None], 3),
    ([1, 2, None, 4, 5], 5),
    # Size parameter is not an integer
    ([1, 2, 3, 4, 5], '5'),
    ([1, 2, 3, 4, 5], 5.0),
    # Size parameter is negative
    ([1, 2, 3, 4, 5], -5),
    # Size parameter is larger than the actual size of the list
    ([1, 2, 3, 4, 5], 10)
])
def test_sumOfList_edge_cases(list, size):
    with pytest.raises(TypeError):
        sumOfList(list, size)