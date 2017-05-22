class Node:

    def __init__(self, previous_element, value, next_element):
        self.previous_element = previous_element
        self.value = value
        self.next_element = next_element
        if isinstance(previous_element, Node):
           previous_element.set_next_element(self)

    def value(self):
        return self.value

    def Next_element(self):
        return self.next_element

    def Previous_element(self):
        return self.previous_element

    def set_next_element(self, element):
        self.next_element = element
        element.previous_element= self

    def set_previous_element(self, element):
        self.previous_element = element
        element.next_element = self

    def __str__(self):
        return str(self.value)

#x = Node(None, 1, None)
#y = Node(None, 2, None)
#x.set_next_element(y)
#x.set_previous_element(Node(None, -1, None))
#print x.Next_element().Previous_element().Next_element()

#x = Node(None, 1, None)
#x = Node(None, 1, Node(x, 2, None))
#x = Node(Node(None, -1, x), 1, Node(x, 2, None))
#x = Node(Node(None, -1, x), 1, Node(x, 2, None))
#print x.Next_element().Previous_element().Next_element()

x = Node(None, 1, None)
y = Node(x, 2, None)
print x.Next_element()
print y.Previous_element()

