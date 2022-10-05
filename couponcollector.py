import sys,random

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of each of n types
def get_coupen(n):
    return random.randrange(0,n)
    
def collect(n):
    count,collected_count=0,0
    is_collected=[False]*n
    
    while collected_count<n:
          count+=1
          value=get_coupen(n)
          if not is_collected[value]:
              collected_count+=1
              is_collected[value]=True
    return count
        
        
n=int(sys.argv[1])
z=collect(n)
print(z)

# python couponcollector.py 1000
# 8507

# python couponcollector.py 1000
# 6602

# python couponcollector.py 1000000
# 14238292