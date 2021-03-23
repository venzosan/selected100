#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
2 1
1000000000 1000000000
2

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob
import collections
import heapq
import math

N,Q=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))

mod=10**9+7
ar=[0]*(N+1)
for i in range(1,N):
  ar[i+1]=ar[i]+pow(a[i-1],a[i],mod)

Ans=0
start=1
for i in range(Q):
  Ans+=abs(ar[c[i]]-ar[start])
  Ans=Ans%mod
  start=c[i]
else:
  Ans+=abs(ar[1]-ar[start])
  Ans=Ans%mod

print(Ans)