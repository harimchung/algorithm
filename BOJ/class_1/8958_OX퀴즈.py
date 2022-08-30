
'''
def correct_number(testcase):
    number_correct = 0
    correct_list = []

    for i in testcase:
        if i == 'O':
            number_correct += 1
        else :
            number_correct = 0
        correct_list.append(number_correct)    
    return sum(correct_list)
'''

'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''

'''
n = int(input())

for i in range(n):
    number_correct = 0
    correct_list = []
    word = input()

    for j in word:
        if j == "O":
            number_correct += 1
        else:
            number_correct = 0
        correct_list.append(number_correct)

    print(sum(correct_list))
'''

def sol(n):
    if n // 2 == 0:
        return str(n % 2)
    return sol(n // 2) + sol (n % 2) 
print(sol(11))
