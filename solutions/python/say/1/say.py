ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousands = ["", "thousand", "million", "billion"]  
def say(number):
    if number < 0:
        raise ValueError("input out of range")
    if number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    def chunk_to_words(num):
        words = []
        hundreds_digit = num // 100      
        tens_digit = (num % 100) // 10   
        ones_digit = num % 10
        if hundreds_digit>0:
            words.append(ones[hundreds_digit]+ " hundred")
        if tens_digit == 1:
            words.append(teens[ones_digit])
        elif tens_digit>1:
            word = tens[tens_digit]
            if ones_digit>0:
                word+= "-"+ones[ones_digit]
            words.append(word)
        elif tens_digit == 0 and ones_digit > 0:
            words.append(ones[ones_digit])
        return " ".join(words)
    number_str = str(number)
    chunks = []
    while number_str:
        chunks.insert(0,int(number_str[-3:]))
        number_str = number_str[:-3]
    words_list = []
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            words_list.append(chunk_to_words(chunk) + (" " + thousands[len(chunks)-i-1] if thousands[len(chunks)-i-1] else ""))
    
    return " ".join(words_list).strip()
    
