
#場合分けは複雑になりそうなのでやめた
#（A+Bと2C・Aと2C・Bと2C・片方だけ高い時に
# 単品で作るかハーフで作るかなど）

A,B,C,X,Y=map(int,input().split())
Ans=0

if (A+B)>C*2:
  Ans+=min(X,Y)*C*2
  if X>Y:
    if A>C*2:
      Ans+=(X-Y)*C*2
    else:
      Ans+=(X-Y)*A
  else:
    if B>C*2:
      Ans+=(Y-X)*C*2
    else:
      Ans+=(Y-X)*B
else:
  if A>C*2:
    Ans+=X*C*2
  else:
    Ans+=X*A
  if B>C*2:
    Ans+=Y*C*2
  else:
    Ans+=Y*B