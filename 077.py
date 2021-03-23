#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
100 100
16
11
37
86
19
8
48
21
13
20
93
54
12
77
82
31
69
64
37
40
32
84
27
76
61
62
87
55
44
24
87
41
68
40
43
78
37
58
65
86
75
75
54
50
22
11
75
100
93
80
41
77
27
79
88
44
95
9
73
69
64
73
97
79
24
41
48
24
17
85
98
33
25
71
5
82
13
72
56
12
13
61
87
39
43
52
40
74
30
7
77
100
46
92
96
55
80
42
96
49
5
35
1
-50
17
-2
27
-58
15
42
-16
2
-39
19
38
-4
-4
5
-69
39
-42
11
-5
55
-30
-33
90
-71
5
28
32
-45
44
-51
25
-30
47
-24
-52
11
68
-1
-69
64
-35
42
-30
22
-75
12
-14
6
43
-50
6
20
36
7
-35
-34
28
-13
-3
71
-26
33
-8
11
-32
-14
-10
29
1
8
-39
-20
63
-71
86
-62
-7
72
-62
-23
10
-2
12
18
33
-23
4
-46
55
-27
42
-31
-49
74
-66

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import itertools
#import copy
import time
#import glob
import heapq
import math
import collections

n,m=map(int,input().split())
dist=[]
journy=[]
for i in range(n-1):
  dist.append(int(input()))

for i in range(m):
  journy.append(int(input()))

s=[0]*(n+1)
s[0]=0

for i in range(n-1):
  s[i+1]=s[i]+dist[i]

#print(dist)
#print(s)
fr=0
Ans=0

for i in range(m):
  to=fr+journy[i]
  Ans+=abs(s[to]-s[fr])
  #print('from:'+str(fr)+' to:'+str(to)+' dist:'+str(s[to]-s[fr])+' Ans:'+str(Ans))
  fr=to

print(Ans%100000)

