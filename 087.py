#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
2 1
1 2

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
    self.par = [-1 for i in range(n+1)]
    self.rank = [0] * (n+1)
    
  def find(self, x):
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    else:
      if self.rank[x] < self.rank[y]:
        self.par[y] = self.par[y] + self.par[x]
        self.par[x] = y
      else:
        self.par[x] = self.par[x] + self.par[y]
        self.par[y] = x
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def size(self, x):
    return -self.par[self.find(x)]
  
N,M=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(M)]
Ans=[0]*(M+1)
Ans[M]=N*(N-1)//2
#Gr=N
UF=UnionFind(N)
#print(AB)

for i in reversed(range(M)):
  if (UF.size(AB[i][0])!=1 and UF.size(AB[i][1])!=1) and UF.same(AB[i][0],AB[i][1]):
    Ans[i]=Ans[i+1]
    UF.unite(AB[i][0],AB[i][1])
  else:
    Ans[i]=Ans[i+1]-(UF.size(AB[i][0])*UF.size(AB[i][1]))
    UF.unite(AB[i][0],AB[i][1])
  
for i in range(1,M+1):
  print(Ans[i])






