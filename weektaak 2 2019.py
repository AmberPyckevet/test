# open file

# read lines

# process line

# advance counters

# print counts

# cg% berekenen

# print cg%
from typing import List

file = 'C:\\Users\\Amber.DESKTOP-MANUOL0\\Documents\\School\\han\\genes\\test_dna.txt'
f = open(file, "r")
lines = f.readlines()
skipline = True
for line in lines:
    if skipline == False:
        aantal_a = line.count("a")
        aantal_t = line.count("t")
        aantal_c = line.count("c")
        aantal_g = line.count("g")
        lengte = len(line)
        print((aantal_c+aantal_g)/lengte)
    skipline = False

