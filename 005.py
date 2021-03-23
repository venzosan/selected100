A,B,C,X,Y=map(int,input().split())
Ans=(A*X)+(B*Y)
Memo=(A*X)+(B*Y)

for i in range(1,max(X,Y)+1):
  Ans=min(Ans,Memo-(min(i,X)*A)-(min(i,Y)*B)+i*(2*C))

print(Ans)


#あんまり筋のよくない解き方だった
#前に解いたやり方の方がスマートだった

#A,B,C,X,Y=map(int,input().split())
#dpr=min(A+B,2*C)
#Apr=min(A,2*C)
#Bpr=min(B,2*C)
#
#dam=dpr*min(X,Y)
#if X>=Y:
#  sam=Apr*(X-Y)
#else:
#  sam=Bpr*(Y-X)
#  
#print(dam+sam)
