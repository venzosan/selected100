#ｎ次元配列のｍ番目の要素でソート
li = [[1,4,3],[2,3,4],[3,4,5],[4,5,6],[2,3,4],[1,5,3],[2,3,4],[5,6,7]]
li = sorted(li, reverse=True, key=lambda x: x[1])  #[1]に注目してソート


