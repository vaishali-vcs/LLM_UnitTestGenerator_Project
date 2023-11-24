# imports
import pytest  # used for our unit tests

# function to test
def rev_sentence(sentence): 
    # Function to reverse words of string  
    # first split the string into words 
    words = sentence.split(' ') 
 
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
 
    # finally return the joined string 
    return reverse_sentence 

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize(
    "input_sentence, expected_output", [
        # Scenario 1: Normal sentences with multiple words
        ("Hello world", "world Hello"),
        ("Python is a great language", "language great a is Python"),
        
        # Scenario 2: Sentences with only one word
        ("Hello", "Hello"),
        ("Python", "Python"),
        
        # Scenario 3: Sentences with special characters
        ("Hello, world!", "! world, Hello"),
        ("Python: A great language?", "? language great A :Python"),
        
        # Scenario 4: Sentences with numbers
        ("I have 2 apples", "apples 2 have I"),
        ("Python 3.8 is the version I use", "use I version the is 3.8 Python"),
        
        # Scenario 5: Sentences with multiple spaces between words
        ("Hello     world", "world     Hello"),
        ("Python     is     great", "great     is     Python"),
        
        # Scenario 6: Empty string
        ("", ""),
        
        # Scenario 7: String with only spaces
        ("     ", "     "),
        
        # Scenario 8: Sentences with punctuation without spaces
        ("Hello,world!", "!world,Hello"),
        ("Python:a great language?", "?language great a:Python"),
        
        # Scenario 9: Sentences with mixed case
        ("Hello World", "World Hello"),
        ("Python Is Great", "Great Is Python"),
        
        # Scenario 10: Sentences with non-alphabetic characters
        ("Hello@world", "world@Hello"),
        ("Python#is#great", "great#is#Python"),
        
        # Edge cases
        ("Hello\u00A0world", "world\u00A0Hello"),  # non-breaking space
        ("Python\tis\ngreat", "great\nis\tPython"),  # tab and newline
        ("Hello\\world", "world\\Hello"),  # escape sequence
        ("123456", "123456"),  # not a sentence
        ("!@#$%^&*()", "!@#$%^&*()"),  # not a sentence
        (" Hello world ", " world Hello "),  # leading/trailing spaces
        ("Able was I ere I saw Elba", "Elba saw I ere I was Able"),  # palindrome
        ("Hello hello Hello hello", "hello Hello hello Hello"),  # repeated words
    ]
)
def test_rev_sentence(input_sentence, expected_output):
    assert rev_sentence(input_sentence) == expected_output