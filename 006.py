N=int(input())
S=input()
A=[0]*1000

for i in range(10):
  for j in range(10):
    for k in range(10):
      if S.find(str(i))!=-1:
        s1=S.find(str(i))
        if S[s1+1:].find(str(j))!=-1:
          s2=s1+S[s1+1:].find(str(j))+1
          if S[s2+1:].find(str(k))!=-1:
            A[int(str(i)+str(j)+str(k))]=1

print(sum(A))