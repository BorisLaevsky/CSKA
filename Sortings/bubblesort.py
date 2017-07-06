def bubblesort(input_list):
    upper_bound = len(input_list)
    while upper_bound > 1:
        index = 0
        while index < upper_bound-1:
            if input_list[index] > input_list[index+1]:
                input_list[index],input_list[index+1] = input_list[index+1],input_list[index]
            index += 1
        upper_bound -= 1

x = [5,10,-1,2,1]
bubblesort(x)
print x
