with open('faculty_list.csv', 'r') as istr:
    with open('output.csv', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + ',password'
            print(line, file=ostr)