# imports
import pytest  # used for our unit tests

# function to test
def compute_tax(income):
    """Calculate income tax for the given income by adhering to the rules below
    0% tax for First $10,000. 10% for Next $10,000 and 20% for the remaining
    """
    tax_payable = 0

    if income <= 10000:
        tax_payable = 0
    elif income <= 20000:
        # no tax on first 10,000
        x = income - 10000
        # 10% tax
        tax_payable = x * 10 / 100
    else:
        # first 10,000
        tax_payable = 0

        # next 10,000 10% tax
        tax_payable = 10000 * 10 / 100

        # remaining 20%tax
        tax_payable += (income - 20000) * 20 / 100

    return tax_payable

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("income, expected", [
    (10000, 0),  # Scenario 1: Income is less than or equal to $10,000
    (0, 0),
    (5000, 0),
    (20000, 1000),  # Scenario 2: Income is more than $10,000 but less than or equal to $20,000
    (15000, 500),
    (10001, 0.1),
    (25000, 2000),  # Scenario 3: Income is more than $20,000
    (100000, 17000),
    (20001, 1000.2),
    (-5000, 0),  # Edge Case 1: Income is a negative number
    (1000000000, 199999800),  # Edge Case 2: Income is a very large number
    ("ten thousand", TypeError),  # Edge Case 3: Income is not a number
    (10000.50, 0),  # Scenario 5: Income is a float number
    (10000, 0),  # Scenario 5: Income is an integer
    (10000+0j, TypeError),  # Scenario 5: Income is a complex number
    ("10000", TypeError),  # Scenario 6: Income is a string
    (True, 0),  # Scenario 6: Income is a boolean
    (None, TypeError)  # Scenario 6: Income is None
])
def test_compute_tax(income, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            compute_tax(income)
    else:
        assert compute_tax(income) == expected