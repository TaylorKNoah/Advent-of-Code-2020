with open('Day_3/aoc3.txt') as f:
    r = 3
    d = 1
    l = len(f.readline()) -1
    trees = 0    
    print(r, l)
    for line in f:
        if line[r] == '#':
            trees += 1
        r += 3
        r %= l
        d += 1
    print(trees)
