#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
65 6
1 2 7 8 12 50
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

N,M=map(int,input().split())
C=list(map(int,input().split()))
inf=10**6

dp=[inf]*(N+1)
dp[N]=0

for i in range(N,0,-1):
  for c in C:
    if i-c>=0:
      dp[i-c]=min(dp[i-c],dp[i]+1)

print(dp[0])




