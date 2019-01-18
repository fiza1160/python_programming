import sys
import os
import tempfile


class File:

    def __init__(self, path):
        if not os.path.exists(path):
            open(path, 'w')
        self.path = path
        with open(self.path) as f:
            self.data = f.readlines()
        self.current = 0
        self.end = len(self.data)

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        new_file = open(new_path, 'w')
        print(''.join(self.data), ''.join(other.data), sep='', end='', file=new_file)
        return File(new_path)

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.data[self.current]
        self.current += 1
        return result

    def write(self, string):
        with open(self.path, 'w') as f:
            print(string, file=f, sep='', end='')


if __name__ == '__main__':
    # path = sys.argv[1]
    path_1 = r'C:\Users\Fiza\PycharmProjects\python_programming\week_04\test_1.txt'
    file_1 = File(path_1)

    file_1.write('String for file 1\n')
    print(file_1)

    path_2 = r'C:\Users\Fiza\PycharmProjects\python_programming\week_04\test_2.txt'
    file_2 = File(path_2)
    file_2.write('String for file 2\nElse string for file 2\n')
    print(file_2)

    new_file = file_1 + file_2
    print(new_file)

    for string in File(r'C:\Users\Fiza\AppData\Local\Temp\new_file.txt'):
        print(string)


