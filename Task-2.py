
def find_three(number_one, number_two):
    sum = str(number_one + number_two)

    if (number_one == 3 or number_two == 3) and (sum.__contains__("3")):
        return True
    else:
        return False 

print(find_three(3, 10))