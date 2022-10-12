n = int(input())
word_list = []
for _ in range(n):
    word = input()
    word_list.append((len(word), word))
word_list = set(word_list)
word_list = list(word_list)
word_list.sort()

for word in word_list:
    print(word[1])