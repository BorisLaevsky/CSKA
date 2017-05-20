class Node:

   def __init__(self, val, next_val):
       self.val = val
       self.next_val = next_val

   def __str__(self):
       return str(self.val)

   def next_element(self):
       return self.next_val

   def value(self):
       return self.val

x = Node(1, Node(2, Node(3, None)))
