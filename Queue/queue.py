class Queue:

    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        try:
            first_element = self.queue[0]
            self.queue = self.queue[1:]
            return first_element
        except IndexError:
            raise IndexError("popin empty queue, Jimbo")

    def peak(self):
        return self.queue[0]

    def __iter__(self):
        return self

    def next(self):
        if len(self.queue) == 0:
           raise StopIteration
        return self.pop()

    def __str__(self):
        return str(self.queue)

q = Queue()
q.pop()
