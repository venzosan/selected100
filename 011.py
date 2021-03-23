#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
5 2
3 1 2 5
2 2 3
1 0

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
#import time
#import glob

N,M=map(int,input().split())
K=[]
for _ in range(M):
  K.append(list(map(int,input().split())))
p=list(map(int,input().split()))
ch=0
cnt=0
Ans=0

for swi in range(2**N):
#  z=str(bin(swi))[2:]
#  print('スイッチパターン'+z.zfill(N))
  for i in range(M):
    cnt=0
    for k in range(K[i][0]):
      ch=K[i][k+1]-1
#      print(ch)
      if swi & (1 << ch):
#        print('+1')
        cnt+=1
    if cnt%2!=p[i]:
#      print(str(i)+':×')
      break
  else:
#    print(str(i)+':○')
    Ans+=1

print(Ans)






