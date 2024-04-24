import sys

if __name__ == '__main__':
    count = len(sys.argv)
    total = 0
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
        print("Total is", total)