_author_ = "aman"


def get_min_modified_date_file(dict_files):
    dict_of_files_sorted = sorted(list(dict_files.keys()))
    print(dict_of_files_sorted)
    oldest_file = dict_files[dict_of_files_sorted[0]]
    return oldest_file

a = "99999123999999"
b = int(a)
print(b)
files = ["file3", "file5", "file4", "file1", "file2"]
dict_files = {}
i = 0
for file in files:
    dict_files[221230222222 - i] = file
    i += 1
print(dict_files)
print(len(dict_files))
oldest_file = get_max_modified_date_file(dict_files)
print(oldest_file)
