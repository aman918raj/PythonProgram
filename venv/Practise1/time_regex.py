_author_ = "aman"
import re
import time

def iterate_till_time_ends(t_end, list_of_files):
    while time.time() < t_end:
        print(time.time())
        print(t_end)
        file_pattern = input("Please enter the file pattern : ")
        for file in list_of_files:
            print("File is : {0}".format(file))
            if re.search(file_pattern, file):
                print("File found is : {0}".format(file))
                return True
    return False

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

list_of_files = ["file1.txt", "file2.csv", "file3.parquet", "file4.orc", "file5.xlsx"]
t_end = time.time() + 60 * 1
is_file_found = iterate_till_time_ends(t_end, list_of_files)

if is_file_found:
    print("File Found")
else:
    raise FileNotFoundError("File not found")
