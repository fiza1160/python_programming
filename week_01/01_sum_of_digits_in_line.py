import sys

if __name__ == '__main__':

    digit_string = sys.argv[1]

    if digit_string.isdigit():
        res = int()
        for number in digit_string:
            res += int(number)
        print(res)
