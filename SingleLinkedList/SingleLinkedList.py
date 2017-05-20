class Node:

   def __init__(self, value, next_element):
       self.Value = value
       self.next_Element = next_element

   def __str__(self):
       return str(self.Value)

   def next_element(self):
       return self.next_Element

   def value(self):
       print self.Value

x = Node(1, Node(2, Node(3, None)))
x.value()
