# imports
import pytest  # used for our unit tests
import random  # used in our function
import re  # used to parse print output
from io import StringIO  # used to capture print output
import sys  # used to redirect print output

# function to test
def multiplyRandomNumbers():
    # Calculate multiplication of two random float numbers
    num1  = random.random()
    print("First Random float is ", num1)
    num2 = random.uniform(9.5, 99.5)
    print("Second Random float is ", num1)

    num3 = num1 * num2
    print("Multiplication is ", num3)

# unit tests
def test_multiplyRandomNumbers():
    # capture print statements
    capturedOutput = StringIO()
    sys.stdout = capturedOutput

    # call function
    multiplyRandomNumbers()

    # reset stdout
    sys.stdout = sys.__stdout__

    # parse print output
    output = capturedOutput.getvalue().split('\n')[:-1]
    num1 = float(re.search(r"[-+]?\d*\.\d+|\d+", output[0]).group())
    num2 = float(re.search(r"[-+]?\d*\.\d+|\d+", output[1]).group())
    num3 = float(re.search(r"[-+]?\d*\.\d+|\d+", output[2]).group())

    # check that num1 and num2 are in the correct ranges
    assert 0 <= num1 < 1
    assert 9.5 <= num2 <= 99.5

    # check that num3 is the product of num1 and num2
    assert num3 == pytest.approx(num1 * num2, 0.0001)  # allow for small floating point inaccuracies