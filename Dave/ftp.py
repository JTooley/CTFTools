import socket
import binascii
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('skillz.baectf.com', 33333))

my_bytes = bytearray()
my_bytes.append(26)
my_bytes.append(0)
my_bytes.append(0)
my_bytes.append(0)

sock.sendall(my_bytes);
sock.sendall("Initiate transfer protocol")
challenge = sock.recv(16);

b = bytearray(challenge)
test  = binascii.hexlify(b)
print test

password = raw_input("enter password:")

my_bytes = bytearray()
my_bytes.append(len(password))
my_bytes.append(0)
my_bytes.append(0)
my_bytes.append(0)

sock.sendall(my_bytes);
sock.sendall(password)

print sock.recv(1024)
print sock.recv(1024)
print "recv2"
print sock.recv(1024)

while(True):
  string = raw_input("enter command:")
  my_bytes = bytearray()
  my_bytes.append(len(string))
  my_bytes.append(0)
  my_bytes.append(0)
  my_bytes.append(0)

  sock.send(my_bytes);
  sock.send(string)

  print sock.recv(1024)