import Client1

c = Client1.Client("127.0.0.1", 8080)
for i in range(0,5):
    c.debug_talk("Message " + str(i))

