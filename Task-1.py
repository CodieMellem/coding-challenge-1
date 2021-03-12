def sum_of_multiples(range_of_mult):
    sum = 0
    for i in range(range_of_mult):
        if i%3 == 0 or i%5 == 0 :
            sum += i
    return sum

print(sum_of_multiples(1000))