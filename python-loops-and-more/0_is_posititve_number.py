#!/usr/bin/python3)
import random
random_num = random.randint(-10, 10)
if random_num == 0:
    print("{} is zero" .format(random_num))
elif random_num < 0:
    print("{} is negative" .format(random_num))
elif random_num > 0:
    print("{} is positive" .format(random_num))
