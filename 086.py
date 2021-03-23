#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
6 5
1 2
2 3
3 4
4 5
5 6

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

N,M=map(int,input().split())
E=[list(map(int,input().split())) for _ in range(M)]
Ans=0

for i in range(M):
  UF=UnionFind(N)

  for j in range(M):
    a,b=map(int,E[j])
    if i==j:
      ta=a
      tb=b
      continue
    else:
      UF.unite(a,b)

#チェック方法を修正
  #ch=UF.find(1)
  #for u in range(2,N+1):
  #  if UF.find(u)!=ch:
  #    #print(ch)
  #    #print(UF.par[u])
  #    Ans+=1
  #    break
  if not UF.same(ta,tb):
    Ans+=1
  
print(Ans)
