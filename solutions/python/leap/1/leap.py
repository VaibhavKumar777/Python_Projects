def leap_year(year):
    if year % 400 == 0:   # Rule 1
        return True
    elif year % 100 == 0: # Rule 2
        return False
    elif year % 4 == 0:   # Rule 3
        return True
    else:                 # Rule 4
        return False
