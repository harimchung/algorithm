# a, b = map(int, input().split())

# if b >= 45:
#     print(a, b-45)

# else:
#     if a == 0:
#         print(23, b+15)
#     else:
#         print(a-1, b + 15)

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         print(numbers[j][i], end=' ')

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         print('걷는다!')

#     def eat(self):
#         print(f'{self.name}!먹는다!')

# dog = Animal('dog')
# dog.walk()

lunch = ['짜장면', '짬뽕', '탕수육']

for idx, num in enumerate(lunch):
    print(idx, num)