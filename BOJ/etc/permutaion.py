a = [1,2,3,4,5]
n = len(a)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(a[j], end="")
    print()