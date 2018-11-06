import re
import socket	#for sockets
import sys	#for exit
import random

try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print('Failed to create socket.')
	sys.exit();

print('Socket Created')

host = 'amazeing.baectf.com'
port = 443
password = 'foggykilljoy'

try:
	remote_ip = socket.gethostbyname( host )

except socket.gaierror:
	#could not resolve
	print('Hostname could not be resolved. Exiting')
	sys.exit()
	
print('Ip address of ' + host + ' is ' + remote_ip)

#Connect to remote server
s.connect((remote_ip , port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)
message = password + '\n'
s.sendall(str.encode(message))

# nums_regex = re.compile('\d+\s+\d+\s+\d+\s+\d+')

directions = [ ['R', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'L', 'L', 'D', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R'] ]

dirs = [ 'R', 'D', 'L', 'U']

i = 0
j = 0
last_dir = dirs[0]

while True:
    data = s.recv(2048)
    if not data:
        break
    else:
        try:
            data_str = str(data,'utf-8')
            print(data_str)
            wall = False
            lines = re.split('\n',data_str)
            for line in lines:
                if "Ouch" in line:
                    print("Hit a wall")                
                    wall = True
            if i == 0:
                message = directions[i][j] + '\n'
                j += 1
                if j == len(directions[i]):
                    i += 1
                    j = 0
                    print("Start maze " + str(i))
            if i >= 1:
                if wall:
                    last_dir = dirs[random.randint(0,3)]
                print("Going: " + last_dir) 
                message = last_dir + '\n'

            s.sendall(str.encode(message))
        except UnicodeDecodeError:
            print(data)
            # data_array = data[len(data)-16:len(data)]
            # byte1 = int.from_bytes(data_array[0:4], byteorder='little')
            # byte2 = int.from_bytes(data_array[4:8], byteorder='little')
            # byte3 = int.from_bytes(data_array[8:12], byteorder='little')
            # byte4 = int.from_bytes(data_array[12:16], byteorder='little')
            # total = byte1 + byte2 + byte3 + byte4            
            # print("Bytes total is " + str(total))
            # message = total.to_bytes((total.bit_length() // 8) + 1, byteorder='little')
            # s.sendall(message)

