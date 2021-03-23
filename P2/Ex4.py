from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)
print(c.debug_talk("Message 1---"))
print(c.debug_talk("Message 2: Testing !!!"))