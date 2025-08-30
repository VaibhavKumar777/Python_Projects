def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)

    result = []
    for words in candidates:
        words_lower = words.lower()
        if words_lower == word_lower:
            continue
        if sorted(words_lower) == word_sorted:
            result.append(words)
    return result
    

    
