#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
1 1
0 0 5
6 -3

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

N,M=map(int,input().split())
C=[]
rMin=999

for i in range(N):
  C.append(list(map(int,input().split())))
  C[i][0]+=100
  C[i][1]+=100
  C[i].append(0)
  rMin=min(rMin,C[i][2])

for i in range(M):
  C.append(list(map(int,input().split())))
  C[N+i][0]+=100
  C[N+i][1]+=100
  C[N+i].append(-1)
  C[N+i].append(1)

for i in range(N,N+M):
  for j in range(N+M):
    if i==j:
      pass
    else:
      wk=0
      X=abs(C[i][0]-C[j][0])
      Y=abs(C[i][1]-C[j][1])
      if C[j][3]==0:
        rMin=min(rMin,(X*X+Y*Y)**0.5-C[j][2])
      else:
        rMin=min(rMin,((X*X+Y*Y)**0.5)/2)

print(rMin)

        












