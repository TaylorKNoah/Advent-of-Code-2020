with open("aoc2.txt") as f:
    valid = 0
    
    for line in f:
        i = 0
        while line[i] != '-':
            i += 1
        lo = int(line[0:i])
        
        j = i
        while line[j] != ' ':
            j += 1
        hi = int(line[i+1:i+j-1])
        
        found = line.count(line[j+1])
        found -= 1
        if found >= lo and found <= hi:
            valid += 1
    
    print(valid)