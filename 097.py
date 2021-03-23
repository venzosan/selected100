#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 1000000000
6 6 2 6 2

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
import time
#import glob
import heapq
import math
import collections
import numpy as np

#read = sys.stdin.buffer.read
#readline = sys.stdin.buffer.readline
#readlines = sys.stdin.buffer.readlines

def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y,x%y)

def lcm(x, y):
  return x // gcd(x,y) * y

N,M=map(int,input().split())
a=list(map(int,input().split()))
wk=a[0]
cnt=1
a_set=set()

while wk%2==0:
  cnt*=2
  wk=wk//2

for i in range(N):
  if (a[i]//cnt)%2==0 and a[i]//cnt!=1:
    print(0)
    break
else:
  for j in range(N):
    a_set.add(a[j]//2)

  l=1

  for s in a_set:
    x=l
    y=s
    l=lcm(x,y)

  Ans1=(M//l)//2
  Ans2=(M//l)%2

  print(Ans1+Ans2)