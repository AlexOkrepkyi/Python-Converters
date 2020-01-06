import sys
import numpy as np


filename = input('Please enter the file\'s name: ')
with open(filename, "r") as f:
    sys.stdout = open('%s (converted).txt' % f.name, 'a')

    data = np.loadtxt(f)
    coords = [(el[:3],el[3:]) for el in data]
    output_tuple = [(c[1][0]+c[1][1]/60.+c[1][2]/3600., c[0][0]+c[0][1]/60.+c[0][2]/3600.) for c in coords]

    for i in output:
        output_string = ','.join(map(str, i))
        print(output_string)
