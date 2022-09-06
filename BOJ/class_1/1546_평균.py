import sys
n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
new_scores = 0
max_score = max(scores)
for score in scores:
    new_scores += score/max_score * 100

print(new_scores/n)