class Node:

   def __init__(self, value, next_val):
       self.value = value
       self.next_val = next_val

   def __str__(self):
       return str(self.value)

   def next_element(self):
       return self.next_val

   def value(self):
       return self.value

x = Node(1, Node(2, Node(3, None)))
print x.next_element()
