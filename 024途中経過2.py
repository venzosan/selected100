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
Gl=[list(map(int,input().split())) for _ in range(N)]
seen=[False]*(N+1)
seen[1]=True

num=1
Ans=[]

for i in range(N):
  Ans.append([i+1,0,0])

Ans[0][1]=num
num+=1

todo=collections.deque()
todo.append(1)

def dfs(G):
#G・Ans添字：0、G・Ans中身：1、todo・seen：1
  global num

  while len(todo)!=0:
    v=todo.pop()
    for i in range(2,2+Gl[v-1][1]):
      print('i:'+str(i))
      next_v=Gl[v-1][i]
      if seen[next_v]:
        continue
      else:
        seen[next_v]=True
        Ans[next_v-1][1]=num
        num+=1
        todo.append(next_v)
        print(todo)

dfs(Gl[0])

for i in range(1,N):
  if seen[i+1]:
    continue
  else:
    dfs(Gl[i])

print(Ans)







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
        




  



