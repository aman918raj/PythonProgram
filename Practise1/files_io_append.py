_author_ = "aman"

with open("C:\\Users\\aman.raj\\Desktop\\python_output\\file1.txt", "a") as city_file1:
    for i in range(2, 13):
        print("{0} table is : ".format(i),file=city_file1)
        for x in range(1, 11):
            print("{0} times {1} is {2}".format(x, i, x*i),file=city_file1)
