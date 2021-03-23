#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
500000000000 500000000000 1000000000000

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

A,B,K=map(int,input().split())
TC=max(A-K,0)
AC=max(B-(max(K-A,0)),0)

print(str(TC)+' '+str(AC))

