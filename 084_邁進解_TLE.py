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
Nail=[0]*(N*(N+1)//2+1)

for i in range(M):
  A,B,X=map(int,input().split())
  cnt=1
  for j in range(A,A+X+1):
    wkv=j*(j-1)//2+B
    if Nail[wkv]==0:
      Nail[wkv]=1
      #print(Nail)
    for k in range(1,cnt):
      if Nail[wkv+k]==0:
        Nail[wkv+k]=1
        #print(Nail)
    cnt+=1

print(sum(Nail))





