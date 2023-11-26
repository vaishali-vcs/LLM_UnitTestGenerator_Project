# imports
import pytest  # used for our unit tests

# function to test
def generateArmstrongNumbers(lower, upper):
    """
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    """
    armstrong_numbers = []  # to store Armstrong numbers
    for num in range(lower,upper + 1):
       sum = 0
       temp = num
       while temp > 0:
           digit = temp % 10
           sum += digit ** 3
           temp //= 10
           if num == sum:
                armstrong_numbers.append(num)  # append Armstrong number to the list
    return armstrong_numbers  # return the list of Armstrong numbers

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("lower,upper,expected", [
    (1, 10, [1]),  # testing with small numbers
    (100, 1000, [153, 370, 371, 407]),  # testing with larger numbers
    (-10, 10, [0, 1]),  # testing with negative and positive numbers
    (5, 5, []),  # testing with lower and upper being the same number
    (10, 5, []),  # testing with lower being greater than upper
    (0, 0, [0]),  # testing with lower and upper being zero
    (1, 500, [1, 153, 370, 371, 407]),  # testing with known Armstrong numbers
    (2, 9, []),  # testing with no Armstrong numbers
    (-10, -1, []),  # testing with negative numbers
])
def test_generateArmstrongNumbers(lower, upper, expected):
    assert generateArmstrongNumbers(lower, upper) == expected