CODON_TABLE = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}

def proteins(strand):
    protein_list = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        amino_acid = CODON_TABLE.get(codon)
        if amino_acid == "STOP":
            break
        if amino_acid:
            protein_list.append(amino_acid)
    return protein_list
