def recite(start_verse, end_verse):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
     
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]
    
    result = []
    for verse_num in range(start_verse, end_verse + 1):
        intro = f"On the {days[verse_num-1]} day of Christmas my true love gave to me: "
        verse_parts = []
        for i in range(verse_num, 0, -1):
            if i == 1 and verse_num>1:
                verse_parts.append("and " + gifts[0])
            else:
                verse_parts.append(gifts[i-1])
        verse = intro + ", ".join(verse_parts)
        result.append(verse)
    return result



