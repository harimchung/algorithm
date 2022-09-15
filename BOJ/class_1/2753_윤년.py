import sys

def lune_year(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return 1
    return 0

n = int(sys.stdin.readline())
print(lune_year(n))