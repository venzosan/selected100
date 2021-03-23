#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4 5 0
0 1 1
0 2 4
1 2 2
2 3 1
1 3 5
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections
import heapq

V,E,r=map(int,input().split())
edge=[list(map(int,input().split())) for _ in range(E)]
G=[[] for _ in range(V)]

for i in range(E):
  G[edge[i][0]].append([edge[i][1],edge[i][2]])

INF=10**10
dist=[INF]*V
dist[r]=0

hq=[]
heapq.heappush(hq,[dist[r],r])

while hq!=[]:
  d=hq[0][0]
  v=hq[0][1]
  heapq.heappop(hq)

  if d>dist[v]:continue

  for to in range(len(G[v])):
    next_v=G[v][to][0]
    w=G[v][to][1]
    if dist[next_v] > d+w:
      dist[next_v] = d+w
      heapq.heappush(hq,[dist[next_v],next_v])

for i in range(V):
  if dist[i]==INF:
    print('INF')
  else:
    print(dist[i])

#pythonのheapqは0インデックスで、ルートが最小値になる仕様





