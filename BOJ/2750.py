# 입력받을 test case를 n개라고 한다.
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

for i in range(n-1,0,-1):
    for j in range (0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    
for k in a:
    print(k)