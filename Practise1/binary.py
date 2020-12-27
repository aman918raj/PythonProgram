_author_ = "aman"

from zipfile import ZipFile

for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

with ZipFile('C:\\Users\\aman.raj\\Documents\\GST\\GST_C_20200229.zip','r') as zipObj:
    zipObj.extractall('C:\\Users\\aman.raj\\Documents\\GST\\temp')
