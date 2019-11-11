_author_ = "aman"
import re

def find_file(list_of_files, pattern):
    for file in list_of_files:
        print("file is : {0}".format(file))
        if re.search(pattern, file):
            print("file found : {0}".format(file))
            return True
    return False

list_of_files = ["file1.txt", "file2.csv", "file3.parquet", "file4.orc", "file5.xlsx"]
pattern = ".*.parquet$"
isFileFound = find_file(list_of_files, pattern)

if isFileFound:
    print("File has been found in the list")
else:
    print("File is not present in the list")
