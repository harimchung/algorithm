import sys
def memo(n):
    
    if n < 4:
        return memoization[n]
    else:
        for i in range(4, n+1):
            temp = []
            if i%3 == 0:
                temp.append(1 + memoization[i//3])
            if i%2 == 0:
                temp.append(1+ memoization[i//2])
            temp.append(1 + memoization[i-1])
            memoization[i] = min(temp)

    return memoization[n]

x = int(sys.stdin.readline())
memoization = [0]*(x+3)
memoization[1] = 0
memoization[2] = 1
memoization[3] = 1
print(memo(x))

