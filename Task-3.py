def find_sixty_three(number_one, number_two):
    sum = str(number_one + number_two)

    if (number_one == 65 or number_two == 65) or (sum.__contains__("65")):
        return True
    else:
        return False 

print(find_sixty_three(5, 60))