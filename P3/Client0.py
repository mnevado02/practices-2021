import socket
from termcolor import colored
import colorama


class Client:
    def __init__(self, ip, port):
        self. ip = ip
        self.port = port

    def ping(self):
        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up!")
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the PORT?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return response

    def debug_talk(self, msg):
        colorama.init(strip= False)
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print("To server:", colored(msg, "blue"))
        s.send(str.encode(msg))
        # Receive data
        response = colored(s.recv(2048).decode("utf-8"), "green")
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response
