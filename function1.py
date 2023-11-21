def remove_chars(word, n):
    # Remove first n characters from a string
    print('Original string:', word)
    x = word[n:]
    return x

    
def checkPrime(max_num):
    """
    Check whether the given number is prime or not
    """
    for num in range (2, max_num):
        if max_num % num == 0:
            return False
        return True
    

def factorial(num):
    """
    Returns the factorial of a number
    """
    
    if num == 1:
        return num
    return num * factorial(num-1)



def cubesum(num):
    """
    Returns the sum of cube of each digit of a given number
    """
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += exp(digit, 3) # digit ** 3
        temp //= 10
        return sum


def prodDigit(num):
    """
    Returns the product of digits of given number
    """
    temp = num
    prod = 1
    while temp > 0:
        digit = temp % 10
        prod *= digit
        temp //= 10
        return prod



def is_palindrome(s):
    return s == s[::-1]
