def merge(left, right):
    result = []
    l = 0
    r = 0
    while l < len(left) or r < len(right):
        if l >= len(left):
            result.append(right[r])
            r += 1
        elif r >= len(right):
            result.append(left[l])
            l += 1
        elif left[l] <= right [r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    return result

def merge_sort(a):
    if len(a) <=1:
        return a    
    left = []
    right = []
    for i in range(len(a)):
        middle = len(a) // 2
        if i < middle:
            left.append(a[i])
        else:
            right.append(a[i])
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



print(merge_sort([2, 4, 3, 7, 8, 1, 5, 6]))

print(merge_sort([1, 10, 50, 1000, 2, 17, 49, 1000000, 50, 43, 1, 7]))