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

# d = {'a':3}
# d['b'] = d.get('a')
# print(d) #{'b':3}

class Person:
    blood_color = 'red' # 클래스 변수 : 공통으로 쓰일변수
    count = 0


    def __init__(self, name) -> None: # __init__ 은 생성자 메서드, 인스턴스가 생성할 때 자동으로 호출된다. 이거죠 인스턴스 변수의 정의
        self.name = name
        Person.count += 1
        

    @classmethod
    def number_of_population(cls):
        print(f"인구수는 {cls.count}입니다")

    @staticmethod
    def check_rich(money): # stati은 cls, self 사용 x
        return money > 10000

person1 = Person('지민')
person2 = Person('하림')
print(Person.check_rich(1000000))
print(person1.check_rich(100000000))
# print(Person.count) # 접근 및 할당
# Person.number_of_population

# print(isinstance(person1, Person)) # True
# print(type(person1)) # class __main__.Person

class Circle():
    pi = 3.14 # 클래스 변수

    def __init__(self, r):
        self.r = r # 인스턴스 변수

    def area(self):
        return 3.14 * self.r* self.r

    def __str__(self) -> str:
        return f"[원] area : {self.r}"

    def __gt__(self, other):
        return self.r > other.r

c1 = Circle(10)
c2 = Circle(1)

# print(c1)
# print(c2)
# print(c1>c2)
# print(c1<c2)

# print(Circle.pi)
# print(c1.pi)

# Circle.pi = 5
# print(c1.pi)
# print(c2.pi)




# def add_print(original):
#     def wrapper():
#         print("함수시작")
#         original()
#         print("함수 끝")
#     return wrapper

# @add_print
# def print_hello():
#     print("hello~")

# print_hello()

# hello