#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 30
1 3 1 13
1 3 2 50
1 4 2 80
0 3 4
0 1 2
0 3 5
1 5 3 75
0 4 5
1 4 5 18
0 4 3
0 4 5
1 3 5 34
1 5 1 27
0 4 1
0 1 2
1 3 4 33
0 5 3
0 5 4
0 3 5
0 1 5
0 4 3
0 5 4
0 3 1
0 4 3
0 5 1
0 3 1
0 1 2
0 4 3
0 1 4
0 2 4
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

n,k=map(int,input().split())
G=[[] for _ in range(n)]
INF=10**10

def order(G,s,g):
  used=[False]*n
  dist=[INF]*n
  dist[s]=0

  for i in range(n):
    min_dist=INF
    min_v=-1
    for j in range(n):
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

  if dist[g]==INF:
    return -1
  else:
    return dist[g]


for i in range(k):
  wk=list(map(int,input().split()))

  if wk[0]==0:
    print(order(G,wk[1]-1,wk[2]-1))

  elif wk[0]==1:
    frm=wk[1]-1
    to=wk[2]-1
    wgt=wk[3]
    for e in range(len(G[frm])):
      if to==G[frm][e][0]:
        if wgt<G[frm][e][1]:
          G[frm][e]=[to,wgt]
          for e2 in range(len(G[to])):
            if frm==G[to][e2][0]:
              G[to][e2]=[frm,wgt]
              break
          break
        else:
          break
    else:
      G[wk[1]-1].append([wk[2]-1,wk[3]])
      G[wk[2]-1].append([wk[1]-1,wk[3]])
      
      

      










