n = int(input())
a = []

for i in range(n):
    (x, y) = map(int, input().split())
    a.append((x,y))


answer_list = []

for j in range(len(a)):
    cnt = 0

    for i in range (len(a)): # i는 0, 1, 2, 3, 4

        if a[j][0] < a[i][0] and a[j][1] < a[i][1] :
        
            cnt+=1
            

    answer_list.append(str(cnt+1))

answer = " ".join(answer_list)
print(answer)
