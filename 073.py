#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
3 3

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

X,Y=map(int,input().split())
mod=10**9+7

if (2*Y-X)%3==0 and (2*X-Y)%3==0 and max(X,Y)<=min(X,Y)*2:
  w=(2*Y-X)//3
  h=(2*X-Y)//3
  nume=1
  deno1=1
  deno2=1
#  print(w)
#  print(h)

  for i in range(2,w+h+1):
    nume*=i
    nume=nume%mod

  for i in range(2,w+1):
    deno1*=i
    deno1=deno1%mod

  for i in range(2,h+1):
    deno2*=i
    deno2=deno2%mod

  deno=(deno1*deno2)%mod

  deno=pow(deno,mod-2,mod)
  print((nume*deno)%mod)

else:
  print(0)

