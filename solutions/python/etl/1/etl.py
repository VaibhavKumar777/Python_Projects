{
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}
def transform(legacy_data):
    new_format = {}
    for score,letters in legacy_data.items():
        for letter in letters:
            new_format[letter.lower()] = score
    return new_format