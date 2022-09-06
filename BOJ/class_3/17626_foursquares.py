import sys

n = int(sys.stdin.readline())
m = int(n ** 0.5)
flag = True
ans = []
for i in range(m, -1, -1):
    if not flag:
        break
    for j in range(int((n-i**2) ** 0.5), -1, -1):
        if not flag:
            break
        for k in range(int((n-i**2-j**2) ** 0.5), -1, -1):
            if not flag:
                break
            for l in range(int((n-i**2-j**2-k**2) ** 0.5), -1, -1):
                if (i**2)+(j**2)+(k**2)+(l**2) == n:
                    ans.append(i)
                    ans.append(j)
                    ans.append(k)
                    ans.append(l)
                    flag = False
                    break


print(4-ans.count(0))



