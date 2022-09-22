import sys

n = int(sys.stdin.readline())
factorial = 1
for i in range(1, n+1):
    factorial *= i

factorial = str(factorial)
l = len(factorial)
cnt_0 = 0
for k in range(l-1, -1, -1):
    if factorial[k] == "0":
        cnt_0 += 1
    else:
        break
print(cnt_0)
