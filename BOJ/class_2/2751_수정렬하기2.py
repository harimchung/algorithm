N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    sorted_list = []
    i, j = 0 , 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        elif i < len(left):
            sorted_list.append(left[i])
            i += 1

        elif j < len(right):
            sorted_list.append(right[j])
            j += 1
    return sorted_list

for i in merge_sort(arr):
    print(i)
