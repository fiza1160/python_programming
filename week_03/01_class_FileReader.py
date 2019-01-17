import sys


class FileReader:

    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path) as f:
                return f.read()
        except IOError:
            return ''


def _main():
    path = sys.argv[1]
    reader = FileReader(path)
    print(reader.read())


if __name__ == '__main__':
    _main()
