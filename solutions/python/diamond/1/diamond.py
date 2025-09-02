def rows(letter):
    rows = 2 * (ord(letter) - ord('A') + 1) - 1
    mid = rows//2
    result = []
    for i in range(rows):
        space = abs(mid-i)
        char_index = mid - space
        char = chr(ord('A')+char_index)
        if char == "A":
            line = " " * space + "A" + " " * space
        else:
            inside = 2*(char_index - 1) + 1
            line = " " * space + char+ " "*inside + char + " "*space
        result.append(line)
    return result
            
        
