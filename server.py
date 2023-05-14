import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1235
s.bind((Host, Port))
s.listen(5)
client_socket, address = s.accept()
print(f"Connection to {address} established")
fileName = "yas.txt"
client_socket.send(fileName.encode('utf-8'))
file = open("yas.txt", "rb")
data = file.read()
client_socket.send(data)
file.close()
client_socket.close()