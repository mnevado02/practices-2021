import Seq0

FOLDER = "./Sequences/"
ID = "U5.txt"

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
print("The first 20 bases are: ", U5_Seq[0:20])
