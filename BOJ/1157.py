from itertools import count


alphabet_list = []
word = input().upper()
alphabet_list.extend(word)
alphabet_list.sort()

# 예를 들어 apple 이라는 단어를 입력하게 되면, alphabet_list 에는 ['A','P','P','L','E'] 로 들어가게 된다.
# 이제 반복문과 조건문을 쓰면서 알파벳이 나온 개수를 세면 된다.
answer_list = []
empty_list = []

for i in alphabet_list:

    # 만약에 empty_list에 자기와 같은 알파벳이 있다면, 무시한다.
    if i in empty_list : 
        continue

    # empty_list에 없다면, 알파벳을 추가하고, list에 append 한다.
    else:
        empty_list.append(i) 
        answer_list.append({'letter':i, 'count':alphabet_list.count(i)})

# 여기까지 하면 단어가 mississipi라고 할 때,
# answer list는 다음과 같이 출력된다.
# [{'I': 4}, {'M': 1}, {'P': 1}, {'S': 4}]

# 이제 lamba 함수를 쓸 차례가 되었다. 하하

sorted_answer_list = sorted(answer_list, key=lambda dict:-dict.get('count'))

try:
    if sorted_answer_list[0]['count'] == sorted_answer_list[1]['count']:
        print('?')

    else:
        print(sorted_answer_list[0]['letter'])

except:
    print(sorted_answer_list[0]['letter'])

