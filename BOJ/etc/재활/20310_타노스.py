# 2 <= S <= 500
# S는 짝수 개의 0, 1로 이루어져 있다.
# 절반의 0과 1을 제거하여 새로운 문자열 S'을 만든다.
# 문자열을 재배치하면 안된다.

S = list(input())
n = len(S)
start = 0

# 앞쪽에 있는 1을 최대한 제거하고
# 뒤쪽에 있는 0을 최대한 제거한다.

a = S.count("1") // 2
b = S.count("0") // 2

cnt_0, cnt_1 = 0, 0
current = 0

while current < len(S):
    num = S[current]

    if num == "1" and cnt_1 < a:
        S.pop(current)
        cnt_1 += 1
        current -= 1
    current += 1

# print(S)
current = len(S) - 1

while current > 0:
    num = S[current]

    if num == "1" and cnt_0 < b:
        S.pop(current)
        cnt_0 += 1
        current += 1
    current -= 1

print(S)
# for i in range(n):
#     try:
#         num = S[i]
#         if num == "1" and cnt_1 < a:
#             S.pop(i)
#             cnt_1 += 1

#     except:
#         break

# m = len(S)
# for j in range(m-1, -1, -1):
#     try:
#         num = S[j]
#         if num == "0" and cnt_0 < b:
#             S.pop(j)
#             cnt_0 += 1

#     except:
#         break

# print(''.join(S))
