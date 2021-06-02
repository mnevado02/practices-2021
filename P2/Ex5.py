from Client1 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
print(c.talk("Sending a gene to the server..."))
print(c.talk(Path("U5.txt").read_text()))