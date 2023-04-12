# 자주 나오는 단어일 수록 앞에 배치한다.
# 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전순으로 앞에있는 단어일수록 앞에 배치한다.

# N M
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
word_dict = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    else:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1


sorted_dict = sorted(word_dict.items(), key=lambda item: (
    -item[1], -len(item[0]), item[0]))

for i in range(len(sorted_dict)):
    print(sorted_dict[i][0])
