import sys
N, K = map(int, sys.stdin.readline().split())

arr=[[0,1,0],[0,1,1,0],[],[],[],[],[],[],[],[],[],[]]

for i in range(2, N+1):
    now = arr[i]
    now.append(0)
    for j in range(len(arr[i-1])-1):
        a = arr[i-1][j] + arr[i-1][j+1]
        now.append(a)
    now.append(0)
print(arr[N][K+1])
