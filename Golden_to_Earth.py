import sys


count = 0
filename = input('Print filename here: ')

with open(filename, "r") as f:
    sys.stdout = open('%s (converted).txt' % f.name, 'a')
    
    for line in f:
        converted_line = line.split()[0:3]  # split each line and remove last 3 column
       
        if not converted_line:  # if list/line is empty
            count += 1  # increase count but DO NOT PRINT/ WRITE TO FILE
        else:
            converted_line.insert(2, str(count))  # insert between 2nd and 3rd column
            print('\t'.join(converted_line))  # join them and print them with tab delimiter
