N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x,y))

arr.sort()
for position in arr:
    print(position[0], position[1])