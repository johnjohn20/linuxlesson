#!/usr/bin/python3
import numpy as np
import argparse

parser= argparse.ArgumentParser(description='Prints out a nxn matrix')
parser.add_argument('--first_dimension', '-x', default=10)
parser.add_argument('--second_dimension', '-y', default=10)
args= parser.parse_args()

x= int(args.first_dimension)
y= int(args.second_dimension)

table = np.random.rand(x,y)

for i in range(x):
    for j in range(y):
        print ("%.4f" %table[i][j], end="\t")
    print(end="\n")
