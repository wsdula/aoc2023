#Read in text. Keep the first and last digit to make a two digit number. Add all numbers.

#Three cases: no digits, one digit, more than one digit
from sys import argv


def main(file='example.txt'):
    digits = []
    with open(file) as f:
        for i in f.readlines():
            temp = ''.join(c for c in i if c.isdigit())
            if temp != '':
                digits.append(int((temp[0] + temp[-1])))
            else:
                digits.append(0)
    
    return print(sum(digits))

main(*argv[1:])
