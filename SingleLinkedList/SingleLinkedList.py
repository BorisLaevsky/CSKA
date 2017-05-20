class Node:

   def __init__(self, element, next_element):
       self.element = element
       self.next_element = next_element

   def __str__(self):
       return str(self.element)

   def next_value(self):
       return self.next_element

   def value(self):
       return self.elemtnt

x = Node(1, Node(2, Node(3, None)))
print x.next_value()
