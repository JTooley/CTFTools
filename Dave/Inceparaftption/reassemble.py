
f1 = open("1.bin", "rb");
f2 = open("2.bin", "rb");
f3 = open("3.bin", "rb");
f4 = open("4.bin", "rb");
f5 = open("5.bin", "rb");

fout = open("msg.txt", "wb");

while True:
  byte = f1.read(1);
  fout.write(byte);
  byte = f2.read(1);
  fout.write(byte);
  byte = f3.read(1);
  fout.write(byte);
  byte = f4.read(1);
  fout.write(byte);
  byte = f5.read(1);
  fout.write(byte);