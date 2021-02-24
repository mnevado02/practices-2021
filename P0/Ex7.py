import Seq0

print("------| Exercise 7 |------")

GENE_FOLDER = "./Sequences/"
gene = "U5"
sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")[:20]

print("Gene", gene + ":")
print("Frag:", sequence)
print("Rev:", Seq0.seq_complement(sequence))