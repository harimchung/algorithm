import sys
T = int(sys.stdin.readline().rstrip())
def hotel(h,w,n):
    height = n % h
    room = n // h + 1
    if height == 0:
        height = h
        room = room - 1
    height = str(height)


    if room <= 9:
        room = "0" + str(room)
    room = str(room)
    return height + room

for tc in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    print(hotel(H, W, N))
