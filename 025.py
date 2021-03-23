#標準入力設定-------------------------------
import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
import math
#import copy
#import time
#import glob
import collections

while True:
  w,h=map(int,input().split())
  if w==0 and h==0:
    break
  else:
    mp=[list(map(int,input().split())) for _ in range(h)]
    seen=[[-1]*w for _ in range(h)]
    todo=collections.deque()
    
    ir=0
    Ans=0
    CH=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    for i in range(h):
      for j in range(w):
        if seen[i][j]!=-1:
          continue
        else:
          #todo.append([i,j])
          if mp[i][j]==0:
            seen[i][j]=0
          else:
            todo.append([i,j])
            ir+=1
            seen[i][j]=ir
            while len(todo)>0:
              hh,ww=map(int,todo.pop())
              for ch in CH:
                if hh+ch[0]>=0 and hh+ch[0]<h \
                  and ww+ch[1]>=0 and ww+ch[1]<w:
                  if seen[hh+ch[0]][ww+ch[1]]==-1:
                    if mp[hh+ch[0]][ww+ch[1]]==0:
                      seen[hh+ch[0]][ww+ch[1]]=0
                    else:
                      seen[hh+ch[0]][ww+ch[1]]=ir
                      if ch!=[0,0]:
                        todo.append([hh+ch[0],ww+ch[1]])
          Ans=ir
  print(Ans)              
    
            


          
          




    




