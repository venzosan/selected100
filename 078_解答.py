#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7

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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

H,W = map(int,readline().split())
Q = int(readline())
grid = np.zeros((H+1,W+1),'S1')
for i in range(1,H+1):
    grid[i,1:] = np.frombuffer(readline().rstrip(),'S1')

query = np.array(read().split(),np.int32)

J = (grid == b'J').cumsum(axis=0).cumsum(axis=1)
O = (grid == b'O').cumsum(axis=0).cumsum(axis=1)

del grid

A = query[::4] - 1
B = query[1::4] - 1
C = query[2::4]
D = query[3::4]

J = J[C,D] + J[A,B] - J[C,B] - J[A,D]
O = O[C,D] + O[A,B] - O[C,B] - O[A,D]
I = (C-A) * (D-B) - J - O

del query,A,B,C,D

print('\n'.join('{} {} {}'.format(j,o,i) for j,o,i in zip(J,O,I)))
  




