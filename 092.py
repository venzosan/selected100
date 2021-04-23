#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
1
6 9 9 9 9
5
5 9 5 5 9
5 5 6 9 9
4 6 3 6 9
3 3 2 9 9
2 2 1 1 1
10
3 5 6 5 6
2 2 2 8 3
6 2 5 9 2
7 7 7 6 1
4 6 6 4 9
8 9 1 1 8
5 6 1 8 1
6 8 2 1 2
9 6 3 3 5
5 3 8 8 8
5
1 2 3 4 5
6 7 8 9 1
2 3 4 5 6
7 8 9 1 2
3 4 5 6 7
3
2 2 8 7 4
6 5 7 7 7
8 8 9 9 9

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

def main():
    while True:
        Row = int(input())
        if Row == 0:
            break
        else:
            Ans = 0
            st = [list(map(int, input().split())) for _ in range(Row)]
            End = False

            while not End:
                #石消し処理
                for i in reversed(range(Row)):
                    for j in range(3):
                        k = j + 1
                        while k <= 4 and st[i][j] == st[i][k]:
                            k += 1
                        if k - j >= 3:
                            for wk in range(j, k):
                                Ans += st[i][wk]
                                st[i][wk] = 0
                #石落とし処理
                End = True
                for i in reversed(range(Row - 1)):
                    for j in range(5):
                        if st[i][j] != 0 and st[i+1][j] == 0:
                            wk = i + 1
                            while wk <= Row - 1 and st[wk][j] == 0:
                                wk += 1
                            st[wk-1][j] = st[i][j]
                            st[i][j] = 0
                            End = False
            print(Ans)

if __name__ == '__main__':
    main()




