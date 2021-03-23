#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 8
2 2
2 4
########
#.#....#
#.###..#
#......#
########

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
Maze=[input() for _ in range(R)]

seen=[[-1]*C for _ in range(R)]
todo=collections.deque()

R-=1;C-=1;sy-=1;sx-=1;gy-=1;gx-=1

todo.append([sy,sx])
seen[sy][sx]=0
ch=[[1,0],[0,-1],[-1,0],[0,1]]

while len(todo)!=0:
  v=todo.popleft()
  for i in range(len(ch)):
    ny=v[0]+ch[i][0]
    nx=v[1]+ch[i][1]

    if seen[ny][nx]!=-1:
      continue
    elif Maze[ny][nx]=='#':
      seen[ny][nx]=-2
    else:
      todo.append([ny,nx])
      seen[ny][nx]=seen[v[0]][v[1]]+1
      if ny==gy and nx==gx:
        break
  if ny==gy and nx==gx:
    print(seen[gy][gx])
    break











