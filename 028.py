#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
6
1 2 2 4
2 1 5
3 2 5 6
4 0
5 1 4
6 1 6
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

N=int(input())
G=[[] for _ in range(N+1)]
seen=[-1]*(N+1)
todo=collections.deque()

for i in range(1,N+1):
  wk=list(map(int,input().split()))
  for r in range(2,wk[1]+2):
    G[i].append(wk[r])

todo.append(1)
seen[1]=0

while len(todo)!=0:
  v=todo.popleft()
  for i in range(len(G[v])):
    if seen[G[v][i]]!=-1:
      continue
    else:
      todo.append(G[v][i])
      seen[G[v][i]]=seen[v]+1

for i in range(1,N+1):
  print(str(i)+' '+str(seen[i]))







