# imports
import pytest  # used for our unit tests

# function to test
def checkLeapYear(year):
    # Python program to check if year is a leap year or not

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return "{0} is a leap year".format(year)

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        return "{0} is a leap year".format(year)

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return "{0} is not a leap year".format(year)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("year, expected", [
    (2001, "2001 is not a leap year"),  # Regular year
    (2004, "2004 is a leap year"),  # Leap year
    (1900, "1900 is not a leap year"),  # Century year
    (2000, "2000 is a leap year"),  # Century leap year
    (-4, "-4 is a leap year"),  # BC year
    (1000000, "1000000 is a leap year"),  # Very large year
    (-1000000, "-1000000 is a leap year"),  # Very small year
])
def test_checkLeapYear(year, expected):
    assert checkLeapYear(year) == expected

@pytest.mark.parametrize("year", [
    2000.0,  # float
    "2000",  # string
])
def test_checkLeapYear_type_error(year):
    with pytest.raises(TypeError):
        checkLeapYear(year)

def test_checkLeapYear_no_input():
    with pytest.raises(TypeError):
        checkLeapYear()