import sys

from builder.Builder import Builder

if __name__ == '__main__':
    builder = Builder('template.txt', 'test.csv', 'out.txt')
    # builder = Builder(sys.argv[1], sys.argv[2])
    builder.build()
