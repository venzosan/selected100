#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
20
4
4
12
8
16
7
7
11
8
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

dis=int(input())
store=int(input())
order=int(input())
st_p=[0]*(store+1)

for i in range(1,store):
  st_p[i]=int(input())
  
st_p[store]=dis
st_p.sort()

ord_p=[0]*order
for i in range(order):
  ord_p[i]=int(input())

Ans=0

def binary_search(Ar,key):
  left=0
  right=len(Ar)-1

  while right-left>1:
    mid=left+(right-left)//2
    if Ar[mid]==key:
      return mid
    elif Ar[mid]>key:
      right=mid
    elif Ar[mid]<key:
      left=mid
  return right

for i in range(order):
  p=binary_search(st_p,ord_p[i])
  Ans+=min(abs(ord_p[i]-st_p[p]),abs(ord_p[i]-st_p[p-1]))
  
print(Ans)









