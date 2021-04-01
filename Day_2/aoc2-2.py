with open('aoc2.txt') as f:
    valid = 0
    for line in f:
        i = 0
        while line[i] != '-':
            i +=1
        
        p1 = int(line[0:i])
        
        j = i
        while line[j] != ' ':
            j += 1
        
        p2 = int(line[i+1:j])

        key = line[j+1]

        if line[j+3+p1] == key and line [j+3+p2] != key:
            valid += 1
        
        if line [j+3+p1] != key and line [j+3+p2] == key:
            valid += 1
        

    print(valid)