#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
3 3
1 3
2 3
2 10
3 100
1 1

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
PC=[set() for _ in range(N+1)]
todo=collections.deque()
C=[0]*(N+1)
Ans=''

for i in range(1,N):
  a,b=map(int,input().split())
  G[a].append(b)

def dfs(G,v):
  if len(G[v])==0:
    PC[v].add(v)
    return []
    
  else:
    for i in range(len(G[v])):
      PC[v].add(v)
      next_v=G[v][i]
      PC[v].add(next_v)
      PC[v] |= set(dfs(G,next_v))
    return PC[v]

dfs(G,1)

for q in range(Q):
  p,x=map(int,input().split())
  for r in PC[p]:
    C[r]+=x

for i in range(1,N+1):
  Ans+=str(C[i])+' '

print(Ans)


#再帰で下りていく時、PCにGの内容を入れる
#nextが無くなったら呼び出し元のPCに自分のPCを入れる
#同様に呼び出し元のPCに自分のPCを入れていく




    




