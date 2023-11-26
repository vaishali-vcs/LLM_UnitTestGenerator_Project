# imports
import pytest  # used for our unit tests

# function to test
def UpdateSet(set1, set2):
    # Update set1 by adding items from set2, except common items
    set1.intersection_update(set2)
    return set1

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("set1, set2, expected", [
    # Scenario 1: Both sets are empty
    (set(), set(), set()),
    # Scenario 2: One set is empty, and the other set has elements
    (set(), {1, 2, 3}, set()),
    ({1, 2, 3}, set(), set()),
    # Scenario 3: Both sets have elements, and there are no common elements between the sets
    ({1, 2, 3}, {4, 5, 6}, set()),
    # Scenario 4: Both sets have elements, and there are some common elements between the sets
    ({1, 2, 3}, {2, 3, 4}, {2, 3}),
    # Scenario 5: Both sets have elements, and all elements are common between the sets
    ({1, 2, 3}, {1, 2, 3}, {1, 2, 3}),
    # Scenario 6: Both sets have elements, and one set is a subset of the other
    ({1, 2, 3, 4}, {2, 3}, {2, 3}),
    ({2, 3}, {1, 2, 3, 4}, {2, 3}),
    # Scenario 7: Both sets have elements, and the sets contain different data types
    ({1, 2, 3}, {"a", "b", "c"}, set()),
    ({1, 2, 3}, {1.1, 2.2, 3.3}, set()),
    # Scenario 8: Both sets have elements, and the sets contain complex data types like tuples
    ({(1, 2), (3, 4)}, {(5, 6), (7, 8)}, set()),
    ({(1, 2), (3, 4)}, {(1, 2), (7, 8)}, {(1, 2)}),
])
def test_UpdateSet(set1, set2, expected):
    assert UpdateSet(set1, set2) == expected