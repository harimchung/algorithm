import sys
def dp(n):
    if n < 4:
        return ans[n]
    for i in range(4, n+1):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]
    return ans[n]
T = int(sys.stdin.readline())
ans = [0]*12
ans[1] = 1
ans[2] = 2
ans[3] = 4
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp(n))
# 1을 만드는 방법 -> 1 => 1가지
# 2를 만드는 방법 -> 1+1 2 => 2가지
# 3을 만드는 방법 -> 1+1+1 1+2, 2+1, 3 => 4가지
# 4를 만드는 방법 -> 1+1+1+1, 1+1+2, 1+3, 1+2+1, 2+1+1, 2+2, 3+1 => 7가지
# (1+3, 2+2, 3+1)
# 5를 만드는 방법 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 2+3 => 1,4,3,3,2 => 13가지
#(1+4, 2+3, 3+2)

