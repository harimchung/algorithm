n = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)
ans = 0
for i in range(n):
    ans += A[i] * B[i]

print(ans)

