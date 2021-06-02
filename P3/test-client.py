import Client1


print("-----| Practice 3, Exercise 7 |-----")

IP = "127.0.0.1"
PORT = 8080
gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
function_list = ["PING", "GET ", "INFO 0", "COMP 0", "REV 0", "GENE "]

c = Client1.Client(IP, PORT)
print(c)
for f in function_list:
    print_f = f.split(" ")[0]
    if f != "GET " and f != "GENE ":
        print("\n* Testing " + print_f + "...")
        print(c.talk(f))
    elif f == "GET ":
        print("\n* Testing " + print_f + "...")
        for i in range(5):
            print(f + str(i) + ":", end=" ")
            print(c.talk(f + str(i)))
    elif f == "GENE ":
        print("\n* Testing " + print_f + "...")
        for gene in gene_list:
            print(f + gene)
            print(c.talk("GENE " + gene) + "\n")
