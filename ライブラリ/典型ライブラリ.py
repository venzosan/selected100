#---------------------------------
#ライブラリ一覧
#010:bit探索
#020:再帰関数
#030:深さ優先探索
#040:深さ優先探索(再帰)
#050:幅優先探索
#060:二分探索
#061:二分探索(一般拡張：探索対象以上で最小の値(配列インデックス)を返す)
#062:めぐる式二分探索
#070:ダイクストラ（通常）
#071:ダイクストラ（ヒープ）
#080:約数列挙
#090:素因数分解
#100:最大公約数・最小公倍数
#110:UnionFind
#111:UnionFind(サイズ管理あり)

#---------------------------------

#---------------------------------
#010:bit探索
N=0 #パターン数
M=0 #チェックする桁

for bit in range(2**N):
  for i in range(N):

#bit の表す部分集合に i 番目の要素が含まれる場合
    if bit & (1 << i):
      pass

#含まれない場合
    else:
      pass


#---------------------------------

#---------------------------------
#020:再帰関数
def rec(x):
#収束時の処理
  if x==0:
    return 0

#再帰呼び出し(収束に向けてxを変化させる必要がある)
  return rec(x-1)+1

#---------------------------------

#---------------------------------
#030:深さ優先探索
import collections

G=[[] for _ in range(N+1)]
seen=[-1]*(N+1)
todo=collections.deque()

for i in range(1,N):
  a,b=map(int,input().split())
  G[a].append(b)
#  G[b].append(a)

todo.append(1)
seen[1]=0

while len(todo)!=0:
  v=todo.pop()
  for r in G[v]:
    if seen[r]!=-1:
      continue
    else:
      todo.append(r)
      seen[r]=0

#---------------------------------

#---------------------------------
#040:深さ優先探索(再帰)
import collections

G=[[] for _ in range(N+1)]
seen=[-1]*(N+1)

for i in range(1,N):
  #隣接する2頂点が与えられる形式
  a,b=map(int,input().split())
  G[a].append(b)
#  G[b].append(a)

def dfs(G,v):
  seen[v]=0
  if len(G[v])==0:
    return
  else:
    for r in G[v]:
      if seen[r]!=-1:
        continue
      else:
        dfs(G,r)
      
for i in range(1,N+1):
  if seen[i]!=-1:
    continue
  else:
    dfs(G,i)

#---------------------------------

#---------------------------------
#050:幅優先探索
import collections

N=int(input())
G=[[] for _ in range(N+1)]
seen=[-1]*(N+1)
todo=collections.deque()

for i in range(1,N+1):
  #入力が「頂点、出次数、隣接頂点1、隣接頂点2、 … 、隣接頂点(出次数)」
  wk=list(map(int,input().split()))
  for r in range(2,wk[1]+2):
    G[i].append(wk[r])

todo.append(1)
seen[1]=0

while len(todo)!=0:
  #幅優先なのでpopleft()（キュー方式）
  v=todo.popleft()
  for i in range(len(G[v])):
    if seen[G[v][i]]!=-1:
      continue
    else:
      todo.append(G[v][i])
      seen[G[v][i]]=seen[v]+1

#---------------------------------

#---------------------------------
#060:二分探索
Ar=[0,2,3,4,5,6,7,8,9] #サンプル配列

def binary_search(Ar,key):
  left=0
  right=len(Ar)-1

  while right>=left:
    mid=left+(right-left)//2
    if Ar[mid]==key:
      return mid
    elif Ar[mid]>key:
      right=mid-1
    elif Ar[mid]<key:
      left=mid+1
  return -1

#---------------------------------

#---------------------------------
#061:二分探索(一般拡張：探索対象以上で最小の値(配列インデックス)を返す)
Ar=[0,2,3,4,5,6,7,8,9] #サンプル配列

def binary_search_ex(Ar,key):
  left=0
  right=len(Ar)-1

  #right・leftの更新時に1を引かないことに注意
  while right-left>1:
    mid=left+(right-left)//2
    if Ar[mid]==key:
      return mid
    elif Ar[mid]>key:
      right=mid
    elif Ar[mid]<key:
      left=mid
  return right

#---------------------------------

