class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        deleted_element = self.stack[-1]
        self.stack.remove(self.stack[-1])
        return deleted_element

    def peak(self):
        return self.stack[-1]

    def Print(self):
        print self.stack

    def __iter__(self):
        return self

    def next(self):
        if len(self.stack) == 0:
            raise StopIteration
        return self.stack.pop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.Print()
print s.next()
s.Print()
for element in s:
    print element
#s.Print()
