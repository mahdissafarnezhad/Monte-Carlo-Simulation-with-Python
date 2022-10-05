import sys
import random
import stdio

 Accept an integer moves as a command-line argument. Read a
# transition matrix from standard input. Perform moves moves as
# prescribed by the transition matrix, and write to standard output
# the relative frequency of hitting each page.

moves=int(sys.argv[1])
n=stdio.readInt() # Discard the second int of standard input.
stdio.readInt()

# Read the transition matrix from standard input.
# p[i][j] is the probability that the surfer moves from
# page i to page j.
p=[[0.0]*n for i in range (n)]

for i in range(n):
    for j in range(n):
        p[i][j]=stdio.readFloat()
# Perform the simulation, thus computing the hits array.
# hits[i] is the number of times the surfer hits page i.
hits=[0]*n
page=0 # Start at page 0.

for i in range(moves):
 # Make one random move.
    r=random.random()
    total=0.0
    for j in range (n):
    # Find interval containing r.
         total+=p[page][j]
         if r<total:
            page=j
            break
    hits[page]+=1
# Write the page ranks.
for v in hits:
    print('%8.5f' %(1*v/moves),end=' ')


#python transition.py<small.txt|randomsurfer.py 1000000
#python transition.py<medium.txr|randomsurfer.py 1000000




       