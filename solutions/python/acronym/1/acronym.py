import re

def abbreviate(words):
    acronym = ""
    for sep in ["-","_"]:
        words = words.replace(sep, " ")
    phrase = words.split()
    for word in phrase:
        for c in word:
            if c.isalpha():
                acronym+=c.upper()
                break
    return acronym
    
   