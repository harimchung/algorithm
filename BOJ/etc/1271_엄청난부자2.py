import sys

n, m = map(int, sys.stdin.readline().split())
# n은 돈, m은 생명체

a = n // m
print(a)
b = n - (m*a)
print(b)