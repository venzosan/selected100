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

def rec(r,c):
  if r==c:
    return 0
    
N=int(input())
R=[]
C=[]
for i in range(N):
  wk1,wk2=map(int,input().split())
  R.append(wk1)
  C.append(wk2)

P=[0]*(N+1)
for i in range(N):
  if i==0:
    P[i]=R[0]
  P[i+1]=C[i]
print(P)

INF=10**9
#INF=-1
dp=[[INF]*(N) for _ in range(N)]
for i in range(N):
  dp[i][i]=0
  if i<=(N-2):
    dp[i][i+1]=P[i]*P[i+1]*P[i+2]
print(dp)

for i in range(N-1):
  for j in range(i+2,N):
    dp[i][j]=min()


#連鎖行列式、以下のブログがいちばんわかりやすかった。
#がぶ飲みミルク珈琲
#https://ttrsq.exblog.jp/24318687/



