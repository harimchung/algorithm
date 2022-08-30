sugar_kg = int(input()) # 설탕의 무게를 받습니다.
how_many_bags = 0 # 총 몇 봉지인지 구하는 변수

def sugar_kg_5(): # 5가 몇번 들어가는지 몫을 구하는 함수
    return sugar_kg // 5

def sugar_5_kg_remainder() : # 5로 나누었을 때 나머지을 반환하는 함수
    return sugar_kg % 5


# 먼저 5로 나누었을 때 나머지를 0, 3, 그리고 나머지로 분류한다.

if sugar_5_kg_remainder() == 0:
  how_many_bags = sugar_kg_5()
  # 5의 배수인 경우 몫을 출력한다.

if sugar_5_kg_remainder() == 3:
    how_many_bags = sugar_kg_5() + 1
    # 5n + 3의 경우 n+1 봉지를 출력한다.

elif sugar_5_kg_remainder() == 1 or 2 or 4: 
    # kg에서 5로 나눈 나머지가 1,2,4인 경우 
    # 값에서 가장 비슷한 5의 배수를 먼저 제외하고, 3으로 나눠본다.
    # 예를 들면 11이면 10을 먼저 빼고 나머지를 3으로 나눠보고, 아니면 5을 빼고 3으로 나눠본다.
    # 나눠진 값이 3의 배수이면 출력하고, 아니면 맞을 떄까지 5의 배수 수를 줄여가며 같은 작업을 반복한다.
    flag = False
    for i in range (sugar_kg_5(),-1,-1) :
        left_over_3 = (sugar_kg - i*5)%3
        left_over_3_quotient = (sugar_kg - i*5) // 3
        if left_over_3 == 0 :
            flag = True
            how_many_bags = i + left_over_3_quotient
            break
            
    if not flag:
        how_many_bags = -1

print(how_many_bags)
