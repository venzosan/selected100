#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
6
00:00:00 03:00:00
01:00:00 03:00:00
02:00:00 03:00:00
03:00:00 04:00:00
03:00:00 05:00:00
03:00:00 06:00:00
0
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

while True:
  n=int(input())
  if n==0:
    break
  else:
    tr=[list(map(str,input().split())) for _ in range(n)]
    calc=[]
    for i in range(n):
      calc.append([tr[i][0],1])
      calc.append([tr[i][1],-1])

    calc.sort()
    wk=calc[0][1]
    Ans=0

#判定の順番を間違えて何度かWA出した
#(wkに足してから同時刻チェックをしていた)
    for i in range(1,len(calc)):
      if calc[i-1][0]!=calc[i][0]:
        Ans=max(wk,Ans)
      wk+=calc[i][1]
    else:
      Ans=max(wk,Ans)

    print(Ans)


      