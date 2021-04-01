with open('Day_4/aoc4.txt') as f:
    valid = 0
    parts = [False for i in range(7)]
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    index = 0

    for line in f:

        index += 1

        #if index == 40:
        #    print(line)

        #reset passport
        if line == '\n':
            if all(parts):
                valid += 1
            for i in range(7):
                parts[i] = False

        #Get passport line by line
        #Check each line for missing parts
        else:
            if not parts[0]:
                i = line.find("byr:")
                if i > -1:
                    byr = int(line[i+4:i+8])
                    #print(index, ': ', byr)
                    if byr >= 1920 and byr <= 2002:
                        parts[0] = True

            if not parts[1]:
                i = line.find("iyr:")
                if i > -1:
                    iyr = int(line[i+4:i+8])
                    if iyr >= 2010 and iyr <= 2020:
                        parts[1] = True

            if not parts[2]:
                i = line.find("eyr:")
                if i > -1:
                    eyr = int(line[i+4:i+8])
                    if eyr >= 2020 and eyr <= 2030:
                        parts[2] = True
            
            if not parts[3]:
                i  = line.find("hgt:")
                if i > -1:
                    j = i+4

                    #print('\n Index: ', end='')
                    #print(index, end=' h = ')
                    while line[j].isdigit() and line[j] != '\n':
                        j += 1
                    h = int(line[i+4:j])
                    #print(' Height: ', h, end=' ')

                    '''
                    print('Units: ', end='')
                    if line[j] !='\n' and (line[j:j+2] == 'cm' or line[j:j+2] == 'in'):
                        print(line[j:j+2])
                    else:
                        print('INVALID')
                    '''
                    
                    if line[j:j+2] == 'cm':
                        if h >= 150 and h <= 193:
                            parts[3] = True
                       # else:
                       #     print('non-valid cm hieght')
                    
                    if line[j:j+2] == 'in':
                        if h >= 59 and h <= 76:
                            parts[3] = True
                       # else:
                       #     print('non valid in hieght')

            if not parts[4]:
                i =  line.find("hcl:")
                i = i+4
                if line[i] == '#':
                    count = 0
                    for j in range(i+1, i+7):
                        if line[j].isalpha():
                            if line[j] >= 'a' and line[j] <= 'f':
                                count += 1
                        elif line[j].isdigit():
                            if int(line[j]) >= 0 and int(line[j]) <= 9:
                                count += 1
                    if count == 6:
                        parts[4] = True

            if not parts[5]:
                i = line.find("ecl:")
                i += 4
                ecl = line[i:i+3]
                for j in range(7):
                    if ecl == valid_ecl[j]:
                        parts[5] = True
                        #print(index, valid_ecl[j], ecl)
                
                #if not parts[5]:
                #    print(index, line[i:i+3])

            if not parts[6]:
                i = line.find("pid:")
                if i > -1:
                    i += 4
                    if line[i].isdigit():
                        count = 0
                        if index == 36:
                            print('breakpoint')
                        for j in range(i+1, i+10):
                            if j < len(line):
                                if  line[j].isdigit() and int(line[j]) >= 0 and int(line[j]) <= 9:
                                     count += 1
                        
                        if count == 8:
                            parts[6] = True
                            print(index, 'VALID', line[i-4:i+9])
                        else:
                            print(index, 'invalid', line[i-4:i+10] )

           
        
        #if there is no '\n' inthe line then it must be the last line
        if line.find('\n') < 0:
            if all(parts):
                valid += 1

    print('\nValid Passports: ', valid, '\n')