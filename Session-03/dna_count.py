def correct_dna(dna):
    for c in dna:
        if c != "A" and c != "C" and c != "G" and c != "T":
            return False
    return True

def dna_count(seq):
    n_a, n_c, n_g, n_t = 0, 0, 0, 0
    for ch in seq:
        if ch.lower() == "a":
            n_a += 1
        elif ch.lower() == "c":
            n_c += 1
        elif ch.lower() == "g":
            n_g += 1
        elif ch.lower() == "t":
            n_t += 1
    return n_a, n_c, n_g, n_t

seq = "ACCTGATGCCAHGTGAAG"

print("The lenght of the sequence is", len(seq))
if correct_dna(seq):
    a, c, g, t = dna_count(seq)
    print("A:", a, "\nC:", c, "\nG:", g, "\nT:", t)
else:
    print("The sequence is not valid DNA.")
