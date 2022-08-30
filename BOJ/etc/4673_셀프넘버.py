def fn(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return n + sum


# def is_self_number(num):
#     for j in range(1, num+1):
#         if fn(j) == num:
#             return False # 셀프넘버가 아니다
#     return True # 셀프넘버 이다

# for k in range (1, 10001):
#     if is_self_number(k) == True:
#         print(k)

# # 시간초과뜸...ㅠ

set_1 = set(range(1, 10001))
gen_set = set()

for j in range (1, 10001):
    gen_set.add(fn(j))

self_set = set()
self_set = set_1 - gen_set

self_list = list(self_set)
self_list.sort()

for k in self_list:
    print(k)
