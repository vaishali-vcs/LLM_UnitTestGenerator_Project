# imports
import pytest  # used for our unit tests
import time

# function to test
import random
def getRandomDate(startDate, endDate ):
    # Generate a random date between given start and end dates
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator

@pytest.mark.parametrize("startDate, endDate", [
    ('01/01/2000', '12/31/2000'),  # Valid date range
    ('06/15/1985', '06/15/2025'),  # Valid date range
    ('12/25/2020', '12/25/2020'),  # Single day date range
    ('02/28/2020', '03/01/2020'),  # Leap year
    ('02/28/2021', '03/01/2021'),  # Non-leap year
])
def test_valid_dates(startDate, endDate):
    # Test that a valid random date is returned for valid inputs
    randomDate = getRandomDate(startDate, endDate)
    assert time.mktime(time.strptime(startDate, '%m/%d/%Y')) <= time.mktime(time.strptime(randomDate, '%m/%d/%Y')) <= time.mktime(time.strptime(endDate, '%m/%d/%Y'))

@pytest.mark.parametrize("startDate, endDate", [
    ('12/31/2020', '01/01/2020'),  # Invalid date range
    ('2020-12-31', '2021-01-01'),  # Invalid date format
    ('hello', 'world'),  # Non-date inputs
    ('', ''),  # Empty strings
    (123, 456),  # Non-string inputs
    (None, None),  # Null inputs
    ('01/01/2000 12:00', '12/31/2000 12:00'),  # Dates with time component
])
def test_invalid_dates(startDate, endDate):
    # Test that a ValueError is raised for invalid inputs
    with pytest.raises(ValueError):
        getRandomDate(startDate, endDate)