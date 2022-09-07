import sys

numbers = list(map(int, sys.stdin.readline().split()))
valid_num = 0
for number in numbers:
    valid_num += number**2
print(valid_num % 10)