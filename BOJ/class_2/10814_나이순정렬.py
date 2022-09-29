N = int(input())
members = []
for j in range(N):
    age, name = input().split()
    age = int(age)
    members.append([age, name, j])
members.sort(key=lambda x:(x[0], x[2]))

for member in members:
    age, name = str(member[0]), member[1]
    print(age + " " + name)
