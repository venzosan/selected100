#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
3
1 0 1
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
import time
#import glob
import heapq
#import math
import collections
import numpy as np
import copy

#read = sys.stdin.buffer.read
#readline = sys.stdin.buffer.readline
#readlines = sys.stdin.buffer.readlines

n=int(input())
lgt=list(map(int,input().split()))
#print(lgt)
start=lgt[0]
end=-1
cnt=1
nr=[]
Ans=0

for i in range(n-1):
  if lgt[i]!=lgt[i+1]:
    cnt+=1
  else:
    end=lgt[i]
    nr.append([start,end,cnt])
    Ans=max(cnt,Ans)
    start=lgt[i+1]
    cnt=1
else:
  if lgt[-1]!=lgt[-2]:
    nr.append([start,lgt[-1],cnt])
  else:
    nr.append([lgt[-1],lgt[-1],cnt])
  Ans=max(cnt,Ans)

if len(nr)<3:
  Ans=n
else:
  for i in range(len(nr)-2):
    Ans=max(Ans,nr[i][2]+nr[i+1][2]+nr[i+2][2])

#print(nr)
print(Ans)










