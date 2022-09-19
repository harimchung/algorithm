import sys

n, m = map(int, sys.stdin.readline().split())
d = set(sys.stdin.readline().rstrip() for _ in range(n))
b = set(sys.stdin.readline().rstrip() for _ in range(m))

db = d&b
l = len(db)
db_list = sorted([db_name for db_name in db])
print(l)
for name in db_list:
    print(name)

