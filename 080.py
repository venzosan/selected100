#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4 7 10 240
17 12 15 18 19 15 23
22 12 41 16 27 10 10
15 69 18 11 10 23 15
12 20 13 12 17 18 15

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
import time
#import glob
import heapq
import math
import collections
import numpy as np

#read = sys.stdin.buffer.read
#readline = sys.stdin.buffer.readline
#readlines = sys.stdin.buffer.readlines

H,W,K,V=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]

S=[[0]*(W+1) for _ in range(H+1)]
Ans=0

for i in range(1,H+1):
  for j in range(1,W+1):
    S[i][j] = A[i-1][j-1]
    S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]
    #S[i][j] += i * j * K

for i in range(1,H+1):
  for j in range(1,W+1):
    for k in range(i,H+1):
      for l in range(j,W+1):
        r=S[k][l]-S[i-1][l]-S[k][j-1]+S[i-1][j-1]
        area=(k-i+1)*(l-j+1)
        r+=area*K
        #print(r)
        if r<=V:
          Ans=max(Ans,area)
          #print(area)

print(Ans)

