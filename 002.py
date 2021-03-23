N=int(input())
Ans=0

for i in range(3,N+1,2):
  cnt=1
  med=int(N//2)+1
  for k in range(1,med+1):
    if i%k==0:
      cnt+=1
  if cnt==8:
    Ans+=1

print(Ans)