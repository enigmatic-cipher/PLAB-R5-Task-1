"""
Given n as input. Print following pattern using For loop.
Input-> n = 2
Output-> 
1 
121 
12321 
1234321
"""

n = 4
for i in range(1,n+1):
  st = ""
  st = st + str(i)
  for j in range(i-1,0,-1):
    st = st + str(j)
  print(st)
  