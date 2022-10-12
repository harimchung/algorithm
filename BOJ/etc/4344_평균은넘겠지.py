C = int(input())
for tc in range(C):
    scores = list(map(int, input().split()))
    N = scores.pop(0)
    avg = sum(scores) / N
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1
    ratio = (cnt / N) * 100

    print(f"{ratio:.3f}%")