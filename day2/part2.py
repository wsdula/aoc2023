#Log each game id as a key, value being a list of dicts containing the information on pulls of cubes. If the bag had 12 red, 13 green, 14 blue to start; which game id's were possible? add those ids.

#Now we try to determine the minimum amount of cubes that are possible

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
            mult = 1
            key, value = line.split(':')
            key = int(key.strip().replace('Game',''))

            #data[key] = value

            for color in limits.keys():
                p = re.findall(rf"(\d*) {color}", value)
                

                if len(p) > 0:
                    print(p,color)
                    mult *= max([int(m) for m in p])

            result += mult
            print("Mult: {} Game {}: {}".format(mult,key,value))

    print("Result: {}".format(result))

main(*argv[1:])
