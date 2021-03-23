#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
2 20
5 9
4 10
"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------

N, W = map(int, input().split())
dp = [0] * (W+1)
for i in range(N):
    v, w = map(int, input().split())
    for j in range(w, W+1):
        dp[j] = max(dp[j-w] + v, dp[j])
print(dp[W])