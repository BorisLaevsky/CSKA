def qsort(input_list):
    if len(input_list) == 0:
        return None
    pivot_index = len(input_list) - 1
    pivot = input_list[pivot_index]
    index = 0
    while index < pivot_index:
        if input_list[index] > pivot:
            input_list[pivot_index - 1], input_list[pivot_index] = input_list[pivot_index], input_list[pivot_index - 1]
            pivot_index, pivot = pivot_index - 1, input_list[pivot_index - 1]
            if index != pivot_index:
                input_list[index], input_list[pivot_index + 1] = input_list[pivot_index+1], input_list[index]
            index = 0
        else:
            index += 1
x = [1,2,3,4,5,0]
qsort(x)
print x
qsort(x[1:])
print x
