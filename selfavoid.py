import sys
import random

# Accept integers n and trialCount as command-line arguments. Do
# trialCount random self-avoiding walks in an n-by-n lattice. 
# Write to standard output the percentage of dead ends encountered.

n=int(sys.argv[1])
trials=int(sys.argv[2])
dead_ends=0

for t in range(trials):
    a=[[False]*n for i in range (n)]
    # Create an n-by-n array, with all elements set to False.
    x,y= n//2,n//2
    while 0<x<n-1 and 0<y  <n-1:
    # Check for dead end and make a random move.
         if a[x-1][y] and a[x+1][y] and a[x][y+1] and a[x][y-1]:
             dead_ends+=1
             break
         a[x][y]=True
         r=random.random()
         if r< 0.25:
            if not a[x+1][y]: x+=1
         elif r< 0.5:
            if not a[x-1][y]: x-=1
         elif r< 0.75:
            if not a[x][y+1]: y+=1
         else:
            if not a[x][y-1]:y-=1
print(100*dead_ends//trials)


# python selfavoid.py 5 100
# 0% dead ends

# python selfavoid.py 20 100
# 27% dead ends

# python selfavoid.py 40 100
# 80% dead ends

# python selfavoid.py 80 100
# 96% dead ends

# python selfavoid.py 5 1000
# 0% dead ends

# python selfavoid.py 20 1000
# 33% dead ends

# python selfavoid.py 40 1000
# 77% dead ends

# python selfavoid.py 80 1000
# 98% dead ends
