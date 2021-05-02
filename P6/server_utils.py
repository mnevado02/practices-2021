import Seq1
import jinja2
import pathlib



def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print("To server: ", end="")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping():
    print_colored("PING, command!", "green")

def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {"number": seq_number, "sequence": list_sequences[int(seq_number)]}
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def info(sequence):
    seq = Seq1.Seq(sequence)
    number_dict = seq.count()
    percentage_dict = seq.count_percentage()
    response = "Total length: " + str(seq.len()) + "<br>"
    for key in number_dict:
        response += (str(key) + ": " + str(number_dict[key]) + " (" + str(round(percentage_dict[key], 1)) + "%)<br>")
    context = {"sequence": sequence, "operation": "Info", "result": response}
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

def comp(sequence):
    seq = Seq1.Seq(sequence)
    response = seq.complement()
    context = {"sequence": sequence, "operation": "Rev", "result": response}
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

def rev(sequence):
    seq = Seq1.Seq(sequence)
    response = seq.reverse()
    context = {"sequence": sequence, "operation": "Rev", "result": response}
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

def gene(seq_name):
    PATH = "./Sequences/"
    s1 = Seq1.Seq()
    s1.seq_read_fasta(PATH + seq_name + ".txt")
    context = {"gene_name": seq_name, "gene_contents": s1.strbases}
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents

