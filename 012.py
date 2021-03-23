#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
12 3
1 2
1 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob
import collections

N,M=map(int,input().split())
P=set(tuple(map(int,input().split())) for _ in range(M))
ch=[]
Ans=1

for bit in range(1,2**N):
  ch.clear()
  for i in range(N):
    if bit & (1<<i):
      ch.append(i+1)

  if len(ch)>1:
    for s in itertools.combinations(ch,2):
      if s not in P:
        break
    else:
      Ans=max(Ans,len(ch))

print(Ans)



