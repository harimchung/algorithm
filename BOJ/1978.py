# 최종적으로 소수의 개수를 셀 count 라는 변수를 만든다.
count = 0

# 사용자에게 숫자의 개수를 입력받는다.
n = int(input())

# 소수를 판별해서 final_list에 추가하는 행위를 n번 반복한다.

numbers = map(int, input().split())
for number in numbers:
    empty_list = []
   
    for j in range (1, number+1) : # j는 1부터 숫자까지의 정수이다.
        if number % j == 0 : 
            empty_list.append(j)
    
    if len(empty_list) == 2:
        count += 1



print(count)


