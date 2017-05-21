class Node:

    def __init__(self, previous_element, value, next_element):
        self.previous_element = previous_element
        self.value = value
        self.next_element = next_element

    def value(self):
        return self.value

    def Next_element(self):
        return self.next_element

    def Previous_element(self):
        return self.previous_element

    def add_next_element(self, element):
        self.next_element = element
        element.previous_element = self
        return element

    def __str__(self):
        return str(self.value)

x = Node(None, 1, None)
x.add_next_element(Node(None, 2, None)).add_next_element(Node(None, 3, None))
print x.Next_element().Next_element().Previous_element()

