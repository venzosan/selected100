#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
2

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob
import collections
import heapq

import math

N=int(input())
n_sq=int(math.sqrt(N))
d=2
Ans=str(N)+': '
PF=[]

for d in range(2,n_sq+1):
  while N%d==0:
    PF.append(d)
    N=N//d
  d+=1

if N!=1:
  PF.append(N)

Ans+=' '.join([str(p) for p in PF])
print(Ans)
