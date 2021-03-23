#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
#import collections

N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]
route=list(itertools.permutations(range(N),N))

cnt=0
amo=0
#print(route)

for r in route:
  for i in range(N-1):
    x=P[r[i]][0]-P[r[i+1]][0]
    y=P[r[i]][1]-P[r[i+1]][1]
    amo+=math.sqrt(x**2+y**2)
  cnt+=1

print(amo/cnt)


