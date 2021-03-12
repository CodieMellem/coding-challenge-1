def triangle(num_of_triangle):
    counter = num_of_triangle
    if num_of_triangle > 0:
        for i in range(num_of_triangle):
            print("#" * (i + 1))
    if num_of_triangle < 0:
        for i in range(num_of_triangle * -1):
            print("#" * ((num_of_triangle * -1)- i))
            

triangle(11)