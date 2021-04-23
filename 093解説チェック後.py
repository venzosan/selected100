#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
17 17 2
12345678912345678
23456789123456789
34567891234567891
45678912345678912
56789123456789123
67891234567891234
78912345678912345
89123456789123456
91234567891234567
12345678912345678
23456789123456789
34567891234567891
45678912345678912
56789123456789123
67891234567891234
78912345678912345
89123456789123456

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
#import itertools
#import copy
#import time
#import glob
#import heapq
#import math
#import collections
#import copy
#import numpy as np
#from matplotlib import pyplot

#read = sys.stdin.buffer.read
#readline = sys.stdin.buffer.readline
#readlines = sys.stdin.buffer.readlines

import copy

def main():
    H, W, K = map(int,input().split())
    st = [list(map(int, input())) for _ in range(H)]
    #print(st)
    Ans = 0

    if K > 3:
        pass
    else:
        for y in reversed(range(H)):
            for x in range(W):
                wk = copy.deepcopy(st)
                wk[y][x] = 0
                secAns = 0
                cnt = 0
                End = False

                #初回石落とし処理
                for i in reversed(range(y)):
                    #if wk[i][x] != 0 and wk[i+1][x] == 0:
                    wk[i+1][x] = wk[i][x]
                wk[0][x] = 0

                while not End:
                    #石消し処理
                    wkAns = 0
                    for i in reversed(range(y + 1)):
                        for j in range(W - K + 1):
                            r = j + 1
                            while r <= W - 1 and wk[i][j] == wk[i][r]:
                                r += 1
                            if r - j >= K:
                                for sn in range(j, r):
                                    wkAns += wk[i][sn]
                                    wk[i][sn] = 0
                    secAns += (2 ** cnt) * wkAns
                    cnt += 1
                
                    #石落とし処理
                    End = True
                    for i in reversed(range(y)):
                        for j in range(W):
                            if wk[i][j] != 0 and wk[i+1][j] == 0:
                                sn = i + 1
                                while sn <= H - 1 and wk[sn][j] == 0:
                                    sn += 1
                                wk[sn-1][j] = wk[i][j]
                                wk[i][j] = 0
                                End = False

                Ans = max(Ans, secAns)
    print(Ans)

if __name__ == '__main__':
    main()

# K>=4の時、消せる石がないため0を出力するコードを追加
# ※制約より、初期状態では隣り合う石の色は異なっているため、
# 1つ石を消すだけでは最大3つまでしか同じ色が並ばない

# このコードでもpythonだと1ケースTLE


