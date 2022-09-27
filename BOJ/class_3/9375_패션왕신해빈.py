T = int(input())
for tc in range(1, T+1):
    n = int(input())
    fashion_dictionary = {}
    for _ in range(n):
        a, b = input().split()
        if b not in fashion_dictionary:
            fashion_dictionary.update({b:[a]})
        else:
            fashion_dictionary[b].append(a)

    cloth_type = list(fashion_dictionary.keys())
    m = len(cloth_type)
    k = 1

    for j in range(m):
        items = fashion_dictionary[cloth_type[j]]
        l = len(items)
        k *= (l+1)
    print(k-1)


