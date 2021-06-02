import http.client
import json
import Seq1

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

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = DICT_GENES["MIR633"]
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)

for gene in DICT_GENES:
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMETERS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        print(response_dict)
        #print(json.dumps(response_dict, indent=4, sort_keys=True))
        description = response_dict["desc"]
        print("\nGene:", gene)
        print("Description:", description)
        sequence = Seq1.Seq(response_dict["seq"])
        print("Total length:", sequence.len())
        freq_count = 0
        freq_base = ""
        for base, count in sequence.count().items():
            print(base + ": " + str(count) + " (" + str(round(sequence.count_percentage()[base], 1)) + "%)")
            if freq_count < count:
                freq_count = count
                freq_base = base

        print("Most frequent base:", freq_base)


