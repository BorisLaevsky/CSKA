class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        deleted_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return deleted_element

    def peak(self):
        return self.stack[-1]

    def __iter__(self):
        return self

    def next(self):
        if len(self.stack) == 0:
            raise StopIteration
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)

s = Stack()
s.push(5)
s.push(2)
s.push(3)
s.push(1)
s.push(2)
print s.pop()
print s
