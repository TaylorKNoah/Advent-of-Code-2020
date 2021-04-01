

with open('aoc4.txt') as f:
    valid = 0
    parts = [False for i in range(7)]


    for line in f:

       

        #reset passport
        if line == '\n':
            if all(parts):
                valid += 1
            for i in range(7):
                parts[i] = False

        #Get password line by line
        #Check each line for missing parts
        else:
            if not parts[0]:
                i1 = line.find("byr:")
                if i1 > -1:
                    j1 = i1+1
                    while line[j1] != ' ' and line[j1] != '\n':
                        j1 += 1
                    byr = int(line[i1+4:j1])
                    if byr > 1920 and byr < 2002:
                        parts[0] = True

            if not parts[1]:
                if line.find("iyr:") > -1:
                    parts[1] = True
            
            if not parts[2]:
                if line.find("eyr:") > -1:
                    parts[2] = True
            
            if not parts[3]:
                if line.find("hgt:") > -1:
                    parts[3] = True

            if not parts[4]:
                if line.find("hcl:") > -1:
                    parts[4] = True

            if not parts[5]:
                if line.find("ecl:") > -1:
                    parts[5] = True

            if not parts[6]:
                if line.find("pid:") > -1:
                    parts[6] = True
        
        if line.find('\n') < 0:
            if all(parts):
                valid += 1

    print(valid)