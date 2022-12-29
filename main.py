import threading
import socket

choice = input("Host for '1' or to guest for '2': ")
if choice == '1':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("Your IPv4 Adress", 9999))
    server.listen()
    client, _ = server.accept()

elif choice == '2':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("Your IPv4 Adress", 9999))

else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You:" + message)

def receiving_messages(c):
    while True:
        print("Partner: " + c.recv(1024).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()