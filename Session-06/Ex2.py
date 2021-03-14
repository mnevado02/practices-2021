from Seq_01 import Seq

def print_seqs(seq_list):
    result = ""
    for i in range(len(seq_list)):
        print("Sequence " + str(i) + ": (Length: " + str(seq_list[i].len()) + "), " + f"{seq_list[i]}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
Seq.print_seqs(seq_list)
