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

N,M,Q=map(int,input().split())
T=[list(map(int,input().split())) for _ in range(M)]
Q=[list(map(int,input().split())) for _ in range(Q)]

Ts=sorted(T,key=lambda x: x[0])
Te=sorted(T,key=lambda x: x[1])
Ss=[0] * (N+1)
Se=[0] * (N+1)

for i in range(M):
  Ss[Ts[i][0]]+=1
  Se[Te[i][1]]+=1

for i in range(1,len(Ss)):
  Ss[i]+=Ss[i-1]
  Se[i]+=Se[i-1]

print(Ss)
print(Se)

for q in Q:
  Ss1=Ss[q[0]-1]
  Ss2=Ss[q[1]]-Ss[q[0]-1]
  Ss3=Ss[q[M]]-Ss[q[1]]
  Se1=Se[q[0]-1]
  Se2=Se[q[1]]-Se[q[0]-1]
  Se3=Se[q[M]]-Se[q[1]]
  
  #Se[q[1]]-Se[q[0]-1]
  print((Se[q[1]]-Se[q[0]-1])-(Ss[q[0]-1]-Se[q[0]-1]))

#上記コードだと区間開始前～区間終了後を走る列車が2回引かれる
#いろいろ考えたが、この組み合わせの加減で対象を抽出するのは無理そう
