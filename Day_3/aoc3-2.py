with open('aoc3.txt') as f:
    r1 = 1
    r3 = 3
    r5 = 5
    r7 = 7
    r2 = 1
    d = 1
    l = len(f.readline()) -1
    t11 = 0
    t13 = 0
    t15 = 0
    t17 = 0
    t12 = 0 
    
    for line in f:
        if line[r1] == '#':
            t11 += 1
        if line[r3] == '#':
            t13 += 1
        if line[r5] == '#':
            t15 += 1
        if line[r7] == '#':
            t17 += 1
        if d%2 == 0:
            if line[r2] == '#':
                t12 += 1
            r2 += 1
            r2 %= l

        r1 += 1
        r1 %= l
        r3 += 3
        r3 %= l
        r5 += 5
        r5 %= l
        r7 += 7
        r7 %= l
        d += 1
    
    total = t11*t13*t15*t17*t12
    print(t11, t13, t15, t17, t12, total)