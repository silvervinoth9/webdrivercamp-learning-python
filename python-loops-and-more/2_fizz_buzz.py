#!/usr/bin/python3
def fizz_buzz():
    for i in range(0, 101):
        if (i%3==0):
            print("Fizz", end=" ")
        elif (i%5==0):
            print("Buzz", end=" ")
        elif (i%3==0 and i%5==0):
            print("FizzBuzz", end=" ")
        else:
            print(i, end=" ")
fizz_buzz()
