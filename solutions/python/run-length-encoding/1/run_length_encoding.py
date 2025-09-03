def decode(string):
    result = []
    count = 0
    for c in string:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            if count == 0:
                result.append(c)
            else:
                result.append(c*count)
                count = 0
    return "".join(result)


def encode(string):
    if not string:
        return ""
    result = []
    count = 1
    prev = string[0]
    for c in string[1:]:
        if c == prev:
            count+=1
        else:
            if count>1:
                result.append(str(count))
            result.append(prev)
            prev = c
            count = 1
    if count>1:
        result.append(str(count))
    result.append(prev)
    return "".join(result)
    