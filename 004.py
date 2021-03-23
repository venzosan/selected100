N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
#print(A)

Ans=0

for i in range(M-1):
  for j in range(i+1,M):
    cnt=0
    for k in range(N):
      cnt+=max(A[k][i],A[k][j])
    if Ans<cnt:
      Ans=cnt

print(Ans)