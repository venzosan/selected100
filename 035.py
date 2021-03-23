#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 6
5 4
4 3
8 5
7 3
3 2
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

N,W=map(int,input().split())
vw=[list(map(int,input().split())) for _ in range(N)]

dp=[[0]*(W+1) for _ in range(N+1)]

for i in range(N):
  for w in range(W+1):
    if w-vw[i][1]>=0:
      dp[i+1][w]=max(dp[i+1][w],dp[i][w-vw[i][1]]+vw[i][0])
    dp[i+1][w]=max(dp[i+1][w],dp[i][w])

#print(dp[0:W+1][0:N+1])
print(dp[N][W])


