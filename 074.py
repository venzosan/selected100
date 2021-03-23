#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
100000
100000

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

n=int(input())
k=int(input())
mod=10**9+7

nume=1
deno1=1
deno2=1

for i in range(2,n+k):
  nume*=i
  nume=nume % mod
  #print(nume)

for i in range(2,k+1):
  deno1*=i
  deno1=deno1 % mod
  #print(deno1)


for i in range(2,n):
  deno2*=i
  deno2=deno2 % mod
  #print(deno2)

deno=(deno1*deno2) % mod
#print(deno)

rdeno=pow(deno,mod-2,mod)

print((nume*rdeno) % mod)
