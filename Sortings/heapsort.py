def sift_down(input_list, start = 0, end = None):
    if end == None:
        end = len(input_list) - 1
    root = start
    while root*2 + 1  <= end:
        child = root*2 + 1
        if child + 1 <= end and input_list[child] < input_list[child + 1]:
            child += 1
        if input_list[root] <= input_list[child]:
            input_list[root], input_list[child] = input_list[child], input_list[root]
        root = child

def heapify(input_list, end):
    start = (len(input_list) - 2) / 2
    while start >= 0:
        sift_down(input_list, start, len(input_list) - 1)
        start -= 1

def heapsort(input_list):
    tail = len(input_list) - 1
    heapify(input_list, tail)
    while tail > 0:
        print tail
        input_list[0], input_list[tail] = input_list[tail], input_list[0]
        tail -= 1
        sift_down(input_list, 0, tail)

x = [4,5,3,8,1,0,10,10,10,1,7]
heapsort(x)
print x
