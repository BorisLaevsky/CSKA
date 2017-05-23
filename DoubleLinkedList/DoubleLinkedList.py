class Node:

    def __init__(self, value, previous_element = None, next_element = None):
        self.__previous_element = previous_element
        self.__value = value
        self.__next_element = next_element
        if isinstance(previous_element, Node):
           previous_element.__next_element = self
           self.__previous_element = previous_element
        if isinstance(next_element, Node):
           next_element.__previous_element = self
           self.__next_element = next_element

    def value(self):
        return self.__value

    def next_element(self):
        return self.__next_element

    def previous_element(self):
        return self.__previous_element

    def __str__(self):
        return str(self.__value)

x = Node(1)
y = Node(3, None, x)
print x.previous_element()
