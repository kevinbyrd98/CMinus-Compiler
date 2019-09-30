import re
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])
Tokens = []
lineCommentRegex = re.compile(r'^(//.*\n)')
blockCommentRegex = re.compile(r'^(/\*)')
whiteSpace = re.compile(r'^[^\S\r\n]+')
operatorRegex = re.compile(r'^(==|>=|<=|>|<|!=)')
delimiterRegex = re.compile(r'^(\(|\)|\[|\]|{|}|,|;|=)')
mathRegex = re.compile(r'^(\+|-|/|\*)')
integerRegex = re.compile(r'^\d+')
keywordRegex = re.compile(r'^(int|void|while|if|else|return)')
identifierRegex = re.compile(r'^[a-zA-Z]+')
errorRegex = re.compile(r'\W+|_')

def makeTokens(text):
    inBlockComment = False
    for line in text:
        print("INPUT: " + line)
        while line != '\n':
            if line not in ['\n', ""]:
                y = 0
                if inBlockComment == False:
                    if re.search(blockCommentRegex, line):
                        x = re.findall(blockCommentRegex, line)[0]
                        line = line.replace(x, "", 1)
                        inBlockComment = True
                    elif re.search(operatorRegex, line):
                        x = re.findall(operatorRegex, line)[0]
                        t = Token('RELOP', x)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                        line = line.replace(x, "", 1)
                    elif re.search(delimiterRegex, line):
                        x = re.findall(delimiterRegex, line)[0]
                        t = Token('DELIM', x)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                        line = line.replace(x, "", 1)
                    elif re.search(mathRegex, line):
                        x = re.findall(mathRegex, line)[0]
                        t = Token('MATOP', x)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                        line = line.replace(x, "", 1)
                    elif re.search(integerRegex, line):
                        x = re.findall(integerRegex, line)[0]
                        t = Token('INT', x)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                        line = line.replace(x, "", 1)
                    elif re.search(keywordRegex, line):
                        x = re.findall(keywordRegex, line)[0]
                        t = Token('KEYWORD', x)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                        line = line.replace(x, "", 1)
                    elif re.search(identifierRegex, line):
                        x = re.findall(identifierRegex, line)[0]
                        t = Token('ID', x)
                        line = line.replace(str(x), "", 1)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                    elif re.search(whiteSpace, line):
                        x = re.findall(whiteSpace, line)[0]
                        line = line.replace(str(x), "", 1)
                    elif re.search(lineCommentRegex, line):
                        break
                    elif re.search(errorRegex, line):
                        x = re.findall(errorRegex, line)[0]
                        t = Token('ERROR', x)
                        line = line.replace(str(x), "", 1)
                        print(str(t[0]) + ": " + str(t[1]))
                        Tokens.append(t)
                else:
                    if line == "":
                        break
                    string = line[y]
                    exitor = ""
                    while line[y] + line[y + 1] != '*/' and y != len(line) - 2:
                        y = y + 1
                        exitor = line[y] + line[y + 1]
                        string = string + line[y]
                    if y != len(line):
                        string = string + line[y + 1]
                    if exitor == "*/":
                        inBlockComment = False

                    line = line.replace(string, "", 1)
            else:
                break
def lex(text):
    makeTokens(text)
