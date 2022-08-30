# 입력에 ababc가 들어오면
# a,b,a,b,c,ab,ba,ab,bc 이런식으로 출력하게 어떻게 만들 수 있을까?

# 1개짜리 0, 1, 2, 3, 4 [0 :1 ]
# 2개짜리 01, 12, 23, 34 [ 0 : 2]
# 3개짜리 012, 123, 234 [ 0 : 3]
# 4개짜리 0123, 1234 [0 : 4]
# 5개짜리 01234 [0 : 5]

# 처음에 입력받은 문자열을 n에 할당한다.
n = input()
set_a = set()

for i in range (len(n)):
    for j in range (len(n)+1):
        set_a.add(n[i:i+j])

set_a.remove("")
print(len(set_a))