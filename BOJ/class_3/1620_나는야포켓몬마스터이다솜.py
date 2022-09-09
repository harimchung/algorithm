import sys

n, m = map(int, sys.stdin.readline().split())
pocketmons_dict = {}
pocketmons_dict_1 = {}

for i in range(1, n+1):
    pocketmon = sys.stdin.readline().rstrip()
    pocketmons_dict[pocketmon] = i
    pocketmons_dict_1[i] = pocketmon



for _ in range(m):
    question = sys.stdin.readline().rstrip()

    # 만약 정수가 입력된다면, 정수에 맞는 딕셔너리를 주세요.
    try:
        print(pocketmons_dict_1.get(int(question)))
    except:
        print(pocketmons_dict.get(question))
