import Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
print("------| Exercise 5 |------")

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print(gene + ":", Seq0.seq_count(sequence))