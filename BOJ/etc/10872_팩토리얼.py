def fact(num):
    if num == 0 or num == 1:
        return 1
    return fact(num-1)*num

print(fact(int(input())))