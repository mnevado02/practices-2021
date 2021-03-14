from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "G", "T"]

for gene in gene_list:
    s1 = Seq()
    s1.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    base_dict = s1.count()
    max_base = list(base_dict.keys())[list(base_dict.values()).index(max(base_dict.values()))]
    print("Gene: " + gene + ": Most frequent Base: " + max_base)

