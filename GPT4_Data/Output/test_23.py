# imports
import pytest  # used for our unit tests
import io
import sys

# function to test
def printPrimeNumbersInRange(start, end):
    # Write a program to display all prime numbers within a range
    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):
        # all prime numbers are greater than 1
        # if number is less than or equal to 1, it is not prime
        if num > 1:
            for i in range(2, num):
                # check for factors
                if (num % i) == 0:
                    # not a prime number so break inner loop and
                    # look for next number
                    break
            else:
                print(num)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

# Helper function to capture print statements
def capture_print(func, *args):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    func(*args)
    sys.stdout = old_stdout
    return new_stdout.getvalue()

@pytest.mark.parametrize("start,end,expected", [
    (1, 10, "Prime numbers between 1 and 10 are:\n2\n3\n5\n7\n"),
    (10, 20, "Prime numbers between 10 and 20 are:\n11\n13\n17\n19\n"),
    (0, 1, "Prime numbers between 0 and 1 are:\n"),
    (24, 30, "Prime numbers between 24 and 30 are:\n"),
    (2, 2, "Prime numbers between 2 and 2 are:\n2\n"),
    (4, 4, "Prime numbers between 4 and 4 are:\n"),
    (100, 110, "Prime numbers between 100 and 110 are:\n101\n"),
    (-10, 10, "Prime numbers between -10 and 10 are:\n2\n3\n5\n7\n"),
    (-10, -1, "Prime numbers between -10 and -1 are:\n"),
    (10, 1, "Prime numbers between 10 and 1 are:\n"),
    (0, 0, "Prime numbers between 0 and 0 are:\n"),
    (-10, -5, "Prime numbers between -10 and -5 are:\n"),
])
def test_printPrimeNumbersInRange(start, end, expected):
    assert capture_print(printPrimeNumbersInRange, start, end) == expected

@pytest.mark.parametrize("start,end", [
    (1.5, 10),
    (10, 20.5),
    ("a", 10),
    (10, "b"),
    (1, 10**100),
    (10**100, 10**100 + 10),
    (float('inf'), 10),
    (10, float('inf')),
    (float('nan'), 10),
    (10, float('nan')),
])
def test_printPrimeNumbersInRange_invalid(start, end):
    with pytest.raises(TypeError):
        capture_print(printPrimeNumbersInRange, start, end)