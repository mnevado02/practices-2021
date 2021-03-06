import socket
import utils

list_sequences = ["ATTCCGTGTCACT", "AAAAAAATTTTCGGCTAT", "AACCTCGCTAGCTAGCTAG",
                  "ATCTATCGCCCTTTTTTTTAA", "AAACCCAGGGTT"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
count_connections = 0
client_adress_list = []

while True:
    # -- Waits for a client to connect
    print("\nWaiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        count_connections += 1
        client_adress_list.append(client_ip_port)

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()
    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    formatted_message = utils.format_command(msg)
    formatted_message = formatted_message.split(" ")
    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]
    if command == "PING":
        utils.ping()
        # -- Send a response message to the client
        response = "OK!"
        # -- The message has to be encoded into bytes
        cs.send(str(response).encode())
    elif command == "GET":
        utils.get(cs, list_sequences, argument)
    elif command == "INFO":
        utils.calc(cs)
    elif command == "COMP":
        utils.comp(cs, list_sequences, argument)
    elif command == "REV":
        utils.rev(cs, list_sequences, argument)
    elif command == "GENE":
        utils.gene(cs, argument)

    else:
        response = "Not available command"
        cs.send(str(response).encode())

    # -- Close the data socket
    cs.close()
