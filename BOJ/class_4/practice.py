# for i, j in a:
#     print(i,j)

def practice(i, j):
    for qi, qj in a: # queen_list 안에 있는 모든 queen들에 대해서 검사해야 한다.
        if i + j == qi + qj:
            return False
        if j - i == qj - qi:
            return False
    return True


a = [(1,2),(3,4)]
print(practice(1,2))
print(practice(0,0))
