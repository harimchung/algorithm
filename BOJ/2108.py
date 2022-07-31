import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
   num_list.append(int(sys.stdin.readline()))

num_list.sort()


# 산술평균
sum_num_list = int(sum(num_list))
if sum_num_list < 0:
    average = int(sum_num_list / n - 0.5)

else:
    average = int(sum_num_list/n + 0.5)

print(average)

# 중앙값 구하기
print(num_list[int(n/2)])

# 최빈값 구하기
cnt = 0



# 범위 구하기
print(num_list[-1]-num_list[0])

