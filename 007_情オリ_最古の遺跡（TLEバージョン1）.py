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
#import glob

#解法はたぶん合っているがTLE

N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]
le=len(P)
area=0
Ans=0

P_set=set()
for i in range(le):
  P_set.add((P[i][0],P[i][1]))

ch=[]

for i in range(le-1):
#for i in range(1,3):
  ch.clear()
  for j in range(i+1,le):
    if i==j:
      pass
    else:
      ch.append(\
        [(abs(P[i][0]-P[j][0])**2)+(abs(P[i][1]-P[j][1])**2)\
        ,i,j])
  ch.sort()
  #pre_st=ch[0][0]
  for k in range(len(ch)-1):

    pre_st=ch[k][0]
    pre_co=ch[k][2]
    st=ch[k+1][0]
    co=ch[k+1][2]
    if pre_st==st:#長さチェック

      x1=P[pre_co][0]-P[i][0]
      x2=P[co][0]-P[i][0]
      y1=P[pre_co][1]-P[i][1]
      y2=P[co][1]-P[i][1]
      if (x1*x2)+(y1*y2)==0:#内積チェック(直角)

        xa=P[i][0]+x1+x2
        ya=P[i][1]+y1+y2
        if (xa,ya) in P_set:#正方形になるポイントに柱があるか
          area=(x1+x2)*(x1+x2)-(x1*x2*2)
          Ans=max(area,Ans)

          #print(P[i])
          #print(P[pre_co])
          #print(P[co])
          #print(str(xa)+' '+str(ya))
          #print(area)
          #print(Ans)
print(Ans)









  







  

