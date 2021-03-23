#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
12 3
1 2
1 3
2 3
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

F=[0]*45

F[0]=1
F[1]=1

for i in range(2,N+1):
  F[i]=F[i-1]+F[i-2]

print(F[N])



