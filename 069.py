#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
6
1 53
13 91
37 55
19 51
73 91
13 49

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

Q=int(input())
pn=[[] for _ in range(100001)]
rw=[0]*100001
pn[0]=0
pn[1]=0

for i in range(2,100000):
  if pn[i]==[]:
    pn[i]=1
    wk=i+i
    while wk<=100000:
      if pn[wk]==[]:
        pn[wk]=0
      wk+=i

cnt=0

for i in range(3,100000,2):
  if pn[i]==1 and pn[(i+1)//2]==1:
    cnt+=1
  rw[i]=cnt

for q in range(Q):
  l,r=map(int,input().split())
  print(rw[r]-rw[l-2])
  



