import Seq1
import jinja2
import pathlib
import json
import http.client

DICT_GENES = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"
         }



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

def get_json(endpoint):
    SERVER = "rest.ensembl.org"
    PARAMETERS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", endpoint + PARAMETERS)
    response = connection.getresponse()
    return json.loads(response.read().decode())

def list_sp(limit):
    list_species = get_json("/info/species")["species"]
    context = {"length": len(list_species)}
    try:
        context["limit"] = min(int(limit), context["length"])
        context["common_name"] = []
        for e in list_species[:min(int(limit), context["length"])]:
            context["common_name"].append(e["common_name"].capitalize())
        return context
    except:
        return {"error": "Need an integer for limit parameter"}

def karyotype(specie):
    try:
        context = {"list_karyotype": get_json("/info/assembly/" + specie)["karyotype"], "specie": specie}
        return context
    except KeyError:
        context = {"error": "Need the name of a valid species for karyotype"}
        return context


def chromo_len(specie, chromo):
    response = get_json("/info/assembly/" + specie)
    context = {"specie": specie, "chromosome": chromo}
    try:
        for d in response["top_level_region"]:
            if d["coord_system"] == "chromosome" and d["name"] == chromo:
                context["length"] = d["length"]
        return context
    except KeyError:
        context["error"] = "Need the name of a valid species and chromosome"
        return context


def seq(gene_name):
    response = get_json("/sequence/id/" + DICT_GENES[gene_name])
    seq = Seq1.Seq(response["seq"])
    return seq


def info(gene_name):
    response = get_json("/sequence/id/" + DICT_GENES[gene_name])
    desc = response["desc"].split(":")
    context = {"gene_name": gene_name, "start": desc[3], "chr_name": desc[1], "end": desc[4], "length": int(desc[4]) - int(desc[3]), "id": response["id"]}
    return context

def calc(gene_name):
    sequence = seq(gene_name)
    context = {"gene_name": gene_name, "length": sequence.len(), "perc_dict": sequence.count_percentage()}
    return context


