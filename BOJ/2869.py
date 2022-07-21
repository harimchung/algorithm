a, b, c = map(int, input().split()) 
final_height = c-a
days = final_height//(a-b)
if final_height%(a-b) != 0:
    days += 1
print(days+1)