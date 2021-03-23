#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
3
1 2 3
1 2 3

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
P=tuple(map(int,input().split()))
Q=tuple(map(int,input().split()))

D=list(itertools.permutations(range(1,N+1),N))

print(abs(D.index(P)-D.index(Q)))