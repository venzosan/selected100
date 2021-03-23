#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
N=int(input())
P=set([tuple(map(int,input().split())) for _ in range(N)])

Ans=0

for (x1,y1),(x2,y2) in itertools.combinations(P,2):
    t1x=x2-(y2-y1)
    t1y=y2+(x2-x1)
    t2x=x1-(y2-y1)
    t2y=y1+(x2-x1)
    if (t1x,t1y) in P and (t2x,t2y) in P:
      area=(x1-x2)**2+(y1-y2)**2
      Ans=max(area,Ans)

print(Ans)









  







  

