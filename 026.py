#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

N,Q=map(int,input().split())
G=[[] for _ in range(N+1)]
GZ=[[] for _ in range(N+1)]
seen=[-1]*(N+1)
todo=collections.deque()
C=[0]*(N+1)

for i in range(1,N):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

for q in range(Q):
  p,x=map(int,input().split())
  C[p]+=x

todo.append(1)
seen[1]=0

while len(todo)!=0:
  v=todo.pop()
  for r in G[v]:
    if seen[r]!=-1:
      continue
    else:
      GZ[v].append(r)
      todo.append(r)
      C[r]+=C[v]
      seen[r]=0
  
Ans=' '.join([str(c) for c in C])
print(Ans[2:])
    




