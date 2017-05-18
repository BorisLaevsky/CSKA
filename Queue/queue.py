class Queue:

    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        first_element = self.queue[0]
        self.queue = self.queue[1:]
        return first_element

    def peak(self):
        return self.queue[0]

    def __iter__(self):
        return self

    def next(self):
        if len(self.queue) == 0:
           raise StopIteration
        first = self.queue[0]
        self.queue = self.queue[1:]
        return first

    def __str__(self):
        return str(self.queue)

q = Queue()
q.push('a')
q.push('b')
q.push('c')
q.push('d')
print q
for x in q:
    print x
print q
