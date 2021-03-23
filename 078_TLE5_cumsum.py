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
mp_2pre=np.array([list(input()) for _ in range(M)])
mp_1pre=np.insert(mp_2pre,0,0,axis=0)
mp=np.insert(mp_1pre,0,0,axis=1)
res=np.array([list(map(int,input().split())) for _ in range(K)])

J=(mp=='J').cumsum(axis=0).cumsum(axis=1)
O=(mp=='O').cumsum(axis=0).cumsum(axis=1)
#I=(mp=='I').cumsum(axis=0).cumsum(axis=1)

for k in range(K):
  br=res[k][2]
  bc=res[k][3]
  wr=res[k][2]
  wc=res[k][1]-1
  hr=res[k][0]-1
  hc=res[k][3]
  sr=res[k][0]-1
  sc=res[k][1]-1

  Ans_J = J[br][bc] - J[wr][wc] - J[hr][hc] + J[sr][sc]
  Ans_O = O[br][bc] - O[wr][wc] - O[hr][hc] + O[sr][sc]
  Ans_I = (res[k][2]-res[k][0]+1) * (res[k][3]-res[k][1]+1) - Ans_J - Ans_O

  print(Ans_J,Ans_O,Ans_I)
  




