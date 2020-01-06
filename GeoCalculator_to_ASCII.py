import sys


filename = input()

with open(filename, "r") as f:
    sys.stdout = open('%s (converted).txt' % f.name, 'a')
    
    for line in f:
        splitted = line.split(',')
        print('\t'.join(splitted[1:3]))
