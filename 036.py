#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
3 9
2 1
3 1
5 2
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
      dp[i+1][w]=max(dp[i+1][w],dp[i][w-vw[i][1]]+vw[i][0],dp[i+1][w-vw[i][1]]+vw[i][0])
    dp[i+1][w]=max(dp[i+1][w],dp[i][w])

#print(dp[0:W+1][0:N+1])
print(dp[N][W])

#精選100問035との違いは28行目、dp[i+1][w-vw[i][1]]+vw[i][0]が入っている点
#これにより複数回の選択を許している

#参照ブログ：No Caffeine, No Life 
#AOJ DPL_1_C：ナップザック問題 (同じ種類の品物はいくつでも選ぶことができる場合)　動的計画法
#http://prdc.hatenablog.com/entry/2017/09/12/140232