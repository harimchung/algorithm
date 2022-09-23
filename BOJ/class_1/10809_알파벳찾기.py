S = input()
ans = [-1] * 26

for i in range(len(S)):
    idx = ord(S[i]) - ord("a")
    if ans[idx] == -1:
        ans[idx] = i
print(*ans)