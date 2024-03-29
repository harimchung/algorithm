N = int(input())

# 정사각형 판 입력받기
cookies = [list(input()) for _ in range(N)]
flag = False

for i in range(N):
    for j in range(N):
        if cookies[i][j] == '*':
            head = (i, j)
            flag = True
            break
    if flag:
        break

heart = (head[0]+1, head[1])
# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽다리
left_arm, right_arm, waist, left_leg, right_leg = 0, 0, 0, 0, 0


# 심장이 있는 열에서 왼쪽, 오른쪽 팔의 끝을 찾는다.
# 왼쪽 팔의 시작지점과, 오른쪽 팔의 끝 지점을 찾는다.
left_arm = heart[1] - cookies[heart[0]].index("*")
right_arm = cookies[heart[0]].index("_", heart[1]) - heart[1] - 1
ci, cj = heart[0], heart[1]
# 몸통 길이 구하기
for i in range(ci, N):
    if i+1 <= N and cookies[i+1][cj] == "*":
        waist += 1
    else:
        break
waist_x, waist_y = heart[0]+waist, heart[1]

# 왼쪽 발
left_leg_start = (waist_x+1, waist_y-1)
right_leg_start = (waist_x+1, waist_y+1)


for j in range(left_leg_start[0], N):
    if j+1 <= N and cookies[j+1][left_leg_start[1]] == "*":
        left_leg += 1
    else:
        break

for k in range(right_leg_start[0], N):
    if k+1 <= N and cookies[k+1][right_leg_start[1]] == "*":
        right_leg += 1
    else:
        break

print(left_arm, right_arm, waist, left_leg, right_leg)
