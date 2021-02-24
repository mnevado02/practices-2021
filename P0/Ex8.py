import Seq0

GENE_FOLDER = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "G", "T"]

print("------| Exercise 8 |------")

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene + ":", end=" ")
    base_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in base_dict:
        base_dict[base] += Seq0.seq_count_base(sequence, base)
    print(list(base_dict.keys())[list(base_dict.values()).index(max(base_dict.values()))])

