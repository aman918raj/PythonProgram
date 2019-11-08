_author_='aman'

def iterate_for(shopping_list):
    print('iterate_for')
    for item in shopping_list:
        print("I am buying {0}".format(item))

def iterate_continue(shopping_list):
    print('iterate_continue')
    for item in shopping_list:
        if item == 'spam':
            continue
        print("I am buying {0}".format(item))

def iterate_break(shopping_list):
    print('iterate_break')
    for item in shopping_list:
        if item == 'spam':
            break
        print("I am buying {0}".format(item))

def for_range():
    for i in range(1,30,7):
        print(i)

shopping_list = ['milk','eggs','bread','spam','butter','rice']
iterate_for(shopping_list)
iterate_continue(shopping_list)
iterate_break(shopping_list)
for_range()
