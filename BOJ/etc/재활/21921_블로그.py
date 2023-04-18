# N, X : 블로그를 시작한 일수, 특정 기간
import sys

N, X = map(int, sys.stdin.readline().rstrip().split())

def max_visitors(list, day):
    global ans, cnt

    for i in range(N-day+1):
        visitor_count = sum(visitors[i:i+day])
        # 만약 방문자 수가 현재 방문자수보다 크다면 숫자를 하나
        if visitor_count > ans :
            ans = visitor_count
            cnt = 1
        elif ans == visitor_count:
            cnt += 1

      
# N일간의 방문자 수가 들어온다.
visitors = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0
cnt = 0
if sum(visitors) == 0 :
    print("SAD")
else:
    max_visitors(visitors, X)
    print(ans)
    print(cnt)