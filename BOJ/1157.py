alphabet_list = []
word = input().upper()
alphabet_list.extend(word)

# 예를 들어 apple 이라는 단어를 입력하게 되면, alphabet_list 에는 ['A','P','P','L','E'] 로 들어가게 된다.
# 이제 반복문과 조건문을 쓰면서 알파벳이 나온 개수를 세면 된다.
for i in alphabet_list:
    print(alphabet_list.count(i))

