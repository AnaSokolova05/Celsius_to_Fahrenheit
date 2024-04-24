#!/usr/bin/env/ python3

if __name__ == '__main__':
    pas = input("Choose a new password: ")
    pas_2 = input("Enter password again: ")
    BAD_PAS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    if pas in BAD_PAS:
        print("You can not use this password")
        print("Try again")
    elif 8 <= len(pas) <= 12 and pas == pas_2:
        print("Password Set")
    else:
        print("Error")
        pas_2 = input("Enter a new password:")
