import string
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = set(string.ascii_lowercase)
    letters_insentence = set(c for c in sentence if c.isalpha())
    return alphabet<= letters_insentence
