import sys

if __name__ == '__main__':

    num_steps = sys.argv[1]

    if num_steps.isdigit():
        num_steps = int(num_steps)
        for i in range(num_steps , 0, -1):
            step = ' ' * (i - 1) + '#' * (num_steps - i + 1)
            print(step)
