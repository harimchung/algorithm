
test_num = int(input())
case = [input().split() for x in range(test_num)]

for j in range (test_num):
    for k in range (len(case[j][1])):
        print(case[j][1][k]*int(case[j][0]), end="")
    print()

    # print(f"{case[j][1][k]}")


 
    # for j in range(test_num):
    #     result = str(case[j][0]*int(case[j][1]))
    #     empty.append(result)    
    #     result_string = ('').join(j for j in empty)
 
    # print(result_string)
 
    