def split(input_list):
    index = 0
    while index <= len(input_list) - 1:
        input_list[index] = [input_list[index]]
        index += 1

def merge(first_list, second_list):
    output = []
    minimal = None
    while first_list and second_list:
        if first_list[0] < second_list[0]:
            output.append(first_list.pop(0))
        else:
            output.append(second_list.pop(0))
    if not first_list:
        output += second_list
    else:
        output += first_list
    return output

def mergesort(input_list):
    print input_list
    if len(input_list) == 1 or not input_list:
        return input_list
    else:
        middle = int(len(input_list)/2)
        left = mergesort(input_list[:middle])
        right = mergesort(input_list[middle:])
        return merge(left, right)

x = [5,4,3,2,1,19]
print mergesort(x)
print x
