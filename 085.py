#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0
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

class UnionFind():
  def __init__(self, n):
    self.par = [i for i in range(n+1)]
    self.rank = [0] * (n+1)
    
  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if self.rank[x] < self.rank[y]:
      self.par[x] = y
    else:
      self.par[y] = x
      
    if self.rank[x] == self.rank[y]:
      self.rank[x] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

n,q=map(int,input().split())

UF=UnionFind(n-1)

for i in range(q):
  c,x,y=map(int,input().split())
  if c==0:
    UF.unite(x,y)
  else:
    if UF.same(x,y):
      print(1)
    else:
      print(0)


