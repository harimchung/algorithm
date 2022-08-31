import sys

n = int(sys.stdin.readline())
num = sys.stdin.readline()
ans =0
for i in range(n):
    ans += int(num[i])
print(ans)