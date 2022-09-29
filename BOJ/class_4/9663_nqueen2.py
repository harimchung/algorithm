def queen(row, n): # row는 행, n은 주어진 N
    global cnt
    if row == n: # N까지 행을 다 찾았으면 카운트를 1 증가시킨다.
        cnt += 1

    for i in range(N):
        if visited[i] == 0:         # 해당 열에 방문하지 않았고
            if possible(row, i):    # 주어진 행에 대해서 열에 둘 수 있을 때
                visited[i] = 1      # 방문처리
                queen_list.append((row,i)) # queen리스트에 추가하기
                queen(row+1, n)      # 다음 행으로 가서 queen 찾기
                queen_list.remove((row, i)) # 이하는 원복 과정
                visited[i] = 0


def possible(i,j):
    # 이미 열은 visited를 통해서 걸러내고 있으므로, 대각선에 대해서만 검사하면 된다.
    if not queen_list: # 아무원소도 없을 경우에는 True를 반환한다.
        return True

    for qi, qj in queen_list: # queen_list 안에 있는 모든 queen들에 대해서 검사해야 한다.
        if i + j == qi + qj:
            return False
        if j - i == qj - qi:
            return False

    return True # 여기까지 왔다면, True를 반환한다.

N = int(input())
queen_list = []
visited = [0]*N
cnt = 0
queen(0, N)
print(cnt)