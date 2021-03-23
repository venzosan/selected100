#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4
1 1 2
2 1 4
3 0
4 1 3
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
Ans=[]
for i in range(N):
  Ans.append([i+1,0,0])

#num=1
seen=[False]*(N+1)
#seen[1]=True
#Ans[0][1]=num
#num+=1

def dfs(G,v):
  #G・Ans添字：0、G・Ans中身：1、todo・seen：1
  while len(todo)!=0:
    v=todo.pop()
    for i in range(2,2+G[v-1][1]):
      next_v=G[v-1][i]
      if seen[next_v]:
        continue
      else:
        seen[next_v]=True
        Ans[v-1][1]=num
        num+=1
        todo.append(next_v)

      if seen[G[v][i]:
        continue
      else:
        seen[G[v][i]]=True
        Ans[G[v][i]]
        todo.append(G[v][i])



todo=collections.deque()
todo.append(1)



#G・Ans添字：0、G・Ans中身：1、todo・seen：1
#while len(todo)!=0:
#  v=todo.pop()
#  for i in range(2,2+G[v-1][1]):
#    next_v=G[v-1][i]
#    if seen[next_v]:
#      continue
#    else:
#      seen[next_v]=True
#      Ans[v-1][1]=num
#      num+=1
#      todo.append(next_v)

#    if seen[G[v][i]:
#      continue
#    else:
#      seen[G[v][i]]=True
#      Ans[G[v][i]]
#        todo.append(G[v][i])
        




  



