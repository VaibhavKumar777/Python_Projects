def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10:
        return False
    if not isbn[:9].isdigit():
        return False
    if not(isbn[9].isdigit() or isbn[9] == "X"):
        return False
    digits = []
    for i,c in enumerate(isbn):
        if c == "X":
            digits.append(10)
        else:
            digits.append(int(c))
    total = sum(d*(10-i) for i,d in enumerate(digits))
    return total%11==0
        
        
            
    
