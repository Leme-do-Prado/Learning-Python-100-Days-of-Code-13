#Originally
#def odd_or_even(number):
#    if number % 2 == 0:
#        return "This is an even number."
#    else:
#        return "This is an odd number."

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

num = int(input("Type number: \n"))
print(odd_or_even(num))
