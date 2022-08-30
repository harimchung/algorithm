remainder_set = set()
for _ in range(10):
    n = int(input())
    remainder = n % 42
    remainder_set.add(remainder)

print(len(remainder_set))