#---------------------------------
#062:めぐる式二分探索

#配列が必要な場合はここで設定
#Ar=[]

#def isOK(Ar,key):
def isOK(key):
  #ifの前・if文に計算式・条件式を設定
  if key:
    return True
  else:
    return False

def binary_search_meguru(ng,ok):
  while abs(ng-ok)>1:
    mid=(ng+ok)//2

    if isOK(mid):
      ok=mid
    else:
      ng=mid

  return ok

#---------------------------------

#---------------------------------
#070:ダイクストラ（通常）
#V：頂点数、r：始点、Gは頂点番号順に
#[隣接頂点、重み]のリストを要素に持つリスト

V=5
r=0

INF=10**10
used=[False]*V
dist=[INF]*V
dist[r]=0

for i in range(V):
  min_dist=INF
  min_v=-1
  for j in range(V):
    if used[j] or dist[j]>=min_dist:
      continue
    else:
      min_dist=dist[j]
      min_v=j

  if min_v==-1:
    break
  else:
    for to in range(len(G[min_v])):
      next_v=G[min_v][to][0]
      w=G[min_v][to][1]
      dist[next_v]=min(dist[next_v],dist[min_v]+w)

    used[min_v]=True

#---------------------------------

#---------------------------------
#071:ダイクストラ（ヒープ）
#V：頂点数、r：始点、Gは頂点番号順に
#[隣接頂点、重み]のリストを要素に持つリスト
import heapq

V=5
r=0
INF=10**10

dist=[INF]*V
dist[r]=0

hq=[]
heapq.heappush(hq,[dist[r],r])

while hq!=[]:
  d=hq[0][0]
  v=hq[0][1]
  heapq.heappop(hq)

  if d>dist[v]:continue

  for to in range(len(G[v])):
    next_v=G[v][to][0]
    w=G[v][to][1]
    if dist[next_v] > d+w:
      dist[next_v] = d+w
      heapq.heappush(hq,[dist[next_v],next_v])

#---------------------------------

#---------------------------------
#080:約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#---------------------------------

#---------------------------------
#090:素因数分解
def make_PrimeFactorization(n):
  import math
  ch_n=int(math.sqrt(n))
  wk=n
  PF=[]
  for d in range(2,ch_n+1):
    while wk%d==0:
      PF.append(d)
      wk=wk//d

  if wk!=1:
    PF.append(wk)

  return PF

#---------------------------------

#---------------------------------
#100:最大公約数・最小公倍数　※mathモジュールにmath.gcd()あり
def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y,x%y)

def lcm(x, y):
  return x // gcd(x,y) * y

#---------------------------------

#---------------------------------
#110:UnionFind
#高さ(rank）あり、根の探索時に辺の貼替処理あり
#参照：「あっとのTECH LOG」
#https://at274.hatenablog.com/entry/2018/02/02/173000#%E5%AE%8C%E6%88%90%E5%BD%A2

class UnionFind_E():
  def __init__(self, n):
    self.par = [i for i in range(n+1)]
    self.rank = [0] * (n+1)
    
  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if self.rank[x] < self.rank[y]:
      self.par[x] = y
    else:
      self.par[y] = x
      
    if self.rank[x] == self.rank[y]:
      self.rank[x] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

#---------------------------------

#---------------------------------
#111:UnionFind(サイズ管理あり)
#110のUnionFindにサイズ管理(同じグループに属する頂点数)を追加
#参照：「じゃあ、したためておきます」
#https://esakat.github.io/esakat-blog/posts/about-union-find/

#2021/03/04、不具合修正：
#unite実行時、すでに同じグループであれば処理をせずにreturn
#※self.parが負の値(根)の時、上書きされる可能性がある

class UnionFind_ES():
  def __init__(self, n):
    self.par = [-1 for i in range(n+1)]
    self.rank = [0] * (n+1)
    
  def find(self, x):
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    else:
      if self.rank[x] < self.rank[y]:
        self.par[y] = self.par[y] + self.par[x]
        self.par[x] = y
      else:
        self.par[x] = self.par[x] + self.par[y]
        self.par[y] = x
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def size(self, x):
    return -self.par[self.find(x)]

#---------------------------------


