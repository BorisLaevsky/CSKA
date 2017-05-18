class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        try:
            deleted_element = self.stack[-1]
            self.stack = self.stack[:-1]
            return deleted_element
        except IndexError:
            print "ay lmao popin empty stack"


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

print s.pop()

