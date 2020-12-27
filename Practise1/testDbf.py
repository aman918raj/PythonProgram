_author_ = "aman"
import dbfread


def convert_rec(dbf, lst_of_key,lst_of_value):
    i = 0
    for records in dbf:
        lst_value = list(records.values())
        lst_of_value.insert(i,lst_value)
        if i == 0:
            for key in records.keys():
                lst_of_key.append(key)
        i += 1
        if(i < 30):
            print(lst_value[5])
    return lst_of_key,lst_of_value

input_path = "C:/Users/aman.raj/Documents/BCN0220.DBF"
dbf = dbfread.DBF(input_path,encoding="ibm850")

lst_of_key = []
lst_of_value=[[]]
print(dbf)
lst_of_key,lst_of_value=convert_rec(dbf,lst_of_key,lst_of_value)
