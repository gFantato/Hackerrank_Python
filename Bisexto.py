from xmlrpc.client import boolean


def is_leap(year):
    leap = False
    d4 = 0
    d100 = 0
    d400 = 0

    d4= year % 4
    d100= year % 100
    d400 = year % 400

    if d4 == 0:

        if d100 == 0:

            if d400 != 0:
                return boolean(False)

        return boolean(True)

    return leap


year = int(input())
print(is_leap(year))