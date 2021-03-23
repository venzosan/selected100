#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
13

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

N=int(input())
print(N*(N-1)//2)

