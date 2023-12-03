#Log each game id as a key, value being a list of dicts containing the information on pulls of cubes. If the bag had 12 red, 13 green, 14 blue to start; which game id's were possible? add those ids.

from sys import argv
import re

def main(file="example.txt"):
    #data = {}
    limits = {
        'red' : 12,
        'blue' : 14,
        'green' : 13
    } 
    result = 0
    

    with open(file, "r") as f:

        for line in f.readlines():
            flag = False
            key, value = line.split(':')
            key = int(key.strip().replace('Game',''))

            if ';' in value:
                value = value.split(';')

            value = [x.strip() for x in value]
            #data[key] = value

            for pull in value:
                for color in limits.keys():
                    p = re.search(rf"(\d\d) {color}", pull)

                    if p is not None and int(p.group(1)) > limits[color]:
                        flag = True
                        break

            if flag == False:
                result += key

                print("{} Game {}: {}".format(flag,key,value))
    print("Result: {}".format(result))

main(*argv[1:])
