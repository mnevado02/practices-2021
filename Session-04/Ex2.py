import P0.Seq0 as Seq0


ID = "U5.txt"
U5_Seq = Seq0.seq_read_fasta(ID)
print("The first 20 bases are: ", U5_Seq[0:20])
a, c, g, t, = 0, 0, 0, 0

for ch in U5_Seq:
    if ch == "A":
        a += 1
    elif ch == "C":
        c += 1
    elif ch == "G":
        g += 1
    elif ch == "T":
        t += 1