_author_ = "aman"

# file = open("C:\\Users\\aman.raj\\Desktop\\new 31.txt","r")
# for line in file:
#     print(line, end='')

# with open("C:\\Users\\aman.raj\\Desktop\\new 31.txt","r") as file:
#     for line in file:
#         print(line, end='')

# with open("C:\\Users\\aman.raj\\Desktop\\new 31.txt","r") as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()

# with open("C:\\Users\\aman.raj\\Desktop\\new 31.txt","r") as file:
#     lines = file.readlines()
# print(lines)
# for line in lines:
#     print(line,end='')

with open("C:\\Users\\aman.raj\\Desktop\\new 31.txt","r") as file:
    lines = file.readlines()
print(lines)
for line in lines[::-1]:
    print(line,end='')
