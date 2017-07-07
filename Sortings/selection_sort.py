def selection_sort(input_list):
    bottom_bound = 0
    while bottom_bound < len(input_list):
        index = bottom_bound
        min = input_list[index]
        min_index = index
        while index < len(input_list):
            if input_list[index] < min:
                min = input_list[index]
                min_index = index
            index += 1
        input_list[bottom_bound], input_list[min_index] = input_list[min_index], input_list[bottom_bound]
        bottom_bound += 1

x = [5,8,10,2,1]

selection_sort(x)
print x
