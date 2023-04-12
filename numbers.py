# a = 9
# wantedLength = 5
# ans = [0]*wantedLength

# for i in range(wantedLength):
#     quo = a // (2**(wantedLength-1-i))
#     rem = a % (2**(wantedLength-1-i))

#     if quo == 1:
#         a =  rem
#         ans[i] = 1

# print(ans)

# a = 20


# def binary(n):
#     if n <= 1:
#         return str(n)
#     else:
#         return binary(n//2) + str(n % 2)


# print(binary(a))

a = 9
wantedLength = 5


def binary(n):
    output = ""
    for j in range(wantedLength-1, -1, -1):
        output += "1" if n & (1 << j) else "0"
    return output


print(binary(a))
