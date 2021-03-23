#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
10
1 3 2 3 4
2 0
3 1 5
4 1 10
5 5 6 7 8 9 10
6 1 2
7 0
8 1 7
9 1 10
10 1 3
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections #counter,deque

N=int(input())
G=[list(map(int,input().split())) for _ in range(N)]
seen=[False]*(N+1)
Ans=[]
for i in range(N):
  Ans.append([i+1,0,0])
num=1

def dfs(G,v):
  global num
  seen[v]=True
  Ans[v-1][1]=num
  num+=1

  for i in range(G[v-1][1]):
    next_v=G[v-1][2+i]
    if next_v==0:
      Ans[G[v-1][0]][2]=num
      num+=1
    elif seen[next_v]:
      continue
    else:
      dfs(G,next_v)
      Ans[next_v-1][2]=num
      num+=1
  
for v in range(1,N):
  if seen[v]:
    continue
  else:
    dfs(G,v)
    Ans[G[v-1][0]-1][2]=num
    num+=1

for a in Ans:
  print(str(a[0])+' '+str(a[1])+' '+str(a[2]))

#再帰を使う場合はtodoの代わりが各再帰になる（todoがない）




        




  



