#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
1
abc
xyb
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

N=int(input())
X=''
Y=''

for r in range(N):
  X=input()
  Y=input()
  leX=len(X)
  leY=len(Y)
  dp=[[0]*(leX+1) for _ in range(leY+1)]
  #print(dp)
  
  #Pythonは典型だと制限時間オーバーで通らない
  for i in range(1,len(X)+1):
    for j in range(1,len(Y)+1):
      if X[i-1]==Y[j-1]:
        dp[j][i]=max(dp[j-1][i-1]+1,dp[j][i])
      else:
        dp[j][i]=max(dp[j-1][i],dp[j][i-1],dp[j][i])

  print(dp[leY][leX])

