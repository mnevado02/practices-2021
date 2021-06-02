import termcolor
from pathlib import Path

class Seq:

    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases=NULL_SEQUENCE):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases = strbases
        else:
            if self.is_valid_sequence_2(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected!")

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True


    @staticmethod
    def print_seqs(seq_list, color="white"):
        result = ""
        for i in range(len(seq_list)):
            text = "Sequence " + str(i) + ": (Length: " + str(seq_list[i].len()) + ") " + f"{seq_list[i]}"
            termcolor.cprint(text, color)


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, t, g
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "G": g, "T": t}

    def count_percentage(self):
        a, c, g, t = self.count_bases()
        total = a + c + g + t
        return {"A": round(((a/total)*100),2), "C": round(((c/total)*100),2), "G": round(((g/total)*100),2), "T": round(((t/total)*100),2)}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[::-1]


    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = ""
            for ch in self.strbases:
                if ch.lower() == "a":
                    complement += "T"
                elif ch.lower() == "c":
                    complement += "G"
                elif ch.lower() == "g":
                    complement += "C"
                elif ch.lower() == "t":
                    complement += "A"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def seq_read_fasta(self, filename):
        self.strbases = self.take_out_first_line(Path(filename).read_text())
        return self.strbases


def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq

def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3