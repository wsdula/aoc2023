#Read in text. Keep the first and last digit to make a two digit number. Add all numbers to get answer.

#Two cases: no digits or atleast one digit
from sys import argv


def main(file='example2.txt'):
    digits = []
    word_digit_pairs = [
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9')
    ]

    with open(file, "r") as f:
        for i in f.readlines():
            print(i)
            temp = ''
            
            #The idea is we start iterating over the string and look at it by ignoring characters starting from the front. 
            #We compare each substring with our tuple of possible digits and build a pure number string from there.
            for c in range(len(i)):
                for word, digit in word_digit_pairs:
                    if i[c:].startswith(word):
                        temp += digit
                    elif i[c:].startswith(digit):
                        temp += digit

            print(temp)

            if temp != '':
                digits.append(int((temp[0] + temp[-1])))
            else:
                digits.append(0)
    
    return print(sum(digits))

main(*argv[1:])
