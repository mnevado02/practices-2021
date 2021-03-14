from Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print("Sequence " + str(i) + ": (Length: " + str(sequence.len()) + " ) " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())


print("-----| Practice 1, Exercise 7 |------")

list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result((i + 1), list_sequences[i])