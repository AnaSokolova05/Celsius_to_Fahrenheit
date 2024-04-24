#!/usr/bin/env/ python3

if __name__ == '__main__':
    number_sweets = input("What is the number of sweets? ")
    number_pupils = input("What is the number of pupils? ")
    number_sweets = int(number_sweets)
    number_pupils = int(number_pupils)
    count = number_sweets/number_pupils
    count = int(count)
    left = number_sweets - (number_pupils * count)
print("Each pupil will get",count, "sweets with", left, "left." )