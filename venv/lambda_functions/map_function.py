_author_ = "aman"

def line_output(line,i):
    output = lambda x: "line {0} is : ".format(i)+x
    return output(line)

file_line = lambda x: "line {0} is : ".format(i)+x


with open("C:\\Users\\aman.raj\\Desktop\\python_output\\file1.txt","r") as file:
    line = file.readline()
    i = 0
    while line:
        i += 1
        output = line_output(line,i)
        print(output)
        print(file_line(line))
        line = file.readline()
