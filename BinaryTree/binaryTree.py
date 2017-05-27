class Child:
    def __init__(self, value, key, parent = None, left_child = None, right_child = None):
        self.__value = value
        self.__parent = parent
        self.__key = key
        self.__left_child = left_child
        self.__right_child = right_child

    def __str__(self):
        return str(self.__value)

    def value(self):
        return self.__value

    def bottom_left(self):
        return self.__left_child

    def parent(self):
        return self.__parent

    def bottom_right(self):
        return self.__right_child

    def key(self):
        return self.__key

    def insert(self, value, key):
        if self.__key <= key:
           if isinstance(self.__right_child, Child):
              self.__right_child.insert(value, key)
           else:
              self.__right_child = Child(value, key, self)
        else:
           if isinstance(self.__left_child, Child):
              self.__left_child.insert(value, key)
           else:
              self.__left_child = Child(value, key, self)

    def find(self, key):
        if key != self.__key:
            if self.__key < key:
               return self.__right_child.find(key)
            else:
               return self.__left_child.find(key)
        else:
            return self

    def remove(self, key):
        removed_element = self.find(key)
        self.find(key).__key = None
        if isinstance(removed_element.__left_child, Child) and removed_element.__right_child == False:
           self.insert(removed_element.__left_child)
        if isinstance(removed_element.__right_child, Child) and removed_element.__left_child == False:
           self.insert(removed_element.__right_child)
        if isinstance(removed_element.__left_child, Child) and isinstance(removed_element.__right_child):
           self.insert(removed_element.__left_child)
           self.insert(removed_element.__right_child)



top = Child(1,1)
top.insert(2,2)
top.insert(3,3)
print top.bottom_right().bottom_right().value()
top.remove(2)
print top.bottom_right()
