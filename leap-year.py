#Originally
#def is_leap(year):
#    if year % 4 == 0:
#        if year % 100 == 0:
#            if year % 4000 == 0:
#                return True
#            else:
#                return False
#        else:
#            return True
#    else:
#        return False

def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

leap_year = int(input("Type leap year:\n"))
print(odd_or_even(num))
