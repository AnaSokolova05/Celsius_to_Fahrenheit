import random

if __name__ == '__main__':

    name = open('names.txt','r+')
    email = open('email.txt','w')
    digits = "0123456789"
    length = 4
    all = ""

    for line in name.readlines():
        join = all.join(random.sample(digits, length))
        surname = line.split(',')[0][8:]
        surname = surname.lower()
        names = line.split(',')
        first_names = names[1].split()
        val = ""

        for initials in first_names:
            val = val + initials[0][0].lower()

        print(line[:8] + " ", val + ".", surname + join + "poppleton.ac.uk")

