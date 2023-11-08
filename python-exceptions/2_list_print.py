#!/usr/bin/python3
def list_int_print(lst=[], i=0):
    num = 0
    for x in range(0, i):
        try:
            print(f"{lst[x]:d}", end=" ")
            num +=1
        except (ValueError, TypeError):
            continue
        print()
    return num

if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_int_print(list_, 4)
    print(f"Count: {count:d}")
