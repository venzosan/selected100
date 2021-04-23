#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
3 1 8

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
import copy

#read = sys.stdin.buffer.read
#readline = sys.stdin.buffer.readline
#readlines = sys.stdin.buffer.readlines

a, b, x=map(int, input().split())
x = x / a

if a * b / 2 <= x:
  Ans = math.degrees(math.atan((2 * (a * b - x)) / (a * a)))
else:
  Ans = math.degrees(math.atan((b * b) / (2 * x)))

print(Ans)

