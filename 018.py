#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5
1 1 2 2 3
2
1 2
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

def binary_search(Ar,key):
  left=0
  right=len(Ar)-1

  while right>=left:
    mid=left+(right-left)//2
    if Ar[mid]==key:
      return mid
    elif Ar[mid]>key:
      right=mid-1
    elif Ar[mid]<key:
      left=mid+1
  return -1

n=int(input())
S=list(map(int,input().split()))
q=int(input())
T=list(map(int,input().split()))
Ans=0

for i in range(q):
  if binary_search(S,T[i])!=-1:
    Ans+=1

print(Ans)









