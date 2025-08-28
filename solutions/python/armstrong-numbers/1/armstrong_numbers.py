def is_armstrong_number(number):
    digits = str(number)
    num = len(digits)
    final = 0
    for x in digits:
        armstrong = int(x) **num
        final += armstrong
    if final == number:
        return True
    else:
        return False
