class Child:
    def __init__(self, value, parent = None, child_orientation = None, left_child = None, right_child = None):
        self.__value = value
        self.__parent = parent
        self.__child_orientation = child_orientation
        self.__left_child = left_child
        self.__right_child = right_child
        if isinstance(parent, Child):
           if self.__child_orientation == "left":
              parent.__left_child = self
           if self.__child_orientation == "right":
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

top = Child(1)
left = Child(2, top, "left")
right = Child(3, top, "right")
print top.bottom_left()
print top.bottom_right()
