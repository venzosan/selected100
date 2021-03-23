#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4 6 1
0 1 1
0 2 4
2 0 1
1 2 2
3 1 1
3 2 5
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

V,E,r=map(int,input().split())
edge=[list(map(int,input().split())) for _ in range(E)]
G=[[] for _ in range(V)]

for i in range(E):
  G[edge[i][0]].append([edge[i][1],edge[i][2]])

INF=10**10
used=[False]*V
dist=[INF]*V
dist[r]=0

for i in range(V):
  min_dist=INF
  min_v=-1
  for j in range(V):
    if used[j] or dist[j]>=min_dist:
      continue
    else:
      min_dist=dist[j]
      min_v=j

  if min_v==-1:
    break
  else:
    for to in range(len(G[min_v])):
      next_v=G[min_v][to][0]
      w=G[min_v][to][1]
      dist[next_v]=min(dist[next_v],dist[min_v]+w)

    used[min_v]=True

for i in range(V):
  if dist[i]==INF:
    print('INF')
  else:
    print(dist[i])















