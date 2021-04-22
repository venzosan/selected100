#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
8
1
0
1
1
0
0
0
1

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
go=[int(input()) for _ in range(n)]
sta=[[go[0],1]]

for i in range(1,n):
  if i%2==0: #奇数
    if go[i]==sta[-1][0]:
      sta[-1][1]+=1
    else:
      sta.append([go[i],1])

  else: #偶数
    if go[i]==sta[-1][0]:
      sta[-1][1]+=1
    else:
      if len(sta)==1:
        sta[-1][0]=go[i]
        sta[-1][1]+=1
      else:
        sta[-2][1]+=sta[-1][1]+1
        del sta[-1]

Ans=0
for s in sta:
  if s[0]==0:
    Ans+=s[1]

print(Ans)




