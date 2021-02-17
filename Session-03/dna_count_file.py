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

def correct_dna(dna):
    for c in dna:
        if c != "A" and c != "C" and c != "G" and c != "T":
            return False
    return True


def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        dna = dna.replace("\n", "")
        f.close()
        return dna

dna = read_from_file("dna.txt")
if correct_dna(dna):
    a, c, g, t = dna_count(dna)
    print("A:", a, "\nC:", c, "\nG:", g, "\nT:", t)
else:
    print("The sequence is not valid DNA.")