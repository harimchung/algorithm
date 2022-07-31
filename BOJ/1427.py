# 수가 주어지면 수를 내림차순으로 정렬하는 문제

# 입력받은 수를 정수라고 하고, n이라는 변수에 할당한다.
n = input()
n_list = []
n_list.extend(n)
sorted_n_list = sorted(n_list, reverse=True)

print(''.join(sorted_n_list))