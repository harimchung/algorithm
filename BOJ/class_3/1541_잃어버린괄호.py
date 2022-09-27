note = input()
N = len(note)
num_list = []
sign = []
temp = ""
for i in range(N):
    if note[i].isdecimal():
        temp += note[i]
    else:
        num_list.append(int(temp))
        temp = ""
        sign.append(note[i])
num_list.append(int(temp))

M = len(sign) # len(num_list) = M+1
ans = num_list[0]

j = 0
while True:
    if j >= M:
        break

    if sign[j] == "-":
        for k in range(j, M):
            ans -= num_list[k+1]
        j = k

    else:
        ans += num_list[j+1]
    j += 1

print(ans)