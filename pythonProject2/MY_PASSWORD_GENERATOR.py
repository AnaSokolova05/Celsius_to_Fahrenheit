import random

passwords = ["hello", "happy", "spiderman", "iceland", "international", "football", "travel", "winder"
             "street", "newyork","password", "leeds", "london", "impressive", "bored", "cold","weather",
             "green", "color", "first", "world", "planet", "car", "tree", "big", "house", "beautiful",
             "forest", "number", "game", "vocabulary", "short", "personality", "question", "dog"
             "problem", "solution", "internet", "smartphone", "navigator", "supermarket", "christmas"]


def threeRandomwords(passwords):
    return ''.join(random.sample(passwords, 3))


if __name__ == '__main__':
    print("Password generator")
    print("==================")

    while True:
        try:
            num_password = int(input("How many passwords are needed?: "))

            if num_password <= 0 or num_password > 24:
                print("Please enter a value between 1 and 24")
            else:
                break
        except ValueError:
            print("Please enter a number")

    for n in range(num_password):
        print(threeRandomwords(passwords))