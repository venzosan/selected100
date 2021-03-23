#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
11
15004200 341668840
277786703 825590503
85505967 410375631
797368845 930277710
90107929 763195990
104844373 888031128
338351523 715240891
458782074 493862093
189601059 534714600
299073643 971113974
98291394 443377420

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob

N=int(input())
AB=[list(map(int,input().split())) for _ in range(N)]
in_out_set=set()
Ans=5*10**10

for i in range(len(AB)):
  in_out_set.add(AB[i][0])
  in_out_set.add(AB[i][1])

in_out=list(in_out_set)
in_out.sort()

in_out_pairs=[(ent,exi) for ent,exi in itertools.combinations(in_out,2)]
#print(in_out_pairs)

for ent,exi in in_out_pairs:
  cnt=0
  for i in range(len(AB)):
    if AB[i][0]<ent and AB[i][1]<=exi:
      cnt+=2*(ent-AB[i][0])+(exi-ent)
    elif AB[i][0]>=ent and AB[i][1]<=exi:
      cnt+=exi-ent
    elif AB[i][0]>=ent and AB[i][1]>exi:
      cnt+=2*(AB[i][1]-exi)+(exi-ent)
    elif AB[i][0]<ent and AB[i][1]>exi:
      cnt+=2*(ent-AB[i][0])+2*(AB[i][1]-exi)+(exi-ent)
  Ans=min(Ans,cnt)
  #print(cnt)
  #print(Ans)

print(Ans)

#A<=B、かつ、入口(s)<=出口(t)の前提があれば、
#場合分けをしなくても|s-A|+|A-B|+|t-B|で計算できる




