import re
import socket	#for sockets
import sys	#for exit
import random
import hashlib

secret = "deadbeef" * 16
data = "ls"

print(secret)
combo = secret.decode("hex") + data
print(combo)

h = hashlib.new('sha1')
h.update(combo)
print(h.hexdigest())
print(h.digest_size)
print(h.block_size)

data = "ls\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x10\x20\x2dl"
combo = secret.decode("hex") + data
print(combo)

h = hashlib.new('sha1')
h.update(combo)
print(h.hexdigest())
print(h.digest_size)
print(h.block_size)