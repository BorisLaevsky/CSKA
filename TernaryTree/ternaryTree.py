class Child:
    def __init__(self, value, key, parent = None, left_child = None, middle_child = None, right_child = None):
        self.__value = value
        self.__key = key
        self.__left_child = left_child
        self.__middle_child = middle_child
        self.__right_child = right_child

    def __str__(self):
        return str(self.__value)

    def right_child(self):
        return self.__right_child

    def left_child(self):
        return self.__left_child

    def middle_child(self):
        return self.__middle_child

    def is_there_no_insert_space(self):
        count_of_empty_children = 0
        list_of_children = [self.__left_child, self.__middle_child, self.__right_child]
        for child in list_of_children:
            if child == None:
                 count_of_empty_children += 1
        if count_of_empty_children == 0:
            return True
        else:
            return False

    def insert(self, value, key_to_insert):
        if self.is_there_no_insert_space():
            self.__left_child.insert(value, key_to_insert)
        if self.__left_child == None and self.__middle_child == None and self.__right_child == None:
            self.__right_child = Child(value, key_to_insert, self)
        if self.__left_child == None and self.__middle_child == None and self.__right_child != None:
            if self.__right_child.__key > key_to_insert:
                self.__middle_child = Child(value, key_to_insert, self)
            else:
                self.__middle_child = self.__right_child
                self.__right_child = Child(value, key_to_insert, self)
        elif self.__left_child == None and self.__middle_child != None and self.__right_child == None:
            if self.__middle_child.__key > key_to_insert:
                self.__left_child = Child(value, key_to_insert, self)
            else:
               self.__left_child = self.__middle_child
               self.__middle_child = Child(value, key_to_insert, self)
        elif self.__left_child != None and self.__middle_child == None and self.__right_child == None:
            if self.__left_child.__key > key_to_insert:
                self.__left_child.insert(value, key_to_insert())
            else:
               self.__middle_child = Child(value, key_to_insert, self)
        elif self.__left_child == None and self.__middle_child != None and self.__right_child != None:
            if self.__right_child.__key > key_to_insert:
                if self.__middle_child.__key > key_to_insert:
                    self.__left_child = Child(value, key_to_insert, self)
                else:
                    self.__left_child = self.__middle_child
                    self.__middle_child = Child(value, key_to_insert, self)
            else:
                self.__left_child = self.__middle_child
                self.__middle_child = self.__right_child
                self.__right_child = Child(value, key_to_insert, self)
        elif self.__left_child != None and self.__middle_child != None and self.__right_child == None:
            if self.__middle_child.__key > key_to_insert:
                if self.__left_child.__key > key_to_insert:
                    self.__left_child.insert(value, key_to_insert)
                else:
                   self.__right_child = self.__middle_child
                   self.__middle_child = Child(value, key_to_insert, self)
            else:
                self.__right_child = Child(value, key_to_insert, self)
        elif self.__left_child != None and self.__middle_child == None and self.__right_child != None:
            if self.__right_child.__key > key_to_insert:
                if self.__left_child.__key < key_to_insert:
                    self.__middle_child = Child(value, key_to_insert, self)
                else:
                    self.__left_child.insert(value, key_to_insert)
            else:
                self.__middle_child = self.__right_child
                self.__right_child = Child(value, key_to_insert, self)




top = Child(1,1)
top.insert(2,2)
print top.right_child()
