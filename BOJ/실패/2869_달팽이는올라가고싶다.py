import math
a , b, v = map(int, input().split())
print(math.ceil((v-a)/(a-b)) + 1)
# print((v-a)/(a-b))