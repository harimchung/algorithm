import sys

n, k = map(int, sys.stdin.readline().split())
# 환형 큐를 이용한 방법
yose = [i for i in range(1, n+1)]
rear = 0
print("<",end="")
while len(yose)>1:
    rear = (rear + (k-1))%len(yose)
    a = yose.pop(rear)
    print(a, end=", ")
print(f"{yose.pop()}>")