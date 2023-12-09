from sys import argv

''' put notes on problem here '''

def main(file="example"):
    #print(open(file,"r").readlines())

    with open(file, "r") as f:
        lines = [[c for c in line] for line in f.read().splitlines()]
        for line in lines:
            print(f"{line}\n")
        adj = [(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy) != (0,0)]
        keep = False
        num = ""
        ans = 0

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j].isdigit():
                    if any(lines[i+dx][j+dy] != '.' and not lines[i+dx][j+dy].isdigit()
                            for dx,dy in adj
                            if (i+dx) in range(len(lines)) and j+dy in range(len(lines[i+dx]))):
                        keep = True
                    num += lines[i][j]
                else:
                    if keep and len(num) > 0:
                        ans += int(num)
                        print(f"num: {num}, ans: {ans}")
                    num = ""
                    keep = False

        #if keep and len(num) > 0:
        #    ans += int(num)

        return print(f"ans: {ans}")


main(*argv[1:])    
