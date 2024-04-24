#!/usr/bin/env/ python3

if __name__ == '__main__':
    number = input("How many students? ")
    size = input("Required group size? ")
    number = int(number)
    size = int(size)
    num = number/size
    num = int(num)
    left = number - (size * num)
print("There will be",num, "groups with",left,"students left over.")