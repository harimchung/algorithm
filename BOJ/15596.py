list = []
a, b, c = map(int, input().split())
list.append(a)
list.append(b)
list.append(c)

list.sort()
print(list[2]*100)
