# imports
import pytest  # used for our unit tests

# function to test
def pig_latin(text):
    def translate(word):
        vowels = 'aeiou'
        if word[0] in vowels:
            return word + 'way'
        else:
            consonants = ''
            for letter in word:
                if letter not in vowels:
                    consonants += letter
                else:
                    break
            return word[len(consonants):] + consonants + 'ay'

    words = text.lower().split()
    translated_words = [translate(word) for word in words]
    return ' '.join(translated_words)

# unit tests
# below, each test case is represented by a tuple passed to the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("input_text, expected_output", [
    ("apple", "appleway"),  # single word starting with a vowel
    ("elephant", "elephantway"),  # single word starting with a vowel
    ("umbrella", "umbrellaway"),  # single word starting with a vowel
    ("python", "onpythay"),  # single word starting with a consonant
    ("banana", "ananabay"),  # single word starting with a consonant
    ("cherry", "errychay"),  # single word starting with a consonant
    ("I like apples", "iway ikelay applesway"),  # sentence with multiple words
    ("The quick brown fox", "ethay uickqay rownbay oxfay"),  # sentence with multiple words
    ("Pig Latin is fun", "igpay atinlay isway unfay"),  # sentence with multiple words
    ("Python", "onpythay"),  # word with uppercase letters
    ("Banana", "ananabay"),  # word with uppercase letters
    ("Cherry", "errychay"),  # word with uppercase letters
    ("Hello, world!", "ellohay, orldway!"),  # text contains punctuation
    ("I'm happy.", "i'mway appyhay."),  # text contains punctuation
    ("Do you like apples?", "oday ouyay ikelay applesway?"),  # text contains punctuation
    ("", ""),  # empty string
    ("123", "123"),  # text contains non-alphabetic characters
    ("$%^&*", "$%^&*"),  # text contains non-alphabetic characters
    ("apple123", "apple123way"),  # text contains non-alphabetic characters
    ("my", "ymay"),  # text contains words with no vowels
    ("by", "ybay"),  # text contains words with no vowels
    ("fly", "lyfay"),  # text contains words with no vowels
    ("shh", "shhay"),  # text contains words that are entirely made up of consonants
    ("tst", "tstay"),  # text contains words that are entirely made up of consonants
    ("hmm", "mmhay"),  # text contains words that are entirely made up of consonants
    ("Python", "onpythay"),  # text contains words with mixed case
    ("PyThOn", "onpythay"),  # text contains words with mixed case
    ("PIG LATIN", "igpay atinlay"),  # text contains words with mixed case
    ("café", "afécaay"),  # text contains non-English characters or diacritics
    ("résumé", "ésuméray"),  # text contains non-English characters or diacritics
    ("naïve", "aïvenay"),  # text contains non-English characters or diacritics
    ("mother-in-law", "other-in-lawmay"),  # text contains words with hyphens or apostrophes
    ("it's", "it'sway"),  # text contains words with hyphens or apostrophes
    ("o'clock", "o'clockway"),  # text contains words with hyphens or apostrophes
    ("aeiou", "aeiouway"),  # text contains words with no consonants
    ("ooee", "ooeeway"),  # text contains words with no consonants
    ("i", "iway"),  # text contains words with no consonants
    ("Hello\tworld", "ellohay\torldway"),  # text contains whitespace characters other than spaces
    ("Hello\nworld", "ellohay\norldway"),  # text contains whitespace characters other than spaces
    ("Hello\r\nworld", "ellohay\r\norldway")  # text contains whitespace characters other than spaces
])
def test_pig_latin(input_text, expected_output):
    assert pig_latin(input_text) == expected_output