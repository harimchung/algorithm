# word = 'ssafy'
# print(word)
# print(id(word))

# word = 'test'
# print(word)
# print(id(word))

#4 s.isupper(), s.islower()

#  title은 첫번째만 대문자. 나머지는 소문자인 경우.
# print('I am harim'.istitle()) # False
# print('I Am Harim'.istitle()) # True

# print('a' in 'apple')
# print('apple' in 'apple curry')
# print('apple' in ['apple', 'banana', 'cherry'])
# print('apple' in ('apple', 'banana', 'cherry'))

# print('apple' + 'curry')
# print(['apple', 'banana']+['cherry'])
# print(('apple', 'banana')+('cherry'))

# a = {'사과', '바나나', '수박'}
# a.add('금귤')
# print(a)

# a.update(['딸기', '바나나', '무화과'])
# print(a)

# a.discard('애플망고')
# print(a)
# # a.remove('애플망고')
# # print(a)

# a.pop()
# print(a)

# a = {'apple':'사과', 'banana':'바나나', 'watermelon':'수박'}
# print(a.get('pineapple')) # None (default)
# print(a.get('pineapple', 0)) # 0

# print(a['apple']) # 사과
# #

# data = a.pop('apple') # key값을 pop에 넣는다.
# print(data, a)

# data = a.pop('pineapple', 0) # 이렇게 없는 경우 대신 반환할 값을 넣어줘도 된다.
# print(data, a)

# a.update(무화과='fig')
# print(a)



# original_list = ['안녕', '정뭄뭄']
# print(id(original_list))
# new_list = original_list
# print(id(new_list))

# duplicate_list = original_list[:]
# print(id(duplicate_list))

import copy

# a = [1, 2, [4, 5]]
# b = copy.deepcopy(a)
# b[2][0] = 0

# print(a, b) #

d = {'a':3}
d['b'] = d.get('a')
print(d) #{'b':3}
