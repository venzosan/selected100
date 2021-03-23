#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
10
61049214 115057849 356385814 932678664 505961980 877482753 476308661 571830644 210047210 873430114

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

N=int(input())
A=list(map(int,input().split()))

s=[0]*(N+1)

for i in range(N):
  s[i+1]=s[i]+A[i]

ma=[0]*(N+1)

for span in range(1,N+1):
  for left in range(1,N-span+2):
    ma[span]=max(ma[span],s[left+span-1]-s[left-1])

for i in range(1,N+1):
  print(ma[i])








