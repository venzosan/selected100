#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5
1 5 7 10 21
4
2 4 17 8
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob

N=int(input())
Pt=list(map(int,input().split()))
M=int(input())
Q=list(map(int,input().split()))
Pt_set=set()


for bit in range(2**N):
  cnt=0
  for i in range(N):
    if bit & (1<<i):
      cnt+=Pt[i]
  Pt_set.add(cnt)

for i in range(M):
  if Q[i] in Pt_set:
    print('yes')
  else:
    print('no')




