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

M,N=map(int,input().split())
K=int(input())
mp=[input() for _ in range(M)]
res=[list(map(int,input().split())) for _ in range(K)]

J=[[0]*(N+1) for _ in range(M+1)]
O=[[0]*(N+1) for _ in range(M+1)]
I=[[0]*(N+1) for _ in range(M+1)]

for i in range(1,M+1):
  for j in range(1,N+1):
    J[i][j]=J[i-1][j]+J[i][j-1]-J[i-1][j-1]
    O[i][j]=O[i-1][j]+O[i][j-1]-O[i-1][j-1]
    I[i][j]=I[i-1][j]+I[i][j-1]-I[i-1][j-1]

    if mp[i-1][j-1]=='J':
      J[i][j]+=1
    elif mp[i-1][j-1]=='O':
      O[i][j]+=1
    elif mp[i-1][j-1]=='I':
      I[i][j]+=1

Ans_J=0
Ans_O=0
Ans_I=0

for k in range(K):
  big_J=J[res[k][2]][res[k][3]]
  w_J=J[res[k][0]-1][res[k][3]]
  h_J=J[res[k][2]][res[k][1]-1]
  small_J=J[res[k][0]-1][res[k][1]-1]
  Ans_J = big_J - w_J - h_J + small_J

  big_O=O[res[k][2]][res[k][3]]
  w_O=O[res[k][0]-1][res[k][3]]
  h_O=O[res[k][2]][res[k][1]-1]
  small_O=O[res[k][0]-1][res[k][1]-1]
  Ans_O = big_O - w_O - h_O + small_O

  big_I=I[res[k][2]][res[k][3]]
  w_I=I[res[k][0]-1][res[k][3]]
  h_I=I[res[k][2]][res[k][1]-1]
  small_I=I[res[k][0]-1][res[k][1]-1]
  Ans_I = big_I - w_I - h_I + small_I

  print(Ans_J,Ans_O,Ans_I)
  




