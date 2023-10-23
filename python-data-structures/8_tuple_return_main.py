#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]


def tuple_return(arg):
    length = len(arg)
    return (length, arg[0]) if length > 0 else (0, None)


if __name__ == "__main__":
    my_tuple = tuple_return(my_list)
    print(my_tuple)
    print(f'List len = {my_tuple[0]}')
    print(f'First element = {my_tuple[1]}')
