#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import time

N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]
P.sort()
#print(P)
le=len(P)

def nibutan(x,y):
  min_p=0
  max_p=le-1
  while max_p>=min_p:
    tar=min_p+(max_p-min_p)//2
    if P[tar][0]==x and P[tar][1]==y:
      #print('x:'+str(x))
      #print('y:'+str(y))
      #print('min_p:'+str(min_p))
      #print('max_p:'+str(max_p))
      #print('tar:'+str(tar))
      #print('P[tar]:'+ str(P[tar]))
      return True
    elif P[tar][0]>x:
      max_p=tar-1
    elif P[tar][0]<x:
      min_p=tar+1
    elif P[tar][0]==x:
      if P[tar][1]>y:
        max_p=tar-1
      elif P[tar][1]<y:
        min_p=tar+1
  return False

#P_set=set()
#for i in range(le):
#  P_set.add((P[i][0],P[i][1]))

area=0
Ans=0

for i in range(le-1):
  for j in range(i+1,le):
    t1x=P[j][0]-(P[j][1]-P[i][1])
    t1y=P[j][1]+(P[j][0]-P[i][0])
    t2x=P[i][0]-(P[j][1]-P[i][1])
    t2y=P[i][1]+(P[j][0]-P[i][0])

#    if (t1x,t1y) in P_set:
#      if (t2x,t2y) in P_set:
    if nibutan(t1x,t1y):
      if nibutan(t2x,t2y):
        #print(P[i])
        #print(P[j])
        #print(str(t1x)+str(t1y))
        #print(str(t2x)+str(t2y))
        area=(P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2
        #print('area:'+str(area))
        Ans=max(area,Ans)

print(Ans)









  







  

