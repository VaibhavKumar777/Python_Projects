def is_isogram(string):
    string = string.lower()
    seen = set()
    for c in string:
        if c.isalpha():
            if c in seen:
                return False
            seen.add(c)
    return True
