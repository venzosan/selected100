#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
10 10 10
1 6
2 9
4 5
4 7
4 7
5 8
6 6
6 7
7 9
10 10
1 8
1 9
1 10
2 8
2 9
2 10
3 8
3 9
3 10
1 10

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import copy
import time
import glob
import heapq
import math
import collections
import numpy as np

#read = sys.stdin.buffer.read
#readline = sys.stdin.buffer.readline
#readlines = sys.stdin.buffer.readlines

N,M,Q=map(int,input().split())
T=[list(map(int,input().split())) for _ in range(M)]
Q=[list(map(int,input().split())) for _ in range(Q)]

S=[[0]*(N+1) for _ in range(N+1)]

for i in range(M):
  S[T[i][0]][T[i][1]]+=1

for i in range(1,N+1):
  for j in range(1,N+1):
    S[i][j]+=S[i][j-1]

for q in Q:
  Ans=0
  m=0
  for i in range(1,q[1]+1):
    Ans+=S[i][q[1]]-S[i][q[0]-1]
    if i==q[0]-1:
      m=Ans
  Ans-=m
  print(Ans)

