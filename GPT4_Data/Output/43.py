# imports
import pytest  # used for our unit tests
import string  # used in the function to test
import random  # used in the function to test

# function to test
def generateRandomPassword():
    """
    Generate a random Password which meets the following conditions
    Password length must be 10 characters long.
    It must contain at least 2 upper case letters, 1 digit, and 1 special symbol."""
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

# unit tests
def test_generateRandomPassword():
    # Test the function 100 times to check randomness and consistency
    for _ in range(100):
        password = generateRandomPassword()
        
        # Check password length
        assert len(password) == 10, "Password length must be 10 characters"
        
        # Check for at least 2 uppercase letters
        assert sum(1 for c in password if c.isupper()) >= 2, "Password must contain at least 2 uppercase letters"
        
        # Check for at least 1 digit
        assert sum(1 for c in password if c.isdigit()) >= 1, "Password must contain at least 1 digit"
        
        # Check for at least 1 special symbol
        assert any(c in string.punctuation for c in password), "Password must contain at least 1 special symbol"