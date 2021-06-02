import http.client



SERVER = "localhost"
PORT = 8080
ENDPOINT_DICT = {"/listSpecies": ["?limit=3&json=1", "?limit=3", "?limit=lksdga&json=1", "?limit=lksdga"],
                 "/karyotype": ["?specie=human&json=1", "?specie=human", "?specie=09&json=1", "?specie=09"],
                 "/chromosomeLength": ["?specie=mouse&chromo=5&json=1", "?specie=mouse&chromo=5", "?specie=ant&chromo=k&json=1", "?specie=ant&chromo=k", "?specie=human&chromo=k&json=1", "?specie=human&chromo=k"],
                 "/geneSeq": ["?gene=RNU6_269P&json=1", "?gene=RNU6_269P"],
                 "/geneInfo": ["?gene=ADA&json=1", "?gene=ADA"],
                 "/geneCalc": ["?gene=KDR&json=1", "?gene=KDR"]}


for endpoint, param_list in ENDPOINT_DICT.items():
    i = 1
    print("--- " + endpoint + " ---\n")
    for param in param_list:
        connection = http.client.HTTPConnection(SERVER, PORT)
        #print("\nConnection at server", SERVER, PORT)

        req = connection.request("GET", endpoint + param)
        response = connection.getresponse()
        print("* TEST" + str(i) + """
* Input:\n\nhttp://""" + SERVER + ":" + str(PORT) + endpoint + param + """\n
* Output:\n""")
        print(response.read().decode() + "\n\n")
        connection.close()
        i += 1
    print("\n\n")