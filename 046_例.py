#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
6
30 35
35 15
15 5
5 10
10 20
20 25
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections


N = int(input())
R = [0]*N
C = [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())

INF = 10**18
dp = [[INF]*N for i in range(N)]
for i in range(N):
    dp[i][i] = 0
for l in range(1, N):
    for i in range(N-l):
        a0 = R[i]
        c0 = C[i+l]
        dp[i][i+l] = min(a0*C[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))
print(dp[0][N-1])



#区間DPだと初期値設定後に「dp[i][i]=0」が定番っぽい（同じ位置なので距離0）
#2次元テーブルをリストで作る場合はxとyがひっくり返るので以下の書き方がよさそう
#for j in range(XN):
#  for i in range(YN):
#    dp[i][j]= [処理]


