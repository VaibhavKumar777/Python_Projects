def to_rna(dna_strand):
    result = ""
    x = dna_strand.strip()
    for i in (x):
        if i == "C":
            result+=("G")
        if i == "G":
            result+=("C")
        if i == "T":
            result+=("A")
        if i == "A":
            result+=("U")
    return result
