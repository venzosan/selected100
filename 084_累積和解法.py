#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 2
2 2 1
2 1 3
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
Nail=[]

for i in range(1,N+1):
  Nail.append([0]*i)

for i in range(M):
  A,B,X=map(int,input().split())

#上頂点(+)
  Nail[A-1][B-1]+=1

#上頂点の1つ右(-)
  if A>=B+1:
    Nail[A-1][B]-=1

#左下頂点の1つ下(-)
  if A+X+1<=N:
    Nail[A+X][B-1]-=1
    #右下頂点の、1つ下の2つ右(+)
    if B+X+2<=A+X+1:
      Nail[A+X][B+X+1]+=1

#左下頂点の2つ下の1つ右(+)
  if A+X+2<=N:
    Nail[A+X+1][B]+=1
    #右下頂点の、2つ下の2つ右(-)
    if B+X+2<=A+X+2:
      Nail[A+X+1][B+X+1]-=1

for i in range(1,N):
  for j in range(1,len(Nail[i])):
    Nail[i][j]+=Nail[i][j-1]

for i in range(1,N):
  for j in range(len(Nail[i])-1):
    Nail[i][j]+=Nail[i-1][j]

for i in range(1,N):
  for j in range(1,len(Nail[i])):
    Nail[i][j]+=Nail[i-1][j-1]

Ans=0

for i in range(N):
  for j in range(len(Nail[i])):
    if Nail[i][j]!=0:
      Ans+=1

print(Ans)

#PythonだとTLE、PyPyでAC
