# 손익분기점을 파악하기 위해서는 1 부터 n 번째 까지 계속 돌리다가
# 최초로 손익분기점을 넣은 경우에 출력해야 하기 때문에
# while 문을 쓰는 것이 적합할 것 같다.


# 처음에는 이 방식으로 생각하였으나, 21억이 넘어가는 경우에는 시간이 너무 많이 걸린다.
# 나머지를 구하는 방식으로 바꾸는 것이 적합할 것 같다!

# 처음에 input으로 a, b, c가 주어진다
# a, b, 는 각각 고정비용, 하나당 드는 금액 이고 c는 판매금액이다.


a, b, c = map(int, input().split())

if b >= c:
    print(-1)

else :
    print(int(a/(c-b)) + 1)





    
