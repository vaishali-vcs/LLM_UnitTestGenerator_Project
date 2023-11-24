# imports
import pytest  # used for our unit tests
from io import StringIO  # used to capture the output of the function
import sys  # used to redirect stdout

# function to test
def calculateCubes(input_number):
    # Calculate the cube of all numbers from 1 to a given number
    for i in range(1, input_number + 1):
        print("Current Number is :", i, " and the cube is", (i * i * i))

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Test with positive integer inputs
@pytest.mark.parametrize("input, output", [(3, "Current Number is : 1  and the cube is 1\nCurrent Number is : 2  and the cube is 8\nCurrent Number is : 3  and the cube is 27\n"), 
                                           (5, "Current Number is : 1  and the cube is 1\nCurrent Number is : 2  and the cube is 8\nCurrent Number is : 3  and the cube is 27\nCurrent Number is : 4  and the cube is 64\nCurrent Number is : 5  and the cube is 125\n")])
def test_calculateCubes_positive(input, output):
    # Redirect stdout to a string buffer
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    # Call the function and capture the output
    calculateCubes(input)
    assert mystdout.getvalue() == output

    # Reset stdout
    sys.stdout = old_stdout

# Test with zero input
def test_calculateCubes_zero():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    calculateCubes(0)
    assert mystdout.getvalue() == ""

    sys.stdout = old_stdout

# Test with negative integer input
def test_calculateCubes_negative():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    calculateCubes(-3)
    assert mystdout.getvalue() == ""

    sys.stdout = old_stdout

# Test with non-integer input
@pytest.mark.parametrize("input", [3.5, 'three'])
def test_calculateCubes_noninteger(input):
    with pytest.raises(TypeError):
        calculateCubes(input)

# Test with large integer input
def test_calculateCubes_large():
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    calculateCubes(1000000)
    assert len(mystdout.getvalue().split('\n')) == 1000001  # There should be 1,000,000 lines of output plus one extra line for the trailing newline

    sys.stdout = old_stdout