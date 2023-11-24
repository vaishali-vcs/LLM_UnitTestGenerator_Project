def extract_number(number):
    # Write a Program to extract each digit from an integer in the reverse order.
    print("Given number", number)
    while number > 0:
        # get the last digit
        digit = number % 10
        # remove the last digit and repeat the loop
        number = number // 10
        print(digit, end=" ")


def compute_tax(income):
    """Calculate income tax for the given income by adhering to the rules below
    0% tax for First $10,000. 10% for Next $10,000 and 20% for the remaining
    """

    print("Given income", income)
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

    print("Total tax to pay is", tax_payable)


def printPrimeNumbersInRange(start, end):
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


def fibonacci(nrange=2):
    # first two numbers
    num1, num2 = 0, 1

    print("Fibonacci sequence:")
    # run loop 10 times
    for i in range(nrange):
        # print next number of a series
        print(num1, end="  ")
        # add last two numbers to get next number
        res = num1 + num2

        # update values
        num1 = num2
        num2 = res


def reverseNumbers(num):
    reverse_number = 0
    print("Given Number ", num)
    while num > 0:
        reminder = num % 10
        reverse_number = (reverse_number * 10) + reminder
        num = num // 10
    print("Reverse Number ", reverse_number)


def printOddIndexNumbers(numlist):
    for i in numlist[1::2]:
        print(i, end=" ")


def calculateCubes(input_number):
    # Calculate the cube of all numbers from 1 to a given number
    for i in range(1, input_number + 1):
        print("Current Number is :", i, " and the cube is", (i * i * i))


def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)


def createMixString(s1, s2):
    """
    Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
    then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars
    go at the end of the result."""
    # get string length
    s1_length = len(s1)
    s2_length = len(s2)

    # get length of a bigger string
    length = s1_length if s1_length > s2_length else s2_length
    result = ""

    # reverse s2
    s2 = s2[::-1]

    # iterate string
    # s1 ascending and s2 descending
    for i in range(length):
        if i < s1_length:
            result = result + s1[i]
        if i < s2_length:
            result = result + s2[i]

    print(result)


def mergeDictionaries(dict1, dict2):
    dict3 = {**dict1, **dict2}
    print(dict3)

def concatenateLists(list1, list2):
    list3 = [i + j for i, j in zip(list1, list2)]
    print(list3)

def turnItemtoSquare(numbers):
    # result list
    res = []
    for i in numbers:
        # calculate square and add to the result list
        res.append(i * i)
    print(res)

def setCommonElements(set1, set2):
    if set1.isdisjoint(set2):
        print("Two sets have no items in common")
    else:
        print("Two sets have items in common")
        print(set1.intersection(set2))

def UpdateSet(set1, set2):
    # Update set1 by adding items from set2, except common items
    set1.intersection_update(set2)
    print(set1)

def reverseTuple(tuple1):
    # Reverse the tuple
    tuple1 = tuple1[::-1]
    print(tuple1)

def checkSameItems(tuple1):
    # Check if all items in the tuple are the same
    print(all(i == tuple1[0] for i in tuple1))

import random
def RandomLotteryPicker():
    lottery_tickets_list = []
    print("creating 100 random lottery tickets")
    # to get 100 ticket
    for i in range(100):
        # ticket number must be 10 digit (1000000000, 9999999999)
        lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
    # pick 2 luck tickets
    winners = random.sample(lottery_tickets_list, 2)
    print("Lucky 2 lottery tickets are", winners)

import random
def generate3IntegersDivisibleBy5():
    # Generate 3 random integer number between 100 and 999 divisible by 5
    print("Generating 3 random integer number between 100 and 999 divisible by 5")
    for num in range(3):
        print(random.randrange(100, 999, 5), end=', ')

def pickRandomChar(name):
    #Pick a random character from a given String
    char = random.choice(name)
    print("random char is ", char)

import random
import string

def randomString(stringLength):
    """Generate a random string of 5 charcters"""
    letters = string.ascii_letters
    print(''.join(random.choice(letters) for i in range(stringLength)))

import random
import string

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
    print(password)

import random

def multiplyRandomNumbers():
    # Calculate multiplication of two random float numbers
    num1  = random.random()
    print("First Random float is ", num1)
    num2 = random.uniform(9.5, 99.5)
    print("Second Random float is ", num1)

    num3 = num1 * num2
    print("Multiplication is ", num3)

import random
import time

def getRandomDate(startDate, endDate ):
    # Generate a random date between given start and end dates
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    print("Random Date = ", randomDate)


def checkLeapYear(year):
    # Python program to check if year is a leap year or not

    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print("{0} is not a leap year".format(year))


def checkTriangle(x, y, z):
    """
    Determine if a triangle is equilateral, isosceles, or scalene.
    An equilateral triangle has all three sides the same length.
    An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
    A scalene triangle has all sides of different lengths.
    """
    if x == y == z:
        print("Equilateral triangle")
    elif x == y or y == z or z == x:
        print("isosceles triangle")
    else:
        print("Scalene triangle")

def generateArmstrongNumbers(lower, upper):
    """
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    """
    for num in range(lower,upper + 1):
       sum = 0
       temp = num
       while temp > 0:
           digit = temp % 10
           sum += digit ** 3
           temp //= 10
           if num == sum:
                print(num)


# import from string all ascii_lowercase and asc_lower
from string import ascii_lowercase as asc_lower

def checkPangram(s):
    # check if a sentence contains all the letters in the English alphabet.
    if set(asc_lower) - set(s.lower()) == set([]):
        print("The string is a pangram")
    else:
         print("The string is not a pangram")


def checkIsoGram(phrase):
    """The isogram is a string where the occurrence of each letter is exactly one. This code
    checks if a phrase or string is isogram
    """
    char_list = []
    for char in phrase:
        if char.isalpha():
            if char in char_list:
                return False
                char_list.append(char)
    return True

s = "education"
print(checkIsoGram(s))

