import string
letters = string.ascii_lowercase
reversed_letters = letters[::-1]
encode_map = {letters[i]: reversed_letters[i] for i in range(26)}
def encode(plain_text):
    plain_text = plain_text.lower()
    result = []
    for c in plain_text:
        if c.isalpha():
            result.append(encode_map[c])
        elif c.isdigit():
            result.append(c)
    grouped = []
    for i in range(0, len(result), 5):
        grouped.append("".join(result[i:i+5]))
    return " ".join(grouped)
decode_map = {v: k for k, v in encode_map.items()}

def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")  # remove spaces
    result = []

    for c in ciphered_text:
        if c.isalpha():
            result.append(decode_map[c])
        else:
            result.append(c)  # numbers stay

    return ''.join(result)
