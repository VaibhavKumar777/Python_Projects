letters = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}
def score(word):
    total = 0
    word = word.upper()
    for letter in word:
        for points, group in letters.items():
            if letter in group:
                total+=points
                break
    return total
        
        
    
