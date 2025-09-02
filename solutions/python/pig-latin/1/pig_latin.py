vowels = ("a", "e", "i", "o", "u")
def translate(text):
    words = text.split()
    result = []

    for word in words:
        if word.startswith(("xr", "yt")):
            result.append(word+"ay")
            continue
        if word[0] in vowels:
            result.append(word+"ay")
            continue
        else:
            idx = 0
            while idx< len(word):
                if word[idx] in vowels or (idx != 0 and word[idx] == "y"):
                    break
                if word[idx:idx+2] == "qu":
                    idx+=2
                    break
                else:
                     idx+=1
            result.append(word[idx:] + word[:idx] + "ay")
    return " ".join(result)
