#!/usr/bin/python3
def int_print(value):
   try:
     print(f"{value:d}")
   except:
     return False
   else:
     return True

if __name__ == "__main__":
    value = 42
    if not (int_print(value)):
        print(f"{value} is not an integer")

    value = -100
    if not (int_print(value)):
        print(f"{value} is not an integer")

    value = "Webdriver Camp"
    if not (int_print(value)):
        print(f"{value} is not an integer")
