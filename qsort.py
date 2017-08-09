import random

def partition(lst, l, r):

    if l >= r:
        return
    v = random.choice(lst[l:r + 1])
    i = l
    j = r
    while i <= j:
        while lst[i] < v:
            i += 1
        while lst[j] > v:
            j -= 1
        if i <= j:
            i += 1
            j -= 1
            lst[i], lst[j] = lst[j], lst[i]
    return j


def quicksort(lst, l, r):

    if l < r:
        q = partition(lst, l, r)
        quicksort(lst, l, q)
        quicksort(lst, q + 1, r)


lData = [2, 4, 5, 3, 0, 8, 1, 9]
print(lData)
quicksort(lData, 0, len(lData) - 1)
print(lData)
