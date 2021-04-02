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

#上頂点にXを入れる
  Nail[A-1][B-1]=max(Nail[A-1][B-1],X+1)

#print(Nail)

for i in range(N-1):
  for j in range(len(Nail[i])):
    Nail[i+1][j]=max(Nail[i+1][j],Nail[i][j]-1)
    Nail[i+1][j+1]=max(Nail[i+1][j+1],Nail[i][j]-1)
    #print(Nail)

Ans=0

for i in range(N):
  for j in range(len(Nail[i])):
    if Nail[i][j]!=0:
      Ans+=1

print(Ans)

#PythonだとTLE、PyPyでAC
