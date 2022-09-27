import sys

t = int(sys.stdin.readline())
for _ in range(t):
    order = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    num_str = input().lstrip('[').rstrip(']').split(',')

    ans = num_str
    for i in order:

        if i == "R":
            num_str = num_str[::-1]

        elif i == "D":
            if n > 0:
                num_str.pop(0)
                n -= 1
            else:
                ans = "error"
                break

    if not ans == "error":
        ans = num_str

    print(ans)
