#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
8 5
7 5 3 5 4
12 5 8
16 2 1
3 1 5
17 12 17
19 7 5
12 2 19
4 1 3

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
P=list(map(int,input().split()))
c=[list(map(int,input().split())) for _ in range(N-1)]

Nt=[0]*(N+1)
for i in range(M-1):
  if P[i]<P[i+1]:
    Nt[P[i]]+=1
    Nt[P[i+1]]-=1
  else:
    Nt[P[i+1]]+=1
    Nt[P[i]]-=1
    
#print(Nt)
for i in range(N):
  Nt[i+1]+=Nt[i]
#print(Nt)

#pl=[0]*(N)
#coc=[0]*(N)
SP=[0]*(N)
Ans=0

for i in range(1,N):
  #if (c[i-1][0]-c[i-1][2]) % c[i-1][1]==0:
  if c[i-1][2] % (c[i-1][0] - c[i-1][1])==0:
    pl=c[i-1][2] // (c[i-1][0] - c[i-1][1])
  else:
    pl=(c[i-1][2] // (c[i-1][0] - c[i-1][1])) + 1

  #print(pl)
  #print(Nt[i])
  if Nt[i]>=pl:
    Ans+= Nt[i] * c[i-1][1] + c[i-1][2]
    #print(Nt[i] * c[i-1][1] + c[i-1][2])
  else:
    Ans+= Nt[i] * c[i-1][0]
    #print(Nt[i] * c[i-1][0])
print(Ans)

