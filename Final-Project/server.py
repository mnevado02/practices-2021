import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import utils as us
import json



# Define the Server's port
PORT = 8080


LIST_SEQUENCES = ["ATTCCGTGTCACT", "AAAAAAATTTTCGGCTAT", "AACCTCGCTAGCTAGCTAG",
                  "ATCTATCGCCCTTTTTTTTAA", "AAACCCAGGGTT"]

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


LIST_OPERATIONS = ["Info", "Comp", "Rev"]



# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties



class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)

        json_check = "json" in arguments and arguments["json"][0] == "1"
        context = {}
        print("path", path_name)
        if path_name == "/":
            context["list_genes"] = DICT_GENES.keys()
            context["dict_operations"] = {"1) Gene Sequence": "geneSeq", "2) Gene Information": "geneInfo", "3) Gene Calculations": "geneCalc"}
            context["op_names"] = ["1) Gene Sequence", "2) Gene Information", "3) Gene Calculations"]
            contents = us.read_template_html_file("./html/index.html").render(context=context)
            context.clear()
        elif path_name == "/listSpecies":
            limit = arguments["limit"][0]
            context = us.list_sp(limit)
            if json_check:
                contents = str(context)
                print(contents)
            else:
                if "error" in context:
                    contents = us.read_template_html_file("./html/error.html").render(context=context)
                else:
                    contents = us.read_template_html_file("./html/list_species.html").render(context=context)

        elif path_name == "/karyotype":
            context = us.karyotype(arguments["specie"][0])
            if json_check:
                contents = str(context)
            else:
                if "error" in context:
                    contents = us.read_template_html_file("./html/error.html").render(context=context)
                else:
                    contents = us.read_template_html_file("./html/karyotype.html").render(context=context)

        elif path_name == "/chromosomeLength":
            context = us.chromo_len(arguments["specie"][0], arguments["chromo"][0])
            if json_check:
                contents = str(context)
            else:
                if "error" in context:
                    contents = us.read_template_html_file("./html/error.html").render(context=context)
                else:
                    contents = us.read_template_html_file("./html/chromo_length.html").render(context=context)
        elif path_name == "/geneSeq":
            gene_name = arguments["gene"][0]
            seq = us.seq(gene_name).strbases
            context = {"gene_contents": seq, "gene_name": gene_name}
            if json_check:
                contents = str(context)
            else:
                contents = us.read_template_html_file("./html/geneSeq.html").render(context=context)
        elif path_name == "/geneInfo":
            gene_name = arguments["gene"][0]
            context = us.info(gene_name)
            if json_check:
                contents = str(context)
            else:
                contents = us.read_template_html_file("./html/geneInfo.html").render(context=context)
        elif path_name == "/geneCalc":
            gene_name = arguments["gene"][0]
            context = us.calc(gene_name)
            if json_check:
                contents = str(context)
            else:
                contents = us.read_template_html_file("./html/geneCalc.html").render(context=context)
        else:
            context["error"] = "Not a valid path"
            contents = us.read_template_html_file("./html/error.html").render(context=context)


        # Message to send back to the client

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()