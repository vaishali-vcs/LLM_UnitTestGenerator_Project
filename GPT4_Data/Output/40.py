# imports
import pytest  # used for our unit tests
import random
import io
import sys
import re

# function to test
def generate3IntegersDivisibleBy5():
    # Generate 3 random integer number between 100 and 999 divisible by 5
    print("Generating 3 random integer number between 100 and 999 divisible by 5")
    for num in range(3):
        print(random.randrange(100, 999, 5), end=', ')

# unit tests
def test_generate3IntegersDivisibleBy5():
    # Redirect stdout to a string stream to capture the function's output
    stream = io.StringIO()
    sys.stdout = stream

    # Call the function
    generate3IntegersDivisibleBy5()

    # Get the function's output
    output = stream.getvalue()

    # Reset stdout to its normal value
    sys.stdout = sys.__stdout__

    # The output should contain 4 lines: the initial message and 3 numbers
    lines = output.split('\n')
    assert len(lines) == 4

    # The first line should be the initial message
    assert lines[0] == "Generating 3 random integer number between 100 and 999 divisible by 5"

    # The last line should be empty (because of the trailing newline)
    assert lines[3] == ""

    # The second line should contain 3 numbers separated by commas
    numbers_str = lines[1].split(', ')
    assert len(numbers_str) == 3

    # Each number should be an integer between 100 and 999 and divisible by 5
    for num_str in numbers_str:
        num = int(num_str)
        assert 100 <= num < 999
        assert num % 5 == 0