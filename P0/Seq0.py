from pathlib import Path


def seq_ping():
    print("OK")


def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")


def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict


def seq_reverse(seq):
    result = ""
    for i in range(len(seq)):
        result += seq[-(i + 1)]
    return result


def seq_complement(seq):
    c_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement = ""
    for c in seq:
        complement += c_dict[c]
    return complement
