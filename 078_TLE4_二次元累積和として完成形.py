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

#J=[[0]*(N+1) for _ in range(M+1)]
#O=[[0]*(N+1) for _ in range(M+1)]
#I=[[0]*(N+1) for _ in range(M+1)]
JOI=[[[0]*3 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1):
  for j in range(1,N+1):
    JOI[i][j][0]=JOI[i-1][j][0]+JOI[i][j-1][0]-JOI[i-1][j-1][0]
    JOI[i][j][1]=JOI[i-1][j][1]+JOI[i][j-1][1]-JOI[i-1][j-1][1]
    JOI[i][j][2]=JOI[i-1][j][2]+JOI[i][j-1][2]-JOI[i-1][j-1][2]

    if mp[i-1][j-1]=='J':
      JOI[i][j][0]+=1
    elif mp[i-1][j-1]=='O':
      JOI[i][j][1]+=1
    elif mp[i-1][j-1]=='I':
      JOI[i][j][2]+=1

#print(JOI)
Ans_J=0
Ans_O=0
Ans_I=0

for k in range(K):
  br=res[k][2]
  bc=res[k][3]
  wr=res[k][2]
  wc=res[k][1]-1
  hr=res[k][0]-1
  hc=res[k][3]
  sr=res[k][0]-1
  sc=res[k][1]-1

  Ans_J = JOI[br][bc][0] - JOI[wr][wc][0] - JOI[hr][hc][0] + JOI[sr][sc][0]
  Ans_O = JOI[br][bc][1] - JOI[wr][wc][1] - JOI[hr][hc][1] + JOI[sr][sc][1]
  Ans_I = JOI[br][bc][2] - JOI[wr][wc][2] - JOI[hr][hc][2] + JOI[sr][sc][2]

  print(Ans_J,Ans_O,Ans_I)
  




