#標準入力設定-------------------------------
import io
import sys

_INPUT = """\
123 456

"""
sys.stdin = io.StringIO(_INPUT)
#------------------------------------------
import math
 
W,H=map(int,input().split())
 
num=math.factorial(W+H-2)//(math.factorial(W-1)*math.factorial(H-1))
print(num%1000000007)