from Client1 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
c.advanced_ping()