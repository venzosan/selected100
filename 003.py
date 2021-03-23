S=input()
cnt=0
Ans=0

for s in S:
  if s=='A' or s=='C' or s=='G' or s=='T':
    cnt+=1
  else:
    if Ans<cnt:
      Ans=cnt
    cnt=0

if Ans<cnt:
  Ans=cnt

print(Ans)