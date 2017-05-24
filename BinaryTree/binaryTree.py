class Child:
    def __init__(self, value, key, parent = None, left_child = None, right_child = None):
        self.__value = value
        self.__parent = parent
        self.__key = key
        self.__left_child = left_child
        self.__right_child = right_child
        if isinstance(parent, Child):
           if self.__key < parent.__key:
              parent.__left_child = self
           else:
              parent.__right_child = self
        if isinstance(left_child, Child):
           left_child.__parent = self
        if isinstance(right_child, Child):
           right_child.__parent = self

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

    def get_key(self):
        return self.__key

    def parent(self):
        return self.__parent

top = Child(1,1)
left = Child(2, 0, top)
right = Child(3, 2, top)
print top.bottom_left()
print top.bottom_right()

