P = int(input())
for _ in range(P):
    tc, *heights = list(map(int, input().split()))


    answer = 0
    for i in range(1, 20):
        for j in range(i-1, -1, -1):
           
            if heights[i] < heights[j]:
                answer += 1
            
    print(tc, answer)