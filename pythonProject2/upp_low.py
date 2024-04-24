#!/usr/bin/env/ python3

if __name__ == '__main__':
    def upp_low(msg):
        count1 = 0
        count2 = 0
        for a in msg:
            if a.islower():
                count1 = count1 + 1
            elif a.isupper():
                count2 = count2 + 1
        print("The number of lowercase letters is:", count1)
        print("The number of uppercase letters is:", count2)
