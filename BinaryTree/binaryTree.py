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
            return self.value()

    def insert_child(self, child):
        if child == None:
           return self
        if self.__key <= child.__key:
           if isinstance(self.__right_child, Child):
              self.__right_child.insert_child(child)
           else:
              self.__right_child = child
              child.__parent = self
        else:
           if isinstance(self.__left_child, Child):
              self.__left_child.insert_child(child)
           else:
              self.__left_child = child
              child.__parent = self


    def remove(self, key):
        left_child_replacement = None
        right_child_replacement = None
        if isinstance(self.__left_child, Child) and key < self.__key:
           if self.__left_child.__key != key:
              self.__left_child.remove(key)
        if isinstance(self.__right_child, Child) and key > self.__key:
           if self.__right_child.__key != key:
              self.__right_child.remove(key)
        if isinstance(self.__right_child, Child) and  self.__right_child.__key == key:
           if isinstance(self.__right_child.__right_child, Child):
              right_child_replacement = self.__right_child.__right_child
           if isinstance(self.__right_child.__left_child, Child):
              left_child_replacement = self.__right_child.__left_child
           self.__right_child = None
           self.insert_child(left_child_replacement)
           self.insert_child(right_child_replacement)
        if isinstance(self.__left_child, Child) and  self.__left_child.__key == key:
           if isinstance(self.__left_child.__right_child, Child):
              right_child_replacement = self.__left_child.__right_child
           if isinstance(self.__left_child.__left_child, Child):
              left_child_replacement = self.__left_child.__left_child
           self.__left_child = None
           self.insert_child(left_child_replacement)
           self.insert_child(right_child_replacement)


top = Child(1,5)
top.insert(2,4)
top.insert(3,9)
top.insert(4,10)
top.insert(5,3)
top.remove(4)
print top.bottom_left()
