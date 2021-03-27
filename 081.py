#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4
1000000 1000000
1000000 1000000
0 1000000
1 1000000

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

n=int(input())

p=[list(map(int,input().split())) for _ in range(n)]
s=[0] * 1000002

for i in range(n):
  s[p[i][0]]+=1
  s[p[i][1]+1]-=1

for i in range(1,len(s)):
  s[i]+=s[i-1]
s[1000001]=0

print(max(s))