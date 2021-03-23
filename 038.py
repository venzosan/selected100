#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
1
abc
xyb
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

def lcs(a: str, b: str):
    L = []
#    r=1
    for bk in b:
#        print('ループ：'+str(r)+'回目')
        bgn_idx = 0  # 検索開始位置
        for i, cur_idx in enumerate(L):
            # ※1
            chr_idx = a.find(bk, bgn_idx) + 1
#            print('chr_idx：'+str(chr_idx))
#            print('bk：'+str(bk))
#            print('bgn_idx：'+str(bgn_idx))

            if not chr_idx:
#                print('chr_idxなしでbreak')
                break
            L[i] = min(cur_idx, chr_idx)
#            print('リストL：')
#            print(L)
            bgn_idx = cur_idx
#            print('bgn_idxをcur_idxに書き換え：'+str(bgn_idx))
        else:
            # ※2
            chr_idx = a.find(bk, bgn_idx) + 1
#            print('elseブロック chr_idx：'+str(chr_idx))
#            print('elseブロック bk：'+str(bk))
#            print('elseブロック bgn_idx：'+str(bgn_idx))
            if chr_idx:
                L.append(chr_idx)
#                print('elseブロック リストL(chr_idx追加後)：')
#                print(L)
#        r+=1
    return len(L)

N=int(input())
X=''
Y=''

for r in range(N):
  X=input()
  Y=input()

  print(lcs(X,Y))

