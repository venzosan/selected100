#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7

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

M,N=map(int,input().split())
K=int(input())
mp=[list(input()) for _ in range(M)]
res=np.array([list(map(int,input().split())) for _ in range(K)])

J=np.zeros((M+1,N+1),'uint64')
O=np.zeros((M+1,N+1),'uint64')
I=np.zeros((M+1,N+1),'uint64')

for i in range(1,M+1):
  for j in range(1,N+1):
    if mp[i-1][j-1]=='J':
      J[i][j]=1
    elif mp[i-1][j-1]=='O':
      O[i][j]=1
    else:
      I[i][j]=1

r_J=J.cumsum(axis=0).cumsum(axis=1)
r_O=O.cumsum(axis=0).cumsum(axis=1)
r_I=I.cumsum(axis=0).cumsum(axis=1)

for k in range(K):
  br=res[k][2]
  bc=res[k][3]
  wr=res[k][2]
  wc=res[k][1]-1
  hr=res[k][0]-1
  hc=res[k][3]
  sr=res[k][0]-1
  sc=res[k][1]-1

  big_J=r_J[br][bc]
  w_J=r_J[wr][wc]
  h_J=r_J[hr][hc]
  small_J=r_J[sr][sc]
  Ans_J = big_J - w_J - h_J + small_J

  big_O=r_O[br][bc]
  w_O=r_O[wr][wc]
  h_O=r_O[hr][hc]
  small_O=r_O[sr][sc]
  Ans_O = big_O - w_O - h_O + small_O

  big_I=r_I[br][bc]
  w_I=r_I[wr][wc]
  h_I=r_I[hr][hc]
  small_I=r_I[sr][sc]
  Ans_I = big_I - w_I - h_I + small_I

  print(Ans_J,Ans_O,Ans_I)
  




