_author_ = "aman"

# * --> allows mutiple parameters to be passed to a function
def print_text(*args):
    txt = ""
    for arg in args:
        txt += str(arg) + " "
    print(txt)

print_text(3, "abcd", 883, "sjdj")

