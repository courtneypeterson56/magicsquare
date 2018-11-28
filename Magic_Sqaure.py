# Peterson, Courtney

# This program creates an odd-sided Magic Square, where the sum of each row, column and diagonal adds up to the same number.


import random

SquareSide = random.randint(3, 14)
if SquareSide%2 == 0:
    SquareSide = SquareSide +1

def MagicSquare(SquareSide):
    rows=0
    col=SquareSide/2
    k =[[0 for i in range(SquareSide)] for j in range(SquareSide)]
    for i in range(1,SquareSide*SquareSide+1):
        k[rows][col]= i
        br = rows+1
        bc = col+1
        rows=(rows+SquareSide-1)%SquareSide
        col=(col+1)%SquareSide
        if k[rows][col]!=0:
             rows=br
             col=bc-1
    for row in k:
        print
        print row
    result = sum(row)
    print
    print "The sum of each row, column, and diagonal is:", result

print "This program creates an odd-sided Magic Square,\
where the sum of each row, column and diagonal \
adds up to the same number."
print
print "Input size of an nxn odd-sided square:", SquareSide
MagicSquare(SquareSide)
