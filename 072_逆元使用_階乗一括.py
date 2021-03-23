#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
123 456

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob
import collections
import heapq
import math

W,H=map(int,input().split())

#num=math.factorial(W+H-2)//(math.factorial(W-1)*math.factorial(H-1))
mod=1000000007
wh_mod=pow(math.factorial(W+H-2),1,mod)
w_mod=pow(math.factorial(W-1),1,mod)
h_mod=pow(math.factorial(H-1),1,mod)

wh_div=pow(w_mod*h_mod,1,mod)
rg=pow(wh_div,mod-2,mod)

print((wh_mod*rg)%mod)

#階乗を全部計算してからpowで剰余を求めると毎回計算するよりかなり遅くなった
#（729ms、毎回計算した時は100ms）





