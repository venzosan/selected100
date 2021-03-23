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
wh_mod=1
w_mod=1
h_mod=1

for i in range(1,W+H-2+1):
  wh_mod*=i
  wh_mod=wh_mod%mod

for i in range(1,W-1+1):
  w_mod*=i
  w_mod=w_mod%mod

for i in range(1,H-1+1):
  h_mod*=i
  h_mod=h_mod%mod

wh_div=(w_mod*h_mod)%mod
rg=pow(wh_div,mod-2,mod)
#print(wh_div)
print((wh_mod*rg)%mod)

  
#逆元の理解にとても苦労した。
#763955619の1000000005乗が逆元になるなんて俄かに信じられないじゃん……。
#@mts1104_mlさんにそれで大丈夫と教えてもらって助かった。
#下手をしたらわからないまま蓋をしていたかもしれない。

#A÷Bの(mod p)はA×Bの逆元(Bの(p-2)乗)
#掛け算の形になれば余り×余りにしてもOKなので
#逆元求める時にpowで剰余出してる。

