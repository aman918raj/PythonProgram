_author_ = "aman"

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\binary","bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\binary","br") as bin_file:
    for b in bin_file:
        print(b)

a = 65534 #FF FE
b = 65535 #FF FF
c = 65536 #00 01 00 00
x = 6273829

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\binary2","bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))
 #   bin_file.write(x.to_bytes(2, 'little')) --> OverflowError: int too big to convert

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\binary2","br") as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'little')
    print(i)
