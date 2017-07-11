def particion(input_list, left = 0, right = None):
    if right == None:
        right = len(input_list) - 1
    pivot = input_list[right]
    i = left
    j = right
    while i <= j:
        while input_list[i] < pivot:
            i += 1
        if i < j:
            input_list.append(input_list.pop(i))
        j -= 1
    if j+1 == right:
        return j
    else:
        return j+1

def qsort(input_list, left = 0, right = None):
    if right == None:
        right = len(input_list) - 1
    pivot = particion(input_list, left, right)
    if left < right:
        qsort(input_list, left, pivot)
        qsort(input_list, pivot+1, len(input_list) - 1)



x = [1,2,3,7,0,1,2,5,7]
print x
qsort(x)
print x

