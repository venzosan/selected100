while True:
  n,x=map(int,input().split())
  Ans=0
  if n==0 and x==0:
    break
  else:
    for i in range(1,n-1):
      for j in range(i+1,n):
        for k in range(j+1,n+1):
          if i+j+k==x:
            Ans+=1
    print(Ans)