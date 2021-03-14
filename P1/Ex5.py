from Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print("Sequence " + str(i) + ": (Length: " + str(sequence.len()) + ") " + str(sequence))
    a, c, g, t = sequence.count_bases()
    print("A: " + str(a) + ",   C: " + str(c) + ",   G: " + str(g) + ",   T: " + str(t))

print("-----| Practice 1, Exercise 5 |------")

list_seq = list(test_sequences())

for i in range(0, len(list_seq)):
    print_result(i, list_seq[i - 1])