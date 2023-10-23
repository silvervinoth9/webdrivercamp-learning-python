#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
even_tuple = tuple(num % 2 == 0 for num in my_list)
print(my_list)
print(even_tuple)
