import sys
from lexer import lex


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("File not found")
        sys.exit(0)
    else:
         with open(sys.argv[1], 'r') as f:
            line = f.readlines()
            while line:
                lex(line)
                line = f.readline()
