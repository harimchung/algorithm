answer_list=input().split()
ascending_list = ['1','2','3','4','5','6','7','8']
if answer_list == ascending_list:
    print('ascending')
elif answer_list == ascending_list[::-1]:
    print('descending')
else :
    print('mixed')
