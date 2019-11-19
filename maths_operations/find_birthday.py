_author_ = "aman"


def birthday(month, day, year):
    days = 0
    for i in range(1, 12):
        print(i)
        if i == month:
            days += day
            break
        if month > 2 and year % 4 == 0:
            if i == 2:
                days += 29
            elif i != 2 and i % 2 != 0:
                days += 31
            else:
                days += 30
        elif month > 2 and year % 4 != 0:
            if i == 2:
                day += 28
            elif i != 2 and i % 2 != 0:
                days += 31
            else:
                days += 30
        else:
            days += 31
    return days

dayInYear = birthday(12, 25, 2004)
print(dayInYear)

##########Extract 'Hello' from my_dict###############
my_dict = {'k1': [23, 56, False], 'k2': {'k3' : [1, 'Hello']}}
print(my_dict['k2']['k3'][1])
